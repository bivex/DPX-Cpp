"""Tests for C++ Namespace Dependency Graph and Circular Dependency Detection."""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter
from pattern_detector.domain.rules.circular_dependency_rule import CircularDependencyRule
from pattern_detector.domain.value_objects import PatternType


def test_circular_dependency_detection_cpp() -> None:
    code_a = """
    #include "BetaService.hpp"

    namespace alpha {
    class AlphaService {};
    }
    """
    code_b = """
    #include "AlphaService.hpp"

    namespace beta {
    class BetaService {};
    }
    """

    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({
        "AlphaService.hpp": code_a,
        "BetaService.hpp": code_b,
    })

    cycles = model.find_circular_dependencies()
    assert len(cycles) == 1
    assert set(cycles[0]) == {"alpha", "beta"}

    rule = CircularDependencyRule()
    detections = rule.detect(model)
    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CIRCULAR_DEPENDENCY
    assert detections[0].confidence.score >= 0.80
