# ⚡ DPX-Cpp Architecture & Data Flow Viewer

Desktop GUI visualizer for **DPX-Cpp (Design Pattern Scanner & SciTools Understand Parity Data Flow Engine)**.
Built with **Tauri 2.0 + React 19 + TypeScript + Cytoscape.js**, organized strictly around **Hexagonal Architecture (Ports & Adapters) + Domain-Driven Design (DDD)**.

---

## 🏛 Hexagonal DDD Architecture

The viewer frontend and backend strictly isolate domain business rules, graphs, and evidence trails from framework specifics, Cytoscape.js rendering engines, and Tauri IPC bindings.

```text
viewer/src/
├── domain/                               # DOMAIN LAYER (Zero external UI/framework dependencies)
│   ├── models/                           # Entities & Aggregates
│   │   ├── architecture-graph.ts         # Graph with nodes & edges
│   │   ├── pattern-detection.ts          # Pattern detection result aggregate
│   │   └── data-flow.ts                  # Def-Use forward/backward graphs & matrix summary
│   ├── value-objects/                    # Value Objects
│   │   └── types.ts                      # ConfidenceLevel, NodeKind, EdgeKind, CodeLocation
│   └── services/                         # Domain Services
│       ├── graph-transformer.service.ts  # Transforms domain DTOs into ArchitectureGraph
│       └── graph-filter.service.ts       # Pure domain graph filtering & slicing
│
├── ports/                                # PORTS / INTERFACES LAYER
│   ├── inbound/                          # Primary / Driving Ports (Use Cases)
│   │   └── use-cases.ts                  # ScanCodebaseUseCase, TraceDataFlowUseCase, FilterGraphUseCase, ReadSourceCodeUseCase
│   └── outbound/                         # Secondary / Driven Ports (SPI)
│       ├── analyzer.port.ts              # AnalyzerPort (CLI engine bridge)
│       ├── source-provider.port.ts       # SourceProviderPort (file reader)
│       └── graph-renderer.port.ts        # GraphRendererPort (Cytoscape contract)
│
├── application/                          # APPLICATION LAYER (Coordinates Use Cases & State)
│   ├── services/
│   │   ├── scan.service.ts               # Coordinates codebase scanning
│   │   ├── data-flow.service.ts          # Coordinates forward/backward propagation tracing
│   │   ├── filter.service.ts             # Coordinates graph filtering
│   │   └── source-code.service.ts        # Coordinates source file loading
│   └── state/
│       └── viewer-context.tsx            # Global reactive context & hooks
│
├── adapters/                             # ADAPTERS LAYER
│   ├── driven/                           # Outbound Adapters (External systems & libraries)
│   │   ├── tauri/
│   │   │   ├── tauri-analyzer.adapter.ts # Tauri IPC invoking Rust `scan_project`, `trace_dataflow_*`
│   │   │   └── tauri-source.adapter.ts   # Tauri IPC invoking Rust `read_source_file`
│   │   ├── mock/                         # Fallback mock adapters for standalone browser preview
│   │   │   ├── sample-data.ts
│   │   │   ├── mock-analyzer.adapter.ts
│   │   │   └── mock-source.adapter.ts
│   │   └── cytoscape/                    # Cytoscape.js driven adapter
│   │       ├── cytoscape-graph.adapter.ts# Implements GraphRendererPort (Dagre, CoSE, Concentric)
│   │       └── cytoscape-theme.ts        # Modern dark theme styles
│   └── driving/                          # Inbound Adapters (UI Presentation)
│       └── components/
│           ├── HeaderBar.tsx             # Scan trigger, project path input, view switcher
│           ├── Sidebar.tsx               # Detections list, dataflow matrix, filters, search
│           ├── CytoscapeCanvas.tsx       # Interactive graph canvas & controls
│           └── InspectorPanel.tsx        # Node inspector, evidence trail, C++ code preview
│
└── bootstrap/                            # COMPOSITION ROOT / DI CONTAINER
    └── container.ts                      # Wires adapters to ports and initializes services
```

---

## 🚀 Running the Viewer

### Prerequisites
- Node.js (v20+) & `pnpm`
- Rust & Cargo (1.80+)
- Python 3.11+ with `uv` (for running the underlying `pattern-detector` engine)

### 1. Browser Development Mode (with mock data & full UI)
To develop or inspect the UI directly in your browser:
```bash
cd viewer
pnpm dev
```
Open [http://localhost:1420](http://localhost:1420) in your browser. When running without Tauri runtime, the app seamlessly activates the mock adapter with full interactive sample data.

### 2. Desktop Mode (Tauri 2.0 with native DPX-Cpp Python bridge)
To launch the native desktop window connected to `pattern-detector`:
```bash
cd viewer
pnpm tauri dev
```

### 3. Production Build
```bash
cd viewer
pnpm build
pnpm tauri build
```

---

## 🛠 Key Features

1. **Design Patterns & SOLID Hierarchy**:
   - Visualizes detected patterns grouped by category clusters (*Creational, Structural, Behavioral, Principle*).
   - Real-time search and confidence threshold filtering.
2. **SciTools Understand-Parity Data Flow Graph**:
   - Forward propagation (**Data Flow Out**) and backward slicing (**Data Flow In**).
   - Def-Use edges (*READS, WRITES, MODIFIES*).
   - Multi-algorithm layout switching: **Dagre** (Hierarchical DAG), **CoSE** (Physics / Force-directed), **Breadthfirst**, **Concentric**.
3. **Inspector & Code Preview**:
   - Clicking any node reveals its evidence trail, heuristics, confidence weights, and loads the target C++ source file with target line highlighting.
   - 1-click **Export as PNG** of high-resolution architecture diagrams.
