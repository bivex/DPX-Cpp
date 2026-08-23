"""Inbound Driving Adapter: CLI interface using Typer and Rich."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from pattern_detector.bootstrap.container import create_container
from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.ports.inbound import ScanOptions

app = typer.Typer(
    name="pattern-detector",
    help="Hexagonal DDD Pattern Scanner & Detector for C++ (C++14/17/20).",
    add_completion=False,
)
console = Console()


@app.command(name="scan")
def scan(
    path: Annotated[
        str,
        typer.Argument(
            help="File or directory path to scan for design patterns.",
        ),
    ] = ".",
    min_confidence: Annotated[
        float,
        typer.Option(
            "--min-confidence",
            "-c",
            help="Minimum confidence threshold (0.0 - 1.0).",
        ),
    ] = 0.0,
    pattern: Annotated[
        list[str] | None,
        typer.Option(
            "--pattern",
            "-p",
            help="Specific pattern types to look for (can be specified multiple times).",
        ),
    ] = None,
    json_output: Annotated[
        str | None,
        typer.Option(
            "--json",
            "-j",
            help="Export results to a JSON file destination.",
        ),
    ] = None,
    html_output: Annotated[
        str | None,
        typer.Option(
            "--html",
            "-H",
            help="Export results to an interactive HTML report dashboard.",
        ),
    ] = None,
    markdown_output: Annotated[
        str | None,
        typer.Option(
            "--markdown",
            "-m",
            help="Export results to a Markdown report file.",
        ),
    ] = None,
    llm: Annotated[
        bool,
        typer.Option(
            "--llm",
            "-L",
            help="Output token-efficient structured XML/Markdown context optimized for LLMs and AI coding agents.",
        ),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            "-v",
            help="Enable verbose output.",
        ),
    ] = False,
) -> None:
    """Scan a C++ source code file or directory for software design patterns."""
    target_path = str(Path(path).resolve())

    container = create_container()
    scanner = container.get_scanner()

    options = ScanOptions(
        min_confidence=min_confidence,
        enabled_patterns=pattern or [],
        output_json_path=json_output,
        output_html_path=html_output,
        output_markdown_path=markdown_output,
        verbose=verbose,
    )

    if llm:
        report = scanner.scan_path(target_path, options=options)
        print(container.llm_formatter.format_scan_report(report))
        return

    with console.status(f"[cyan]Scanning [bold]{path}[/bold] using ANTLR parser & Domain Rules...[/cyan]"):
        report = scanner.scan_path(target_path, options=options)

    # Render formatted report to terminal
    container.report_formatter.render_to_console(report, console, verbose=verbose)  # type: ignore[attr-defined]

    if json_output:
        console.print(f"[bold green]✔[/bold green] Full JSON detection report exported to: [underline]{json_output}[/underline]")
    if html_output:
        console.print(f"[bold green]✔[/bold green] Interactive HTML dashboard exported to: [underline]{html_output}[/underline]")
    if markdown_output:
        console.print(f"[bold green]✔[/bold green] Markdown report exported to: [underline]{markdown_output}[/underline]")
    if json_output or html_output or markdown_output:
        console.print()


@app.command(name="rules")
def list_rules() -> None:
    """Display catalog of all registered pattern detection rules and heuristics."""
    table = Table(title="📐 Registered Design Pattern Rules & Heuristics", border_style="bright_blue", show_header=True)
    table.add_column("Pattern Type", style="bold cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Intent & Detection Strategy", style="white")
    table.add_column("Tags", style="dim")

    for p_type, p_def in PATTERN_CATALOG.items():
        tags_str = ", ".join(p_def.tags)
        desc = f"[bold]{p_def.name}[/bold]\n{p_def.description}\n[dim]Intent: {p_def.intent}[/dim]"
        table.add_row(p_type.value, p_def.category.value.upper(), desc, tags_str)

    console.print(table)


@app.command(name="dataflow")
def dataflow(
    target: Annotated[
        str | None,
        typer.Argument(
            help="Target variable, field, or object. If omitted or '--all', analyzes ALL variables in file/project.",
        ),
    ] = None,
    path: Annotated[
        str,
        typer.Option(
            "--path",
            "-p",
            help="File or directory path containing C++ source code.",
        ),
    ] = ".",
    all_vars: Annotated[
        bool,
        typer.Option(
            "--all",
            "-a",
            help="Analyze and summarize data flow for ALL variables in the file/project.",
        ),
    ] = False,
    file_filter: Annotated[
        str | None,
        typer.Option(
            "--file",
            "-f",
            help="Filter analysis to variables inside a specific source file.",
        ),
    ] = None,
    direction: Annotated[
        str,
        typer.Option(
            "--direction",
            "-d",
            help="Direction of data flow: 'out' (forward) or 'in' (backward).",
        ),
    ] = "out",
    variant: Annotated[
        str,
        typer.Option(
            "--variant",
            "-v",
            help="Visualization variant: 'simplified', 'cluster', 'relationship'.",
        ),
    ] = "simplified",
    to_entity: Annotated[
        str | None,
        typer.Option(
            "--to",
            help="Second entity to trace paths between (for relationship variant).",
        ),
    ] = None,
    mermaid: Annotated[
        bool,
        typer.Option(
            "--mermaid",
            "-m",
            help="Output Mermaid.js graph code.",
        ),
    ] = False,
    llm: Annotated[
        bool,
        typer.Option(
            "--llm",
            "-L",
            help="Output token-efficient structured XML/text context for LLMs and AI agents.",
        ),
    ] = False,
    html_output: Annotated[
        str | None,
        typer.Option(
            "--html",
            "-H",
            help="Export interactive HTML report using Vis.js visualizer.",
        ),
    ] = None,
    json_output: Annotated[
        str | None,
        typer.Option(
            "--json",
            "-j",
            help="Export graph or summary report data to a JSON file.",
        ),
    ] = None,
    max_depth: Annotated[
        int,
        typer.Option(
            "--max-depth",
            help="Maximum propagation traversal depth.",
        ),
    ] = 15,
) -> None:
    """Trace forward (Data Flow Out) or backward (Data Flow In) propagation graph for one or ALL variables."""
    target_path = str(Path(path).resolve())
    container = create_container()

    # If no target specified or --all requested: Analyze ALL variables
    if target is None or all_vars:
        summary_report = container.scanning_service.analyze_all_data_flows(
            target_path=target_path,
            direction=direction,
            file_filter=file_filter,
            max_depth=max_depth,
        )

        if llm:
            print(container.llm_formatter.format_data_flow_summary(summary_report))
            return

        console.print(summary_report.to_rich_table())

        if html_output:
            html_content = container.data_flow_html_formatter.format_summary_report(summary_report)
            Path(html_output).parent.mkdir(parents=True, exist_ok=True)
            with open(html_output, "w", encoding="utf-8") as f:
                f.write(html_content)
            console.print(f"\n[bold green]✔[/bold green] Interactive HTML report exported to: [underline]{html_output}[/underline]")

        if json_output:
            import json

            Path(json_output).parent.mkdir(parents=True, exist_ok=True)
            with open(json_output, "w", encoding="utf-8") as f:
                json.dump(summary_report.to_json(), f, indent=2)
            console.print(f"\n[bold green]✔[/bold green] Data flow summary JSON exported to: [underline]{json_output}[/underline]")
        return

    # Single variable flow analysis
    graph = container.scanning_service.analyze_data_flow(
        target_path=target_path,
        target_entity=target,
        direction=direction,
        variant=variant,
        to_entity=to_entity,
        max_depth=max_depth,
    )

    if llm:
        print(container.llm_formatter.format_data_flow_graph(graph))
        return

    if mermaid:
        console.print(f"[bold green]Mermaid Diagram for Data Flow ({graph.direction.value}):[/bold green]\n")
        console.print(f"```mermaid\n{graph.to_mermaid()}\n```")
    else:
        title = f"Data Flow {graph.direction.value}: '{target}'"
        if to_entity:
            title += f" ➔ '{to_entity}'"
        console.print(Panel(graph.to_rich_tree(), title=f"📊 [bold cyan]{title}[/bold cyan]", border_style="bright_blue"))

    if html_output:
        html_content = container.data_flow_html_formatter.format_single_graph(graph)
        Path(html_output).parent.mkdir(parents=True, exist_ok=True)
        with open(html_output, "w", encoding="utf-8") as f:
            f.write(html_content)
        console.print(f"\n[bold green]✔[/bold green] Interactive HTML report exported to: [underline]{html_output}[/underline]")

    if json_output:
        import json

        Path(json_output).parent.mkdir(parents=True, exist_ok=True)
        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(graph.to_json(), f, indent=2)
        console.print(f"\n[bold green]✔[/bold green] Data flow graph JSON exported to: [underline]{json_output}[/underline]")


@app.command(name="info")
def info() -> None:
    """Display architecture info and supported grammar configurations."""
    info_text = (
        "[bold magenta]Pattern Scanner & Detector (Hexagonal DDD Architecture)[/bold magenta]\n\n"
        "• [bold cyan]Core Domain:[/bold cyan] Agnostic CodeModel, Evidence & Confidence Score Engine, Specification Rules\n"
        "• [bold cyan]Inbound Ports:[/bold cyan] ScannerPort, DetectorPort, DataFlowPort\n"
        "• [bold cyan]Outbound Ports:[/bold cyan] ParserPort, SourceProviderPort, ResultRepositoryPort, ReportFormatterPort\n"
        "• [bold cyan]Active Grammar Adapter:[/bold cyan] ANTLR 4.13.2 C++ Grammar (CPP14Lexer.g4 / CPP14Parser.g4)\n"
        "• [bold cyan]Supported Extensions:[/bold cyan] .cpp, .hpp, .h, .cc, .cxx, .hxx, .hh, .C\n"
        "• [bold cyan]Features:[/bold cyan] 23/23 GoF Patterns, SOLID Principles, Data Flow Out / In Analysis\n"
    )
    console.print(Panel(info_text, title="ℹ System Info", border_style="cyan"))


def main() -> None:
    app()


if __name__ == "__main__":
    main()
