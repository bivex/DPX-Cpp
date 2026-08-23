"""Tests for Java ANTLR4 Parser Adapter and Java Pattern Detection."""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import PatternType


def test_java_parser_extracts_classes_and_interfaces() -> None:
    java_code = """
    package com.example.service;

    import java.util.List;

    public interface OrderProcessor {
        void processOrder(int orderId);
        boolean validate(String customerId);
    }

    public class StandardOrderProcessor implements OrderProcessor {
        private String endpoint;

        public void processOrder(int orderId) {
            System.out.println("Processing order: " + orderId);
        }

        public boolean validate(String customerId) {
            return customerId != null;
        }
    }
    """

    adapter = JavaAntlrParserAdapter()
    model = adapter.parse_sources({"OrderProcessor.java": java_code})

    assert "com.example.service" in model.namespaces
    ns = model.namespaces["com.example.service"]
    assert "OrderProcessor" in ns.protocols
    assert len(ns.protocols["OrderProcessor"].methods) == 2
    assert "StandardOrderProcessor" in ns.records
    assert "OrderProcessor" in ns.records["StandardOrderProcessor"].implemented_protocols


def test_java_pattern_detection_strategy_and_composite() -> None:
    java_code = """
    package com.example.design;

    import java.util.List;
    import java.util.ArrayList;

    public interface Graphic {
        void render();
    }

    public class Circle implements Graphic {
        public void render() {
            System.out.println("Circle");
        }
    }

    public class CanvasContainer implements Graphic {
        private List<Graphic> children = new ArrayList<>();

        public void render() {
            for (Graphic g : children) {
                g.render();
            }
        }
    }
    """

    adapter = JavaAntlrParserAdapter()
    model = adapter.parse_sources({"Graphic.java": java_code})
    detector = PatternDetectorService(rules=get_default_rules())
    report = detector.detect_all(model)

    assert report.total_detections_count >= 1
    pattern_types = [d.pattern_type for d in report.detections]
    assert PatternType.STRATEGY in pattern_types or PatternType.COMPOSITE in pattern_types
