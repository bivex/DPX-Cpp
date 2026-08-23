"""Unit tests for SOLID Principles, Clean Code, Coupling & Cohesion Rules."""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter
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
    package com.example.service;

    public class MegaGodManager {
        private String dbUrl;
        private String httpPort;
        private String jwtSecret;
        private String cacheHost;
        private int retryCount;
        private boolean isDev;
        private String logFile;

        public void saveToDatabase() {}
        public void deleteFromDatabase() {}
        public void queryDatabase() {}
        public void handleHttpRequest() {}
        public void getHttpEndpoint() {}
        public void serializeToJson() {}
        public void parseXml() {}
        public void authenticateUser() {}
        public void calculateTaxes() {}
        public void computeDiscounts() {}
        public void processOrder() {}
        public void validatePayment() {}
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"MegaGodManager.java": code})
    detections = SingleResponsibilityRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.SINGLE_RESPONSIBILITY
    assert detections[0].pattern_category == PatternCategory.PRINCIPLE


def test_ocp_instanceof_cascade_violation() -> None:
    code = """
    package com.example.graphics;

    public class ShapeDrawer {
        public void drawShape(Object shape) {
            if (shape instanceof Circle) {
                System.out.println("Drawing circle");
            } else if (shape instanceof Square) {
                System.out.println("Drawing square");
            } else if (shape instanceof Triangle) {
                System.out.println("Drawing triangle");
            }
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"ShapeDrawer.java": code})
    detections = OpenClosedPrincipleRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.OPEN_CLOSED
    assert "instanceof" in detections[0].evidences[0].description


def test_lsp_unsupported_operation_violation() -> None:
    code = """
    package com.example.collections;

    public interface ReadOnlyList {
        void get(int index);
        void add(Object item);
    }

    public class ImmutableListImpl implements ReadOnlyList {
        public void get(int index) {}

        public void add(Object item) {
            throw new UnsupportedOperationException("Immutable list cannot be modified");
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"ImmutableListImpl.java": code})
    detections = LiskovSubstitutionRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.LISKOV_SUBSTITUTION


def test_isp_fat_interface_violation() -> None:
    code = """
    package com.example.worker;

    public interface MonolithicWorker {
        void code();
        void test();
        void deploy();
        void manageInfrastructure();
        void reviewBudget();
        void designGraphics();
        void recruitEmployees();
        void handleCustomerSupport();
        void cleanOffice();
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"MonolithicWorker.java": code})
    detections = InterfaceSegregationRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.INTERFACE_SEGREGATION


def test_dip_concrete_instantiation_violation() -> None:
    code = """
    package com.example.service;

    public class OrderProcessingService {
        public void processOrder() {
            MySqlDatabaseRepository repo = new MySqlDatabaseRepository();
            repo.saveOrder();
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"OrderProcessingService.java": code})
    detections = DependencyInversionRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.DEPENDENCY_INVERSION


def test_composition_over_inheritance_deep_hierarchy() -> None:
    code = """
    package com.example.hierarchy;

    public class BaseEntity {}
    public class AuditableEntity extends BaseEntity {}
    public class VersionedEntity extends AuditableEntity {}
    public class ConcreteUserEntity extends VersionedEntity {}
    """
    model = JavaAntlrParserAdapter().parse_sources({"Hierarchy.java": code})
    detections = CompositionOverInheritanceRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.COMPOSITION_OVER_INHERITANCE


def test_law_of_demeter_train_wreck_violation() -> None:
    code = """
    package com.example.shipping;

    public class ShippingService {
        public void calculateShipping(Order order) {
            String zip = order.getCustomer().getAddress().getLocation().getPostalCode();
            System.out.println("Zip: " + zip);
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"ShippingService.java": code})
    detections = LawOfDemeterRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.LAW_OF_DEMETER


def test_kiss_long_parameter_list_violation() -> None:
    code = """
    package com.example.complex;

    public class ComplexCalculator {
        public void computeMetrics(int a, int b, String name, double rate, boolean flag, String mode, Object ctx) {
            System.out.println("Computing");
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({"ComplexCalculator.java": code})
    detections = KissRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.KISS


def test_dry_duplicate_code_violation() -> None:
    code_a = """
    package com.example.dups;

    public class AlphaProcessor {
        public double calculateStandardDiscount(double price, int count) {
            double base = price * count;
            if (base > 100.0) {
                return base * 0.85;
            }
            return base * 0.95;
        }
    }
    """
    code_b = """
    package com.example.dups;

    public class BetaProcessor {
        public double computePartnerDiscount(double price, int count) {
            double base = price * count;
            if (base > 100.0) {
                return base * 0.85;
            }
            return base * 0.95;
        }
    }
    """
    model = JavaAntlrParserAdapter().parse_sources({
        "AlphaProcessor.java": code_a,
        "BetaProcessor.java": code_b,
    })
    detections = DryRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.DRY


def test_cohesion_coupling_high_fan_out() -> None:
    code_hub = """
    package com.example.hub;

    import com.example.mod1.Mod1;
    import com.example.mod2.Mod2;
    import com.example.mod3.Mod3;
    import com.example.mod4.Mod4;

    public class GlobalOrchestrator {}
    """
    model = JavaAntlrParserAdapter().parse_sources({
        "GlobalOrchestrator.java": code_hub,
        "Mod1.java": "package com.example.mod1; public class Mod1 {}",
        "Mod2.java": "package com.example.mod2; public class Mod2 {}",
        "Mod3.java": "package com.example.mod3; public class Mod3 {}",
        "Mod4.java": "package com.example.mod4; public class Mod4 {}",
    })
    detections = CohesionCouplingRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.HIGH_COHESION_LOW_COUPLING

