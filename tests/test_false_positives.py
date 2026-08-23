"""Comprehensive False Positives Test Suite for DPX-Cpp.

Verifies that ordinary, standard C++ idioms (structs, DTOs, std::ranges / std::string,
std::optional pipelines, standard operator==, STL containers, and pure utility functions)
do not produce false positive detections for Design Patterns or SOLID Principle violations.
"""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternType


def _scan_snippet(code_map: dict[str, str]):
    adapter = CppAntlrParserAdapter()
    model = adapter.parse_sources(code_map)
    detector = PatternDetectorService(rules=get_default_rules())
    return detector.detect_all(model)


def test_plain_pure_math_and_string_utilities_have_zero_detections() -> None:
    code = """
    namespace utils {

    class MathUtils {
    public:
        static int add(int a, int b) {
            return a + b;
        }

        static int multiply(int x, int y) {
            return x * y;
        }

        static long factorial(int n) {
            if (n <= 1) return 1;
            return n * factorial(n - 1);
        }
    };

    } // namespace utils
    """
    report = _scan_snippet({"MathUtils.hpp": code})
    # Pure standard utilities must not trigger any design patterns or violations
    assert report.total_detections_count == 0


def test_dto_with_many_getters_and_setters_not_flagged_as_srp_god_object() -> None:
    code = """
    #include <string>

    namespace dto {

    class CustomerProfileDto {
    private:
        std::string id;
        std::string firstName;
        std::string lastName;
        std::string email;
        std::string phoneNumber;
        std::string streetAddress;
        std::string city;
        std::string postalCode;
        std::string country;
        std::string status;

    public:
        std::string getId() const { return id; }
        void setId(const std::string& val) { id = val; }
        std::string getFirstName() const { return firstName; }
        void setFirstName(const std::string& val) { firstName = val; }
        std::string getLastName() const { return lastName; }
        void setLastName(const std::string& val) { lastName = val; }
        std::string getEmail() const { return email; }
        void setEmail(const std::string& val) { email = val; }
        std::string getPhoneNumber() const { return phoneNumber; }
        void setPhoneNumber(const std::string& val) { phoneNumber = val; }
        std::string getStreetAddress() const { return streetAddress; }
        void setStreetAddress(const std::string& val) { streetAddress = val; }
        std::string getCity() const { return city; }
        void setCity(const std::string& val) { city = val; }
        std::string getPostalCode() const { return postalCode; }
        void setPostalCode(const std::string& val) { postalCode = val; }
        std::string getCountry() const { return country; }
        void setCountry(const std::string& val) { country = val; }
        std::string getStatus() const { return status; }
        void setStatus(const std::string& val) { status = val; }
    };

    } // namespace dto
    """
    report = _scan_snippet({"CustomerProfileDto.hpp": code})
    srp_detections = [d for d in report.detections if d.pattern_type == PatternType.SINGLE_RESPONSIBILITY]
    assert len(srp_detections) == 0


def test_standard_operator_equals_not_flagged_as_ocp_violation() -> None:
    code = """
    #include <string>

    namespace domain {

    class MoneyValue {
    private:
        double amount;
        std::string currency;

    public:
        MoneyValue(double amount, std::string currency)
            : amount(amount), currency(std::move(currency)) {}

        bool operator==(const MoneyValue& other) const {
            return amount == other.amount && currency == other.currency;
        }

        bool operator!=(const MoneyValue& other) const {
            return !(*this == other);
        }
    };

    } // namespace domain
    """
    report = _scan_snippet({"MoneyValue.hpp": code})
    ocp_detections = [d for d in report.detections if d.pattern_type == PatternType.OPEN_CLOSED]
    assert len(ocp_detections) == 0


def test_fluent_std_string_chains_not_flagged_as_law_of_demeter() -> None:
    code = """
    #include <string>
    #include <vector>
    #include <optional>

    namespace service {

    class DataAggregationService {
    public:
        std::string findSafeUserEmail(const std::optional<std::string>& optionalEmail) {
            if (optionalEmail.has_value()) {
                std::string email = optionalEmail.value();
                return email;
            }
            return "guest@example.com";
        }
    };

    } // namespace service
    """
    report = _scan_snippet({"DataAggregationService.hpp": code})
    lod_detections = [d for d in report.detections if d.pattern_type == PatternType.LAW_OF_DEMETER]
    assert len(lod_detections) == 0


def test_service_instantiating_vector_or_dto_not_flagged_as_dip_violation() -> None:
    code = """
    #include <vector>
    #include <string>

    namespace service {

    class ItemListingService {
    public:
        std::vector<std::string> generateSummary() {
            std::vector<std::string> result;
            result.push_back("Item A");
            result.push_back("Item B");
            return result;
        }
    };

    } // namespace service
    """
    report = _scan_snippet({"ItemListingService.hpp": code})
    dip_detections = [d for d in report.detections if d.pattern_type == PatternType.DEPENDENCY_INVERSION]
    assert len(dip_detections) == 0


def test_simple_record_getters_not_flagged_as_dry_duplicate_code() -> None:
    code_a = """
    #include <string>

    namespace models {

    class UserEntity {
    private:
        std::string id;
    public:
        std::string getId() const { return id; }
    };

    } // namespace models
    """
    code_b = """
    #include <string>

    namespace models {

    class ProductEntity {
    private:
        std::string id;
    public:
        std::string getId() const { return id; }
    };

    } // namespace models
    """
    report = _scan_snippet({
        "UserEntity.hpp": code_a,
        "ProductEntity.hpp": code_b,
    })
    dry_detections = [d for d in report.detections if d.pattern_type == PatternType.DRY]
    assert len(dry_detections) == 0


def test_string_helpers_with_make_or_create_name_not_flagged_as_factory() -> None:
    code = """
    #include <string>

    namespace helpers {

    class StringHelpers {
    public:
        static std::string makeUppercase(const std::string& s) {
            std::string res = s;
            for (auto& c : res) c = toupper(c);
            return res;
        }

        static std::string createSlug(const std::string& title) {
            return title;
        }
    };

    } // namespace helpers
    """
    report = _scan_snippet({"StringHelpers.hpp": code})
    factory_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.FACTORY_METHOD and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(factory_detections) == 0
