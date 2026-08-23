"""Unit tests for SOLID Principles, Clean Code, Coupling & Cohesion Rules for C++."""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter
from pattern_detector.domain.rules.cohesion_coupling_rule import CohesionCouplingRule
from pattern_detector.domain.rules.composition_over_inheritance_rule import CompositionOverInheritanceRule
from pattern_detector.domain.rules.dip_rule import DependencyInversionRule
from pattern_detector.domain.rules.dry_rule import DryRule
from pattern_detector.domain.rules.isp_rule import InterfaceSegregationRule
from pattern_detector.domain.rules.kiss_rule import KissRule
from pattern_detector.domain.rules.law_of_demeter_rule import LawOfDemeterRule
from pattern_detector.domain.rules.lsp_rule import LiskovSubstitutionRule
from pattern_detector.domain.rules.ocp_rule import OpenClosedPrincipleRule
from pattern_detector.domain.rules.srp_rule import SingleResponsibilityRule
from pattern_detector.domain.value_objects import PatternCategory, PatternType


def test_srp_god_object_violation() -> None:
    code = """
    namespace service {

    class MegaGodManager {
    public:
        void saveToDatabase() {}
        void deleteFromDatabase() {}
        void queryDatabase() {}
        void handleHttpRequest() {}
        void getHttpEndpoint() {}
        void serializeToJson() {}
        void parseXml() {}
        void authenticateUser() {}
        void calculateTaxes() {}
        void computeDiscounts() {}
        void processOrder() {}
        void validatePayment() {}
    };

    } // namespace service
    """
    model = CppAntlrParserAdapter().parse_sources({"MegaGodManager.hpp": code})
    detections = SingleResponsibilityRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.SINGLE_RESPONSIBILITY
    assert detections[0].pattern_category == PatternCategory.PRINCIPLE


def test_ocp_dynamic_cast_cascade_violation() -> None:
    code = """
    #include <iostream>

    namespace graphics {

    class ShapeDrawer {
    public:
        void drawShape(Shape* shape) {
            if (dynamic_cast<Circle*>(shape)) {
                std::cout << "Drawing circle" << std::endl;
            } else if (dynamic_cast<Square*>(shape)) {
                std::cout << "Drawing square" << std::endl;
            } else if (dynamic_cast<Triangle*>(shape)) {
                std::cout << "Drawing triangle" << std::endl;
            }
        }
    };

    } // namespace graphics
    """
    model = CppAntlrParserAdapter().parse_sources({"ShapeDrawer.hpp": code})
    detections = OpenClosedPrincipleRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.OPEN_CLOSED
    assert "dynamic_cast" in detections[0].evidences[0].description


def test_lsp_unsupported_operation_violation() -> None:
    code = """
    #include <stdexcept>

    namespace collections {

    class IReadOnlyList {
    public:
        virtual ~IReadOnlyList() = default;
        virtual void get(int index) = 0;
        virtual void add(int item) = 0;
    };

    class ImmutableListImpl : public IReadOnlyList {
    public:
        void get(int index) override {}

        void add(int item) override {
            throw std::runtime_error("UnsupportedOperation: Immutable list cannot be modified");
        }
    };

    } // namespace collections
    """
    model = CppAntlrParserAdapter().parse_sources({"ImmutableListImpl.hpp": code})
    detections = LiskovSubstitutionRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.LISKOV_SUBSTITUTION


def test_isp_fat_interface_violation() -> None:
    code = """
    namespace worker {

    class IMonolithicWorker {
    public:
        virtual ~IMonolithicWorker() = default;
        virtual void code() = 0;
        virtual void test() = 0;
        virtual void deploy() = 0;
        virtual void manageInfrastructure() = 0;
        virtual void reviewBudget() = 0;
        virtual void designGraphics() = 0;
        virtual void recruitEmployees() = 0;
        virtual void handleCustomerSupport() = 0;
        virtual void cleanOffice() = 0;
    };

    } // namespace worker
    """
    model = CppAntlrParserAdapter().parse_sources({"MonolithicWorker.hpp": code})
    detections = InterfaceSegregationRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.INTERFACE_SEGREGATION


def test_dip_concrete_instantiation_violation() -> None:
    code = """
    #include <memory>

    namespace service {

    class OrderProcessingService {
    public:
        void processOrder() {
            auto repo = std::make_unique<MySqlDatabaseRepository>();
            repo->saveOrder();
        }
    };

    } // namespace service
    """
    model = CppAntlrParserAdapter().parse_sources({"OrderProcessingService.hpp": code})
    detections = DependencyInversionRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.DEPENDENCY_INVERSION


def test_composition_over_inheritance_deep_hierarchy() -> None:
    code = """
    namespace hierarchy {

    class BaseEntity {};
    class AuditableEntity : public BaseEntity {};
    class VersionedEntity : public AuditableEntity {};
    class ConcreteUserEntity : public VersionedEntity {};

    } // namespace hierarchy
    """
    model = CppAntlrParserAdapter().parse_sources({"Hierarchy.hpp": code})
    detections = CompositionOverInheritanceRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.COMPOSITION_OVER_INHERITANCE


def test_law_of_demeter_train_wreck_violation() -> None:
    code = """
    #include <iostream>
    #include <string>

    namespace shipping {

    class ShippingService {
    public:
        void calculateShipping(Order& order) {
            std::string zip = order.getCustomer().getAddress().getLocation().getPostalCode();
            std::cout << "Zip: " << zip << std::endl;
        }
    };

    } // namespace shipping
    """
    model = CppAntlrParserAdapter().parse_sources({"ShippingService.hpp": code})
    detections = LawOfDemeterRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.LAW_OF_DEMETER


def test_kiss_long_parameter_list_violation() -> None:
    code = """
    #include <iostream>
    #include <string>

    namespace complex {

    class ComplexCalculator {
    public:
        void computeMetrics(int a, int b, std::string name, double rate, bool flag, std::string mode, void* ctx) {
            std::cout << "Computing" << std::endl;
        }
    };

    } // namespace complex
    """
    model = CppAntlrParserAdapter().parse_sources({"ComplexCalculator.hpp": code})
    detections = KissRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.KISS


def test_dry_duplicate_code_violation() -> None:
    code_a = """
    namespace dups {

    class AlphaProcessor {
    public:
        double calculateStandardDiscount(double price, int count) {
            double base = price * count;
            if (base > 100.0) {
                return base * 0.85;
            }
            return base * 0.95;
        }
    };

    } // namespace dups
    """
    code_b = """
    namespace dups {

    class BetaProcessor {
    public:
        double computePartnerDiscount(double price, int count) {
            double base = price * count;
            if (base > 100.0) {
                return base * 0.85;
            }
            return base * 0.95;
        }
    };

    } // namespace dups
    """
    model = CppAntlrParserAdapter().parse_sources({
        "AlphaProcessor.hpp": code_a,
        "BetaProcessor.hpp": code_b,
    })
    detections = DryRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.DRY


def test_cohesion_coupling_high_fan_out() -> None:
    code_hub = """
    #include "Mod1.hpp"
    #include "Mod2.hpp"
    #include "Mod3.hpp"
    #include "Mod4.hpp"

    namespace hub {
    class GlobalOrchestrator {};
    }
    """
    model = CppAntlrParserAdapter().parse_sources({
        "GlobalOrchestrator.hpp": code_hub,
        "Mod1.hpp": "namespace mod1 { class Mod1 {}; }",
        "Mod2.hpp": "namespace mod2 { class Mod2 {}; }",
        "Mod3.hpp": "namespace mod3 { class Mod3 {}; }",
        "Mod4.hpp": "namespace mod4 { class Mod4 {}; }",
    })
    detections = CohesionCouplingRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.HIGH_COHESION_LOW_COUPLING
