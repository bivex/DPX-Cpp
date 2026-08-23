"""Tests for design pattern rules on Java source code."""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter
from pattern_detector.domain.rules.lifecycle_rule import LifecycleComponentPatternRule
from pattern_detector.domain.rules.singleton_rule import SingletonPatternRule
from pattern_detector.domain.rules.strategy_rule import StrategyPatternRule
from pattern_detector.domain.value_objects import PatternType


def test_strategy_pattern_java() -> None:
    code = """
    package com.example.strategy;

    public interface SortStrategy {
        void sort(int[] array);
    }

    public class QuickSort implements SortStrategy {
        public void sort(int[] array) {}
    }

    public class MergeSort implements SortStrategy {
        public void sort(int[] array) {}
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"SortStrategy.java": code})
    detections = StrategyPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.STRATEGY
    assert detections[0].target_name == "SortStrategy"


def test_singleton_pattern_java() -> None:
    code = """
    package com.example.singleton;

    public class AppConfig {
        private static final AppConfig INSTANCE = new AppConfig();
        private AppConfig() {}

        public static AppConfig getInstance() {
            return INSTANCE;
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"AppConfig.java": code})
    detections = SingletonPatternRule().detect(model)
    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.SINGLETON for d in detections)


def test_lifecycle_component_pattern_java() -> None:
    code = """
    package com.example.lifecycle;

    public interface Lifecycle {
        void start();
        void stop();
    }

    public class HttpServerComponent implements Lifecycle {
        public void start() {
            System.out.println("Starting server");
        }
        public void stop() {
            System.out.println("Stopping server");
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"Lifecycle.java": code})
    detections = LifecycleComponentPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.LIFECYCLE_COMPONENT
