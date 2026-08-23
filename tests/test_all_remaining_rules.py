"""Tests for design pattern rules on C++ source code."""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter
from pattern_detector.domain.rules.abstract_factory_rule import AbstractFactoryRule
from pattern_detector.domain.rules.bridge_rule import BridgePatternRule
from pattern_detector.domain.rules.composite_rule import CompositePatternRule
from pattern_detector.domain.rules.iterator_rule import IteratorPatternRule
from pattern_detector.domain.rules.mediator_rule import MediatorPatternRule
from pattern_detector.domain.value_objects import PatternType


def test_abstract_factory_rule_cpp() -> None:
    code = """
    #include <memory>

    namespace factory {

    class IButton { public: virtual ~IButton() = default; };
    class ICheckbox { public: virtual ~ICheckbox() = default; };
    class WinButton : public IButton {};
    class WinCheckbox : public ICheckbox {};
    class MacButton : public IButton {};
    class MacCheckbox : public ICheckbox {};

    class IGUIFactory {
    public:
        virtual ~IGUIFactory() = default;
        virtual std::unique_ptr<IButton> createButton() = 0;
        virtual std::unique_ptr<ICheckbox> createCheckbox() = 0;
    };

    class WinFactory : public IGUIFactory {
    public:
        std::unique_ptr<IButton> createButton() override { return std::make_unique<WinButton>(); }
        std::unique_ptr<ICheckbox> createCheckbox() override { return std::make_unique<WinCheckbox>(); }
    };

    class MacFactory : public IGUIFactory {
    public:
        std::unique_ptr<IButton> createButton() override { return std::make_unique<MacButton>(); }
        std::unique_ptr<ICheckbox> createCheckbox() override { return std::make_unique<MacCheckbox>(); }
    };

    } // namespace factory
    """
    model = CppAntlrParserAdapter().parse_sources({"GUIFactory.hpp": code})
    detections = AbstractFactoryRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.ABSTRACT_FACTORY
    assert detections[0].target_name == "IGUIFactory"


def test_composite_rule_cpp() -> None:
    code = """
    #include <vector>
    #include <memory>

    namespace composite {

    class IGraphic {
    public:
        virtual ~IGraphic() = default;
        virtual void draw() = 0;
    };

    class Dot : public IGraphic {
    public:
        void draw() override {}
    };

    class CompoundGraphic : public IGraphic {
    public:
        void draw() override {
            for (auto& g : children_) { g->draw(); }
        }
    private:
        std::vector<std::shared_ptr<IGraphic>> children_;
    };

    } // namespace composite
    """
    model = CppAntlrParserAdapter().parse_sources({"Graphic.hpp": code})
    detections = CompositePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.COMPOSITE
    assert detections[0].target_name == "IGraphic"


def test_bridge_rule_cpp() -> None:
    code = """
    #include <string>
    #include <memory>

    namespace bridge {

    class IDatabaseDriver {
    public:
        virtual ~IDatabaseDriver() = default;
        virtual void executeQuery(const std::string& sql) = 0;
    };

    class DatabaseService {
    public:
        void run(const std::string& sql) {
            if (driver) { driver->executeQuery(sql); }
        }
    private:
        std::shared_ptr<IDatabaseDriver> driver;
    };

    } // namespace bridge
    """
    model = CppAntlrParserAdapter().parse_sources({"Bridge.hpp": code})
    detections = BridgePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.BRIDGE


def test_iterator_rule_cpp() -> None:
    code = """
    #include <string>

    namespace iter {

    class ICustomIterator {
    public:
        virtual ~ICustomIterator() = default;
        virtual bool hasNext() = 0;
        virtual std::string next() = 0;
    };

    } // namespace iter
    """
    model = CppAntlrParserAdapter().parse_sources({"CustomIterator.hpp": code})
    detections = IteratorPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.ITERATOR


def test_mediator_rule_cpp() -> None:
    code = """
    #include <string>

    namespace mediator {

    class IEventBroker {
    public:
        virtual ~IEventBroker() = default;
        virtual void publish(const std::string& topic, const std::string& msg) = 0;
        virtual void subscribe(const std::string& topic) = 0;
    };

    class MessageHub : public IEventBroker {
    public:
        void publish(const std::string& topic, const std::string& msg) override {}
        void subscribe(const std::string& topic) override {}
    };

    } // namespace mediator
    """
    model = CppAntlrParserAdapter().parse_sources({"Mediator.hpp": code})
    detections = MediatorPatternRule().detect(model)
    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.MEDIATOR for d in detections)
