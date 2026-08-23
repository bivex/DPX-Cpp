"""Comprehensive False Positives Test Suite for DPX-Java.

Verifies that ordinary, standard Java idioms (POJOs, DTOs, JPA Entities, Stream API,
Optional pipelines, standard equals/hashCode, collections, and pure utility functions)
do not produce false positive detections for Design Patterns or SOLID Principle violations.
"""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternType


def _scan_snippet(code_map: dict[str, str]):
    adapter = JavaAntlrParserAdapter()
    model = adapter.parse_sources(code_map)
    detector = PatternDetectorService(rules=get_default_rules())
    return detector.detect_all(model)


def test_plain_pure_math_and_string_utilities_have_zero_detections() -> None:
    code = """
    package com.example.utils;

    public class MathUtils {
        public static int add(int a, int b) {
            return a + b;
        }

        public static int multiply(int x, int y) {
            return x * y;
        }

        public static long factorial(int n) {
            if (n <= 1) return 1;
            return n * factorial(n - 1);
        }
    }
    """
    report = _scan_snippet({"MathUtils.java": code})
    # Pure standard utilities must not trigger any design patterns or violations
    assert report.total_detections_count == 0


def test_dto_with_many_getters_and_setters_not_flagged_as_srp_god_object() -> None:
    code = """
    package com.example.dto;

    public class CustomerProfileDto {
        private String id;
        private String firstName;
        private String lastName;
        private String email;
        private String phoneNumber;
        private String streetAddress;
        private String city;
        private String postalCode;
        private String country;
        private String status;

        public String getId() { return id; }
        public void setId(String id) { this.id = id; }
        public String getFirstName() { return firstName; }
        public void setFirstName(String firstName) { this.firstName = firstName; }
        public String getLastName() { return lastName; }
        public void setLastName(String lastName) { this.lastName = lastName; }
        public String getEmail() { return email; }
        public void setEmail(String email) { this.email = email; }
        public String getPhoneNumber() { return phoneNumber; }
        public void setPhoneNumber(String phoneNumber) { this.phoneNumber = phoneNumber; }
        public String getStreetAddress() { return streetAddress; }
        public void setStreetAddress(String streetAddress) { this.streetAddress = streetAddress; }
        public String getCity() { return city; }
        public void setCity(String city) { this.city = city; }
        public String getPostalCode() { return postalCode; }
        public void setPostalCode(String postalCode) { this.postalCode = postalCode; }
        public String getCountry() { return country; }
        public void setCountry(String country) { this.country = country; }
        public String getStatus() { return status; }
        public void setStatus(String status) { this.status = status; }
    }
    """
    report = _scan_snippet({"CustomerProfileDto.java": code})
    srp_detections = [d for d in report.detections if d.pattern_type == PatternType.SINGLE_RESPONSIBILITY]
    assert len(srp_detections) == 0


def test_standard_equals_method_with_instanceof_not_flagged_as_ocp_violation() -> None:
    code = """
    package com.example.domain;

    public class MoneyValue {
        private final double amount;
        private final String currency;

        public MoneyValue(double amount, String currency) {
            this.amount = amount;
            this.currency = currency;
        }

        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null) return false;
            if (!(obj instanceof MoneyValue)) return false;
            MoneyValue other = (MoneyValue) obj;
            return this.amount == other.amount && this.currency.equals(other.currency);
        }

        public int hashCode() {
            return Double.hashCode(amount) ^ currency.hashCode();
        }
    }
    """
    report = _scan_snippet({"MoneyValue.java": code})
    ocp_detections = [d for d in report.detections if d.pattern_type == PatternType.OPEN_CLOSED]
    assert len(ocp_detections) == 0


def test_fluent_java_stream_and_optional_chains_not_flagged_as_law_of_demeter() -> None:
    code = """
    package com.example.service;

    import java.util.List;
    import java.util.Optional;
    import java.util.stream.Collectors;

    public class DataAggregationService {
        public List<String> processNames(List<String> rawNames) {
            return rawNames.stream()
                .filter(name -> name != null)
                .map(name -> name.trim())
                .map(name -> name.toUpperCase())
                .collect(Collectors.toList());
        }

        public String findSafeUserEmail(Optional<String> optionalEmail) {
            return optionalEmail
                .map(email -> email.toLowerCase())
                .map(email -> email.strip())
                .orElse("guest@example.com");
        }
    }
    """
    report = _scan_snippet({"DataAggregationService.java": code})
    lod_detections = [d for d in report.detections if d.pattern_type == PatternType.LAW_OF_DEMETER]
    assert len(lod_detections) == 0


def test_service_instantiating_arraylist_or_dto_not_flagged_as_dip_violation() -> None:
    code = """
    package com.example.service;

    import java.util.ArrayList;
    import java.util.List;

    public class ItemListingService {
        public List<String> generateSummary() {
            List<String> result = new ArrayList<>();
            result.add("Item A");
            result.add("Item B");
            return result;
        }
    }
    """
    report = _scan_snippet({"ItemListingService.java": code})
    dip_detections = [d for d in report.detections if d.pattern_type == PatternType.DEPENDENCY_INVERSION]
    assert len(dip_detections) == 0


def test_simple_record_getters_not_flagged_as_dry_duplicate_code() -> None:
    code_a = """
    package com.example.models;

    public class UserEntity {
        private String id;
        public String getId() { return this.id; }
    }
    """
    code_b = """
    package com.example.models;

    public class ProductEntity {
        private String id;
        public String getId() { return this.id; }
    }
    """
    report = _scan_snippet({
        "UserEntity.java": code_a,
        "ProductEntity.java": code_b,
    })
    dry_detections = [d for d in report.detections if d.pattern_type == PatternType.DRY]
    assert len(dry_detections) == 0


def test_string_helpers_with_make_or_create_name_not_flagged_as_factory() -> None:
    code = """
    package com.example.helpers;

    public class StringHelpers {
        public static String makeUppercase(String s) {
            return s.toUpperCase();
        }

        public static String createSlug(String title) {
            return title.toLowerCase().replace(" ", "-");
        }
    }
    """
    report = _scan_snippet({"StringHelpers.java": code})
    factory_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.FACTORY_METHOD and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(factory_detections) == 0
