"""Tests for design pattern rules on Java source code."""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter
from pattern_detector.domain.rules.abstract_factory_rule import AbstractFactoryRule
from pattern_detector.domain.rules.bridge_rule import BridgePatternRule
from pattern_detector.domain.rules.composite_rule import CompositePatternRule
from pattern_detector.domain.rules.iterator_rule import IteratorPatternRule
from pattern_detector.domain.rules.mediator_rule import MediatorPatternRule
from pattern_detector.domain.value_objects import PatternType


def test_abstract_factory_rule_java() -> None:
    code = """
    package com.example.factory;

    public interface GUIFactory {
        Button createButton();
        Checkbox createCheckbox();
    }

    public class WinFactory implements GUIFactory {
        public Button createButton() { return new WinButton(); }
        public Checkbox createCheckbox() { return new WinCheckbox(); }
    }

    public class MacFactory implements GUIFactory {
        public Button createButton() { return new MacButton(); }
        public Checkbox createCheckbox() { return new MacCheckbox(); }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"GUIFactory.java": code})
    detections = AbstractFactoryRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.ABSTRACT_FACTORY
    assert detections[0].target_name == "GUIFactory"


def test_composite_rule_java() -> None:
    code = """
    package com.example.composite;

    import java.util.List;
    import java.util.ArrayList;

    public interface Graphic {
        void draw();
    }

    public class Dot implements Graphic {
        public void draw() {}
    }

    public class CompoundGraphic implements Graphic {
        private List<Graphic> children = new ArrayList<>();
        public void draw() {
            for (Graphic g : children) { g.draw(); }
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"Graphic.java": code})
    detections = CompositePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.COMPOSITE
    assert detections[0].target_name == "Graphic"


def test_bridge_rule_java() -> None:
    code = """
    package com.example.bridge;

    public interface DatabaseDriver {
        void executeQuery(String sql);
    }

    public class DatabaseService {
        private DatabaseDriver driver;
        public void run(String sql) {
            driver.executeQuery(sql);
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"Bridge.java": code})
    detections = BridgePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.BRIDGE


def test_iterator_rule_java() -> None:
    code = """
    package com.example.iter;

    public interface CustomIterator {
        boolean hasNext();
        Object next();
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"CustomIterator.java": code})
    detections = IteratorPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.ITERATOR


def test_mediator_rule_java() -> None:
    code = """
    package com.example.mediator;

    public interface EventBroker {
        void publish(String topic, Object msg);
        void subscribe(String topic, Object handler);
    }

    public class MessageHub implements EventBroker {
        public void publish(String topic, Object msg) {}
        public void subscribe(String topic, Object handler) {}
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"Mediator.java": code})
    detections = MediatorPatternRule().detect(model)
    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.MEDIATOR for d in detections)
