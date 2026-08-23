# ⚡ DPX-Cpp: Pattern Scanner & Software Architecture Analyzer for C++

> **Hexagonal Architecture (Ports & Adapters) + Domain-Driven Design (DDD)** static analysis and software design pattern detection engine for **C++ (C++14 / 17 / 20 / 23)** powered by **ANTLR4** grammar parsing.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg?style=flat&logo=python)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C%2B%2B-14%20%2F%2017%20%2F%2020%20%2F%2023-blue.svg?style=flat&logo=cplusplus)](https://en.cppreference.com/)
[![Architecture](https://img.shields.io/badge/Architecture-Hexagonal%20%2B%20DDD-brightgreen.svg?style=flat)]()
[![ANTLR](https://img.shields.io/badge/Parser-ANTLR%204.13.2-red.svg?style=flat)](https://www.antlr.org/)
[![Tests](https://img.shields.io/badge/Tests-43%20passed%20(100%25)-success.svg?style=flat)]()
[![Code Style](https://img.shields.io/badge/Linter-Ruff%20%26%20Mypy%20Strict-black.svg?style=flat)]()
[![Rules](https://img.shields.io/badge/Supported%20Rules-35%20(23%20GoF%20%2B%2010%20SOLID%2FPrinciples%20%2B%202%20Arch)-orange.svg?style=flat)]()
[![Template](https://img.shields.io/badge/GitHub-Template%20Repository-purple.svg?style=flat)]()

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
                    │   • ANTLR4 C++ Parser (CPP14Lexer.g4 / CPP14Parser.g4) │
                    │   • Fast Brace-Balanced Macro-Tolerant AST Parser      │
                    │   • FileSystem Source Provider (.cpp, .hpp recursive)  │
                    │   • Interactive HTML Dashboard Formatter & Repository  │
                    │   • GitHub-Flavored Markdown Formatter & Repository    │
                    │   • JSON Result Repository                             │
                    │   • Rich Console Terminal Formatter                    │
                    └────────────────────────────────────────────────────────┘
```

---

## 📐 Catalog of 35 Supported Rules & Principles

DPX-Cpp analyzes C++ codebases across **5 major categories**:

### 1. 🏗 Creational Patterns (GoF)
1. **Singleton**: Meyers' Singleton (`static T& getInstance() { static T inst; return inst; }`), deleted copy/move constructors, private constructors, static instance fields.
2. **Factory Method**: Virtual factory methods returning `std::unique_ptr<Product>` or `std::shared_ptr<Product>`.
3. **Abstract Factory**: Factory interfaces declaring multiple product creation families.
4. **Builder**: Method chaining / fluent builders returning references (`Builder&`).
5. **Prototype**: Classes declaring `clone()` / copy-creation returning `std::unique_ptr<Base>`.

### 2. 🏛 Structural Patterns (GoF)
6. **Adapter**: Object / Class adapters delegating to wrapped instances.
7. **Bridge / PIMPL Idiom**: Decoupled abstraction & implementation, Pointer to Implementation (`std::unique_ptr<Impl> pImpl`).
8. **Composite**: Tree structures aggregating `std::vector<std::shared_ptr<Component>>`.
9. **Decorator**: Wrapping same abstract base class / interface and delegating.
10. **Facade**: High-level unified interfaces coordinating multiple sub-systems.
11. **Flyweight**: Factory managing shared intrinsic object pools / flyweights.
12. **Proxy**: Intermediary objects controlling access / lazy-initialization to real subjects.

### 3. 🎯 Behavioral Patterns (GoF)
13. **Chain of Responsibility**: Handler chains with `next` pointers / smart pointers.
14. **Command**: Command objects encapsulating `execute()` / `undo()`.
15. **Interpreter**: Grammar expression hierarchies (`Expression` with `interpret()`).
16. **Iterator**: Custom iterator implementations (`hasNext()`, `next()`, `operator++`).
17. **Mediator**: Central event brokers / dispatchers decoupling components.
18. **Memento**: Snapshot & state rollback managers (`createMemento()`, `restore()`).
19. **Observer**: Subject maintaining subscriber lists (`std::vector<std::weak_ptr<IObserver>>`).
20. **State**: Polymorphic state machines delegating behavior to current state object.
21. **Strategy**: Interchangeable algorithmic strategies (`IStrategy` with concrete subclasses).
22. **Template Method**: Base class skeleton algorithm calling virtual / pure-virtual step primitives.
23. **Visitor**: Double-dispatch visitor (`Visitor` interface with overloaded `visit()` + `Element.accept(Visitor& v)`).

### 4. 💎 SOLID & Clean Code Principles
24. **Single Responsibility (SRP)**: God Object detector filtering out standard DTO getters/setters.
25. **Open/Closed (OCP)**: Detects fragile `dynamic_cast<T*>` and `typeid` cascades vs extensible polymorphic hierarchies.
26. **Liskov Substitution (LSP)**: Detects overridden methods throwing `std::runtime_error("unsupported")` or breaking parent contracts.
27. **Interface Segregation (ISP)**: Fat Abstract Classes (>8 pure virtual methods) vs Focused Role Interfaces (1-3 pure virtual methods).
28. **Dependency Inversion (DIP)**: Flags hardcoded `std::make_unique<ConcreteClass>()` / `new ConcreteClass()` in business services vs injected interface pointers/references.
29. **Composition over Inheritance**: Deep inheritance tree analyzer (flags hierarchies with depth $\ge 3$).
30. **Law of Demeter (LoD)**: Train-wreck call detector (`a->getB()->getC()->doSomething()`) with built-in exclusions for `std::ranges`, `std::string`, `std::optional`, and fluent builders.
31. **High Cohesion & Low Coupling**: Efferent coupling (Fan-Out) metric analyzing cross-namespace `#include` dependencies.
32. **Keep It Simple, Stupid (KISS)**: Long parameter lists ($\ge 6$) and high cyclomatic branching complexity.
33. **Don't Repeat Yourself (DRY)**: Structural cross-method duplicate code logic detector.

### 5. 🔄 Architectural & System Patterns
34. **Lifecycle Component**: RAII lifecycle management (`~Destructor()`, `start()`, `stop()`, `init()`, `shutdown()`).
35. **Circular Dependency**: Tarjan/DFS topological cycle detector identifying circular `#include` / namespace dependencies.

---

## 🛡️ False-Positive Prevention & Precision

DPX-Cpp implements specialized heuristic filters for modern idiomatic C++:

* **DTO / POD Struct Whitelist:** Classes with getters/setters (`get*`, `set*`, `is*`, `has*`) are never misidentified as SRP God Objects.
* **Standard Operators Excluded:** `operator==`, `operator!=`, `operator<` comparing members are ignored by OCP cascades.
* **STL & Fluent API Excluded from LoD:** `std::string`, `std::optional`, `std::ranges`, `std::vector`, and fluent builders do not trigger Law of Demeter violations.
* **Container Exemption in DIP:** Instantiations of STL containers (`std::vector`, `std::map`) and value objects are whitelisted.
* **Trivial Forwarder Filtering in DRY:** 1-line getters, return statements, and default forwards are ignored by duplication detection.

---

## 🚀 Real-World Benchmarks

| Project / Repository | Files | Scan Duration | Identified Patterns & Principles |
| :--- | :---: | :---: | :--- |
| **[`JakubVojvoda/design-patterns-cpp`](https://github.com/JakubVojvoda/design-patterns-cpp)** | 24 | **6.21 s** | Abstract Factory, Composite, Observer, Strategy, Singleton, Chain of Resp., Flyweight, ISP Role Interfaces |
| **[`gabime/spdlog`](https://github.com/gabime/spdlog) (`spdlog/sinks`)** | 28 | **0.058 s** | DIP Injected Abstractions, RAII Lifecycle, Cross-Namespace Cycles (`global ⇄ sinks`), SRP Metrics |

---

## ⚡ Quick Start

### Installation with `uv`
```bash
# Clone the repository
git clone https://github.com/bivex/DPX-Cpp.git
cd DPX-Cpp

# Install dependencies and sync virtual environment
uv sync
```

### CLI Usage

```bash
# 1. Scan a C++ codebase or header/source directory
uv run pattern-detector scan path/to/cpp/project

# 2. Generate an Interactive Dark-Mode HTML Dashboard
uv run pattern-detector scan path/to/cpp/project --html reports/cpp_patterns_dashboard.html

# 3. Export GitHub-Flavored Markdown Report
uv run pattern-detector scan path/to/cpp/project --markdown reports/report.md

# 4. Filter by specific pattern types with confidence threshold
uv run pattern-detector scan path/to/cpp/project -p strategy -p singleton -c 0.75

# 5. List all 35 catalog rules
uv run pattern-detector rules

# 6. Display Hexagonal DDD Architecture info
uv run pattern-detector info
```

---

## 💻 Python SDK API Usage

You can also integrate DPX-Cpp programmatically into CI/CD pipelines or Python tools:

```python
from pattern_detector.bootstrap.container import create_container
from pattern_detector.ports.inbound import ScanOptions

container = create_container()
scanner = container.get_scanner()

options = ScanOptions(
    min_confidence=0.70,
    output_html_path="reports/dashboard.html",
    output_json_path="reports/report.json",
)

report = scanner.scan_path("path/to/cpp/project", options=options)
print(f"Scanned {report.scanned_files_count} files, found {report.total_detections_count} patterns.")
```

---

## 📊 Interactive HTML Dashboard

DPX-Cpp exports a standalone, dark-themed HTML report featuring:
- **Metrics Bar**: Total detections, confidence levels (Very High, High, Medium, Low).
- **Category Filter Pills**: CREATIONAL, STRUCTURAL, BEHAVIORAL, PRINCIPLE, ARCHITECTURAL.
- **Search & Filter**: Real-time filtering by class name, file path, or pattern keyword.
- **Evidence Trail**: Heuristic scores, explanations, and exact source code file:line navigation.

---

## 🧪 Testing & Code Quality

```bash
# Run 100% full test suite with coverage (43 tests)
uv run pytest --cov=pattern_detector -v

# Run Ruff linter and code formatter
uv run ruff check .

# Run Strict Mypy type checker
uv run mypy src/pattern_detector
```

---

## 📄 License
MIT License. Developed for advanced static code analysis and architecture verification.
