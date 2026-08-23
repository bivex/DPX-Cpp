"""Tests for design pattern rules on C++ source code."""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter
from pattern_detector.domain.rules.lifecycle_rule import LifecycleComponentPatternRule
from pattern_detector.domain.rules.singleton_rule import SingletonPatternRule
from pattern_detector.domain.rules.strategy_rule import StrategyPatternRule
from pattern_detector.domain.value_objects import PatternType


def test_strategy_pattern_cpp() -> None:
    code = """
    #include <vector>

    namespace algorithms {

    class ISortStrategy {
    public:
        virtual ~ISortStrategy() = default;
        virtual void sort(std::vector<int>& data) = 0;
    };

    class QuickSort : public ISortStrategy {
    public:
        void sort(std::vector<int>& data) override {}
    };

    class MergeSort : public ISortStrategy {
    public:
        void sort(std::vector<int>& data) override {}
    };

    } // namespace algorithms
    """
    model = CppAntlrParserAdapter().parse_sources({"SortStrategy.hpp": code})
    detections = StrategyPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.STRATEGY
    assert detections[0].target_name == "ISortStrategy"


def test_singleton_pattern_cpp() -> None:
    code = """
    namespace config {

    class AppConfig {
    public:
        static AppConfig& getInstance() {
            static AppConfig instance;
            return instance;
        }

    private:
        AppConfig() = default;
        AppConfig(const AppConfig&) = delete;
        AppConfig& operator=(const AppConfig&) = delete;
    };

    } // namespace config
    """
    model = CppAntlrParserAdapter().parse_sources({"AppConfig.hpp": code})
    detections = SingletonPatternRule().detect(model)
    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.SINGLETON for d in detections)


def test_lifecycle_component_pattern_cpp() -> None:
    code = """
    #include <iostream>

    namespace server {

    class ILifecycle {
    public:
        virtual ~ILifecycle() = default;
        virtual void start() = 0;
        virtual void stop() = 0;
    };

    class HttpServerComponent : public ILifecycle {
    public:
        void start() override {
            std::cout << "Starting server" << std::endl;
        }
        void stop() override {
            std::cout << "Stopping server" << std::endl;
        }
    };

    } // namespace server
    """
    model = CppAntlrParserAdapter().parse_sources({"Lifecycle.hpp": code})
    detections = LifecycleComponentPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.LIFECYCLE_COMPONENT
