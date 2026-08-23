"""Tests for C++ ANTLR4 Parser Adapter and C++ Pattern Detection."""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import PatternType


def test_cpp_parser_extracts_classes_and_interfaces() -> None:
    cpp_code = """
    #include <iostream>
    #include <string>

    namespace service {

    class IOrderProcessor {
    public:
        virtual ~IOrderProcessor() = default;
        virtual void processOrder(int orderId) = 0;
        virtual bool validate(const std::string& customerId) = 0;
    };

    class StandardOrderProcessor : public IOrderProcessor {
    public:
        void processOrder(int orderId) override {
            std::cout << "Processing order: " << orderId << std::endl;
        }

        bool validate(const std::string& customerId) override {
            return !customerId.empty();
        }
    };

    } // namespace service
    """

    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({"OrderProcessor.hpp": cpp_code})

    assert "service" in model.namespaces
    ns = model.namespaces["service"]
    assert "IOrderProcessor" in ns.protocols
    assert "StandardOrderProcessor" in ns.records
    assert "IOrderProcessor" in ns.records["StandardOrderProcessor"].implemented_protocols


def test_cpp_pattern_detection_strategy_and_composite() -> None:
    cpp_code = """
    #include <vector>
    #include <memory>
    #include <iostream>

    namespace graphics {

    class IGraphic {
    public:
        virtual ~IGraphic() = default;
        virtual void render() = 0;
    };

    class Circle : public IGraphic {
    public:
        void render() override {
            std::cout << "Circle" << std::endl;
        }
    };

    class CanvasContainer : public IGraphic {
    public:
        void render() override {
            for (auto& g : children_) {
                g->render();
            }
        }
    private:
        std::vector<std::shared_ptr<IGraphic>> children_;
    };

    } // namespace graphics
    """

    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources({"Graphic.hpp": cpp_code})
    detector = PatternDetectorService(rules=get_default_rules())
    report = detector.detect_all(model)

    assert report.total_detections_count >= 1
    pattern_types = [d.pattern_type for d in report.detections]
    assert PatternType.STRATEGY in pattern_types or PatternType.COMPOSITE in pattern_types or PatternType.OPEN_CLOSED in pattern_types
