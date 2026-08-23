# ☕ DPX-Java: Pattern Scanner & Software Architecture Analyzer for Java

> **Hexagonal Architecture (Ports & Adapters) + Domain-Driven Design (DDD)** static analysis and software design pattern detection engine for **Java (Java 8 / 11 / 17 / 21+)** powered by **ANTLR4** grammar parsing.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg?style=flat&logo=python)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-8%20--%2021%2B-orange.svg?style=flat&logo=java)](https://openjdk.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Hexagonal%20%2B%20DDD-brightgreen.svg?style=flat)]()
[![ANTLR](https://img.shields.io/badge/Parser-ANTLR%204.13.2-red.svg?style=flat)](https://www.antlr.org/)
[![Tests](https://img.shields.io/badge/Tests-39%20passed%20(100%25)-success.svg?style=flat)]()
[![Code Style](https://img.shields.io/badge/Linter-Ruff%20%26%20Mypy%20Strict-black.svg?style=flat)]()
[![Rules](https://img.shields.io/badge/Supported%20Rules-35%20(23%20GoF%20%2B%2010%20SOLID%2FPrinciples%20%2B%202%20Arch)-orange.svg?style=flat)]()

---

## 🏛 Architecture Overview

The system strictly follows **Domain-Driven Design (DDD)** and **Hexagonal Architecture (Ports & Adapters)**. The domain layer has **zero knowledge** of ANTLR, grammar tokens, AST implementation details, filesystem, or CLI frameworks.

```text
                    ┌────────────────────────────────────────────────────────┐
                    │                    Driving Adapters                    │
                    │                                                        │
                    │   Typer + Rich CLI         /       Python SDK API      │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │                   Application Layer                    │
                    │                                                        │
                    │     ScanningService (Pipeline Coordinator & Use Cases) │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                      ┌─────────▼─────────┐
                                      │    DOMAIN CORE    │
                                      │                   │
                                      │  CodeModel        │
                                      │  35 AnalysisRules │
                                      │  Confidence Model │
                                      │  Evidence Trail   │
                                      │  Dependency Graph │
                                      └─────────┬─────────┘
                                                │
                    ┌───────────────────────────▼────────────────────────────┐
                    │                      Ports / SPI                       │
                    │                                                        │
                    │   Inbound:  ScannerPort, DetectorPort, ScanOptions     │
                    │   Outbound: ParserPort, SourceProviderPort,            │
                    │             ResultRepositoryPort, ReportFormatterPort  │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                    ┌───────────────────────────▼────────────────────────────┐
                    │                    Driven Adapters                     │
                    │                                                        │
                    │   • ANTLR4 Java Parser (JavaLexer.g4 / JavaParser.g4)  │
                    │   • FileSystem Source Provider (.java recursive)       │
                    │   • Interactive HTML Dashboard Formatter & Repository  │
                    │   • GitHub-Flavored Markdown Formatter & Repository    │
                    │   • JSON Result Repository                             │
                    │   • Rich Console Terminal Formatter                    │
                    └────────────────────────────────────────────────────────┘
```

---

## 📐 Supported Rules Catalog (35 Rules)

### 1. SOLID & Clean Code Principles (10 Rules)
| # | Principle | Category | Detection Strategy & Heuristics |
|---|---|---|---|
| 1 | **Single Responsibility (SRP)** | Principle | Detects God Object anti-patterns mixing multiple disparate concerns (>10 methods, high field counts, combining DB + HTTP + business logic). |
| 2 | **Open/Closed (OCP)** | Principle | Identifies fragile `instanceof` / `switch(type)` cascades vs praises polymorphic interface extension points. |
| 3 | **Liskov Substitution (LSP)** | Principle | Detects derived classes breaking parent contracts (e.g. throwing `UnsupportedOperationException`). |
| 4 | **Interface Segregation (ISP)** | Principle | Flags Fat Interfaces (>8 methods) and praises fine-grained Role Interfaces (1-3 cohesive methods). |
| 5 | **Dependency Inversion (DIP)** | Principle | Verifies constructor/field interface injection vs hardcoded `new ConcreteClass()` instantiations. |
| 6 | **Composition Over Inheritance** | Principle | Flags deep inheritance trees (depth $\ge$ 3) and recommends composition/delegation. |
| 7 | **Law of Demeter (LoD)** | Principle | Detects train-wreck chained calls (`a.getB().getC().getD().run()`) causing tight structural coupling. |
| 8 | **High Cohesion & Low Coupling** | Principle | Evaluates package fan-out efferent coupling metrics to enforce modularity. |
| 9 | **Keep It Simple, Stupid (KISS)** | Principle | Detects high cyclomatic complexity and methods with long parameter lists ($\ge$ 6 parameters). |
| 10 | **Don't Repeat Yourself (DRY)** | Principle | Detects identical and near-duplicate non-trivial method bodies across classes. |

### 2. Gang of Four (GoF) Patterns (23 Rules)
| # | Pattern Type | Category | Detection Strategy & Java OOP Idioms |
|---|---|---|---|
| 11 | **Singleton** | Creational | `private static final ... INSTANCE = new ...();`, `getInstance()` accessor. |
| 12 | **Factory Method** | Creational | Factory creator classes or methods (`createButton`, `buildWidget`, `makeRequest`). |
| 13 | **Abstract Factory** | Creational | Factory interfaces (`GUIFactory`) declaring families of product creation methods. |
| 14 | **Builder** | Creational | Fluent step methods (`withHost`, `setPort`, `withSsl`) returning `this` / `Builder` and terminal `build()`. |
| 15 | **Prototype** | Creational | `implements Cloneable`, `clone()` methods, or copy constructors producing variants. |
| 16 | **Adapter** | Structural | Wrapper classes implementing a target interface and holding an adaptee reference. |
| 17 | **Decorator** | Structural | Classes implementing an interface and wrapping another instance of the same interface. |
| 18 | **Facade** | Structural | Service facade classes coordinating access to multiple subsystem dependencies. |
| 19 | **Composite** | Structural | Component interface implemented by Leaf elements and Composite container classes with `List<Component>`. |
| 20 | **Bridge** | Structural | Abstraction classes holding injected backend driver interfaces (`DatabaseDriver`). |
| 21 | **Proxy** | Structural | Surrogate classes controlling access / caching / logging, or dynamic proxies. |
| 22 | **Flyweight** | Structural | Object pools with `Map<Key, Value> cache` sharing fine-grained immutable instances. |
| 23 | **Observer** | Behavioral | Listener/Observer interfaces (`EventListener`), subscription methods, and event dispatching. |
| 24 | **Strategy** | Behavioral | Strategy interfaces with 2+ interchangeable concrete class implementations. |
| 25 | **Chain of Responsibility** | Behavioral | Handler pipelines with `setNext(Handler next)` / `next.handle(request)` delegation. |
| 26 | **Template Method** | Behavioral | Abstract classes with template execution methods delegating to abstract/protected step hooks. |
| 27 | **Command** | Behavioral | `Command` interface (`execute()`, `undo()`) with concrete command action classes. |
| 28 | **State** | Behavioral | State interface with concrete state classes and Context delegating state transitions. |
| 29 | **Iterator** | Behavioral | Custom classes implementing `java.util.Iterator<T>` or `java.lang.Iterable<T>`. |
| 30 | **Mediator** | Behavioral | Centralized mediator / event broker classes (`EventBroker`) decoupling components. |
| 31 | **Memento** | Behavioral | State snapshot classes (`Memento`) with `saveStateToMemento()` and `restoreState()`. |
| 32 | **Visitor** | Behavioral | Visitor interface with `visit(ElementA a)`, `visit(ElementB b)` and `Element.accept(Visitor v)`. |
| 33 | **Interpreter** | Behavioral | Grammar expression interfaces (`Expression`) with `interpret(Context ctx)`. |

### 3. Architectural Rules (2 Rules)
| # | Pattern Type | Category | Detection Strategy |
|---|---|---|---|
| 34 | **Lifecycle Component** | Architectural | Deterministic component lifecycles (`start()`, `stop()`). |
| 35 | **Circular Dependency** | Architectural | Package graph analysis detecting cyclic dependencies (`pkg A ➔ pkg B ➔ pkg A`). |

---

## 💻 CLI Usage Guide

```bash
# 1. Scan a Java project directory
uv run pattern-detector scan path/to/java/project

# 2. Export to interactive color-coded HTML dashboard
uv run pattern-detector scan path/to/java/project --html reports/dashboard.html
open reports/dashboard.html

# 3. Filter by confidence threshold or pattern
uv run pattern-detector scan path/to/java/project --min-confidence 0.70 --pattern srp

# 4. View registered rules catalog (all 35 rules)
uv run pattern-detector rules

# 5. Run test suite
uv run pytest -v
```

---

## 🧪 Quality & Verification

```bash
uv run pytest --cov=pattern_detector -v
uv run ruff check .
uv run mypy src/pattern_detector
```

* **Test Suite:** `39 / 39 PASSED` (100% pass rate).
* **Linter:** `ruff` (0 errors).
* **Static Typing:** strict `mypy` compliant.
