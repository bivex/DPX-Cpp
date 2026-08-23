"""Tests for Java Package Dependency Graph and Circular Dependency Detection."""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter
from pattern_detector.domain.rules.circular_dependency_rule import CircularDependencyRule
from pattern_detector.domain.value_objects import PatternType


def test_circular_dependency_detection_java() -> None:
    code_a = """
    package com.example.alpha;

    import com.example.beta.BetaService;

    public class AlphaService {
        private BetaService beta;
    }
    """
    code_b = """
    package com.example.beta;

    import com.example.alpha.AlphaService;

    public class BetaService {
        private AlphaService alpha;
    }
    """

    adapter = JavaAntlrParserAdapter()
    model = adapter.parse_sources({
        "AlphaService.java": code_a,
        "BetaService.java": code_b,
    })

    cycles = model.find_circular_dependencies()
    assert len(cycles) == 1
    assert set(cycles[0]) == {"com.example.alpha", "com.example.beta"}

    rule = CircularDependencyRule()
    detections = rule.detect(model)
    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CIRCULAR_DEPENDENCY
    assert detections[0].confidence.score >= 0.80
