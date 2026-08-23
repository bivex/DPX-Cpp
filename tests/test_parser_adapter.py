"""Tests for ANTLR C++ Parser Adapter."""

from pattern_detector.adapters.outbound.antlr.cpp_parser_adapter import CppAntlrParserAdapter


def test_parse_namespace_and_classes() -> None:
    code = """
    #include <string>
    #include <iostream>

    namespace service {

    class UserService {
    private:
        std::string dbUrl;
    public:
        static UserService& getInstance() {
            static UserService instance;
            return instance;
        }

        void processUser(const std::string& id) {
            std::cout << "Processing: " << id << std::endl;
        }
    };

    } // namespace service
    """
    adapter = CppAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="UserService.hpp")

    assert ns.name == "service"
    assert len(ns.imports) == 2
    assert "UserService" in ns.records
    rec = ns.records["UserService"]
    assert rec.name == "UserService"
    assert "UserService::instance" in ns.states
    assert ns.states["UserService::instance"].kind == "atom"
    assert ns.states["UserService::instance"].is_once is True


def test_parse_interfaces_and_implementations() -> None:
    code = """
    #include <string>
    #include <iostream>

    namespace repo {

    class ICrudRepository {
    public:
        virtual ~ICrudRepository() = default;
        virtual void save(const std::string& entity) = 0;
        virtual std::string findById(const std::string& id) = 0;
    };

    class DatabaseRepository : public ICrudRepository {
    public:
        void save(const std::string& entity) override {
            std::cout << "Saving: " << entity << std::endl;
        }

        std::string findById(const std::string& id) override {
            return "";
        }
    };

    } // namespace repo
    """
    adapter = CppAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="DatabaseRepository.hpp")

    assert "ICrudRepository" in ns.protocols
    proto = ns.protocols["ICrudRepository"]
    assert len(proto.methods) == 2
    assert proto.has_method("save")
    assert proto.has_method("findById")

    assert "DatabaseRepository" in ns.records
    rec = ns.records["DatabaseRepository"]
    assert rec.implements_protocol("ICrudRepository")
