"""Tests for ANTLR Java Parser Adapter."""

from pattern_detector.adapters.outbound.antlr.java_parser_adapter import JavaAntlrParserAdapter


def test_parse_package_and_classes() -> None:
    code = """
    package com.example.service;

    import java.util.List;
    import java.util.Map;

    public class UserService {
        private String dbUrl;
        private static final UserService INSTANCE = new UserService();

        public void processUser(String id) {
            System.out.println("Processing: " + id);
        }
    }
    """
    adapter = JavaAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="UserService.java")

    assert ns.name == "com.example.service"
    assert len(ns.imports) == 2
    assert "UserService" in ns.records
    rec = ns.records["UserService"]
    assert "dbUrl" in rec.fields
    assert "INSTANCE" in rec.fields
    assert "INSTANCE" in ns.states
    assert ns.states["INSTANCE"].kind == "atom"
    assert ns.states["INSTANCE"].is_once is True


def test_parse_interfaces_and_implementations() -> None:
    code = """
    package com.example.repo;

    public interface CrudRepository {
        void save(Object entity);
        Object findById(String id);
    }

    public class DatabaseRepository implements CrudRepository {
        private String connectionString;

        public void save(Object entity) {
            System.out.println("Saving: " + entity);
        }

        public Object findById(String id) {
            return null;
        }
    }
    """
    adapter = JavaAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="DatabaseRepository.java")

    assert "CrudRepository" in ns.protocols
    proto = ns.protocols["CrudRepository"]
    assert len(proto.methods) == 2
    assert proto.has_method("save")
    assert proto.has_method("findById")

    assert "DatabaseRepository" in ns.records
    rec = ns.records["DatabaseRepository"]
    assert rec.implements_protocol("CrudRepository")
