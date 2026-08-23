"""Tests for Data Flow Analysis (SciTools Understand Data Flow Out/In Parity)."""

from __future__ import annotations

from pathlib import Path
from typer.testing import CliRunner

from pattern_detector.adapters.inbound.cli.main import app
from pattern_detector.adapters.outbound.antlr import CppAntlrParserAdapter
from pattern_detector.bootstrap.container import create_container
from pattern_detector.domain.data_flow import (
    DataFlowDirection,
    DataFlowVariant,
    NodeKind,
)
from pattern_detector.domain.services.data_flow import DataFlowService

SAMPLE_CPP = """
extern int auxData;
extern int transformedData;
extern int outputResult;
extern int logBuffer;
extern int runningTotal;
extern int reportValue;

void normalize()
{
    if (transformedData > 100)
        transformedData = 100;
    else
        transformedData = transformedData + auxData;
}

void output()
{
    outputResult = transformedData;
}

void logData()
{
    logBuffer += transformedData;
}

void accumulate()
{
    runningTotal += outputResult;
}

void report()
{
    reportValue = runningTotal;
}
"""


def test_data_flow_out_extraction_and_graph() -> None:
    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({"sample.cpp": SAMPLE_CPP})

    # Verify states and functions
    states = [s.name for s in model.all_states()]
    assert "transformedData" in states
    assert "outputResult" in states
    assert "runningTotal" in states
    assert "reportValue" in states

    service = DataFlowService()
    graph = service.trace_data_flow_out(model, "transformedData")

    assert graph.direction == DataFlowDirection.OUT
    assert graph.root_id == "transformedData"
    assert "transformedData" in graph.nodes
    assert "fn_normalize" in graph.nodes
    assert "fn_output" in graph.nodes
    assert "outputResult" in graph.nodes
    assert "fn_accumulate" in graph.nodes
    assert "runningTotal" in graph.nodes
    assert "fn_report" in graph.nodes
    assert "reportValue" in graph.nodes

    # Check edges
    edge_pairs = [(e.from_id, e.to_id, e.kind) for e in graph.edges]
    assert ("transformedData", "fn_normalize", "READS") in edge_pairs
    assert ("transformedData", "fn_output", "READS") in edge_pairs
    assert ("fn_output", "outputResult", "WRITES") in edge_pairs
    assert ("outputResult", "fn_accumulate", "READS") in edge_pairs
    assert ("fn_accumulate", "runningTotal", "MODIFIES") in edge_pairs
    assert ("runningTotal", "fn_report", "READS") in edge_pairs
    assert ("fn_report", "reportValue", "WRITES") in edge_pairs


def test_data_flow_in_backward_slice() -> None:
    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({"sample.cpp": SAMPLE_CPP})

    service = DataFlowService()
    graph = service.trace_data_flow_in(model, "reportValue")

    assert graph.direction == DataFlowDirection.IN
    assert graph.root_id == "reportValue"
    assert "reportValue" in graph.nodes
    assert "fn_report" in graph.nodes
    assert "runningTotal" in graph.nodes
    assert "fn_accumulate" in graph.nodes
    assert "outputResult" in graph.nodes
    assert "fn_output" in graph.nodes
    assert "transformedData" in graph.nodes


def test_data_flow_relationship_path() -> None:
    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({"sample.cpp": SAMPLE_CPP})

    service = DataFlowService()
    graph = service.trace_relationship(model, source="transformedData", target="reportValue")

    assert graph.variant == DataFlowVariant.RELATIONSHIP
    assert "transformedData" in graph.nodes
    assert "reportValue" in graph.nodes
    # Should contain intermediate chain nodes
    assert "outputResult" in graph.nodes
    assert "runningTotal" in graph.nodes
    # But logBuffer should NOT be in the path to reportValue
    assert "logBuffer" not in graph.nodes


def test_data_flow_mermaid_rendering() -> None:
    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({"sample.cpp": SAMPLE_CPP})

    service = DataFlowService()
    graph = service.trace_data_flow_out(model, "transformedData")
    mermaid = graph.to_mermaid(direction_layout="LR")

    assert "graph LR" in mermaid
    assert "transformedData" in mermaid
    assert "reportValue" in mermaid
    assert "reads" in mermaid
    assert "writes" in mermaid


def test_data_flow_cli_command(tmp_path: Path) -> None:
    runner = CliRunner()
    sample_file = tmp_path / "data_flow_sample.cpp"
    sample_file.write_text(SAMPLE_CPP)

    # Test CLI dataflow command
    result = runner.invoke(app, ["dataflow", "transformedData", "--path", str(sample_file)])
    assert result.exit_code == 0
    assert "transformedData" in result.stdout
    assert "outputResult" in result.stdout

    # Test CLI mermaid output
    result_m = runner.invoke(app, ["dataflow", "transformedData", "--path", str(sample_file), "--mermaid"])
    assert result_m.exit_code == 0
    assert "```mermaid" in result_m.stdout
    assert "graph LR" in result_m.stdout

    # Test CLI JSON output
    json_dest = tmp_path / "df.json"
    result_j = runner.invoke(
        app, ["dataflow", "transformedData", "--path", str(sample_file), "--json", str(json_dest)]
    )
    assert result_j.exit_code == 0
    assert json_dest.exists()


def test_data_flow_all_variables_summary_matrix(tmp_path: Path) -> None:
    runner = CliRunner()
    sample_file = tmp_path / "data_flow_batch.cpp"
    sample_file.write_text(SAMPLE_CPP)

    # Test CLI dataflow --all
    result_all = runner.invoke(app, ["dataflow", "--all", "--path", str(sample_file)])
    assert result_all.exit_code == 0
    assert "Data Flow Summary Matrix" in result_all.stdout
    assert "auxData" in result_all.stdout
    assert "transformedData" in result_all.stdout
    assert "outputResult" in result_all.stdout
    assert "runningTotal" in result_all.stdout

    # Test summary JSON output
    json_dest = tmp_path / "summary.json"
    result_json = runner.invoke(app, ["dataflow", "--all", "--path", str(sample_file), "--json", str(json_dest)])
    assert result_json.exit_code == 0
    assert json_dest.exists()


def test_data_flow_html_report_export(tmp_path: Path) -> None:
    runner = CliRunner()
    sample_file = tmp_path / "data_flow_html_sample.cpp"
    sample_file.write_text(SAMPLE_CPP)

    # 1. Test single-variable HTML export
    html_single = tmp_path / "single_flow.html"
    res_single = runner.invoke(
        app, ["dataflow", "transformedData", "--path", str(sample_file), "--html", str(html_single)]
    )
    assert res_single.exit_code == 0
    assert html_single.exists()
    content_single = html_single.read_text(encoding="utf-8")
    assert "vis.Network" in content_single
    assert "transformedData" in content_single

    # 2. Test batch summary HTML export
    html_all = tmp_path / "all_flows.html"
    res_all = runner.invoke(app, ["dataflow", "--all", "--path", str(sample_file), "--html", str(html_all)])
    assert res_all.exit_code == 0
    assert html_all.exists()
    content_all = html_all.read_text(encoding="utf-8")
    assert "vis.Network" in content_all
    assert "auxData" in content_all
    assert "reportValue" in content_all


