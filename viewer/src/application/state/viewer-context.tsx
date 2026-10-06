import React, { createContext, useContext, useEffect, useState } from 'react';
import { container } from '../../bootstrap/container';
import { ArchitectureGraph, GraphNode } from '../../domain/models/architecture-graph';
import { DataFlowSummary } from '../../domain/models/data-flow';
import { Detection, DetectionReport } from '../../domain/models/pattern-detection';
import { GraphLayoutAlgorithm } from '../../ports/outbound/graph-renderer.port';

export interface ViewerContextType {
  currentView: 'patterns' | 'dataflow';
  projectPath: string;
  setProjectPath: (p: string) => void;
  isLoading: boolean;
  error: string | null;

  // Patterns State
  report: DetectionReport | null;
  selectedDetection: Detection | null;

  // DataFlow State
  dataFlowSummary: DataFlowSummary | null;
  activeVariable: string | null;
  dataFlowDirection: 'out' | 'in';

  // Graph & Inspector State
  activeGraph: ArchitectureGraph | null;
  filteredGraph: ArchitectureGraph | null;
  selectedNodeId: string | null;
  selectedNode: GraphNode | null;
  sourceCode: string | null;

  // Filters & Layout
  searchQuery: string;
  setSearchQuery: (q: string) => void;
  selectedCategory: string | null;
  setSelectedCategory: (cat: string | null) => void;
  minConfidence: number;
  setMinConfidence: (val: number) => void;
  layoutAlgorithm: GraphLayoutAlgorithm;
  setLayoutAlgorithm: (algo: GraphLayoutAlgorithm) => void;

  // Methods
  scan: (path?: string) => Promise<void>;
  loadDataFlow: (path?: string) => Promise<void>;
  traceVariable: (variable: string, direction?: 'out' | 'in') => Promise<void>;
  selectNode: (nodeId: string | null) => Promise<void>;
  switchView: (view: 'patterns' | 'dataflow') => void;
}

const ViewerContext = createContext<ViewerContextType | null>(null);

export const ViewerProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [currentView, setCurrentView] = useState<'patterns' | 'dataflow'>('patterns');
  const [projectPath, setProjectPath] = useState<string>('examples/cpp_samples');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const [report, setReport] = useState<DetectionReport | null>(null);
  const [selectedDetection, setSelectedDetection] = useState<Detection | null>(null);

  const [dataFlowSummary, setDataFlowSummary] = useState<DataFlowSummary | null>(null);
  const [activeVariable, setActiveVariable] = useState<string | null>(null);
  const [dataFlowDirection, setDataFlowDirection] = useState<'out' | 'in'>('out');

  const [activeGraph, setActiveGraph] = useState<ArchitectureGraph | null>(null);
  const [filteredGraph, setFilteredGraph] = useState<ArchitectureGraph | null>(null);
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null);
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [sourceCode, setSourceCode] = useState<string | null>(null);

  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [minConfidence, setMinConfidence] = useState<number>(0.0);
  const [layoutAlgorithm, setLayoutAlgorithm] = useState<GraphLayoutAlgorithm>('dagre');

  // Trigger scan
  const scan = async (path?: string) => {
    const targetPath = path || projectPath;
    setIsLoading(true);
    setError(null);
    try {
      const res = await container.scanService.execute(targetPath, minConfidence);
      setReport(res.report);
      setActiveGraph(res.graph);
      setCurrentView('patterns');
      setSelectedNodeId(null);
      setSelectedNode(null);
      setSelectedDetection(null);
      setSourceCode(null);
    } catch (err: any) {
      setError(err?.message || String(err));
    } finally {
      setIsLoading(false);
    }
  };

  // Load Data Flow summary matrix
  const loadDataFlow = async (path?: string) => {
    const targetPath = path || projectPath;
    setIsLoading(true);
    setError(null);
    try {
      const summary = await container.dataFlowService.executeSummary(targetPath);
      setDataFlowSummary(summary);
      setCurrentView('dataflow');
      // If there are variables, trace the first high-impact one by default
      if (summary.summary.length > 0) {
        await traceVariable(summary.summary[0].variableName, 'out');
      }
    } catch (err: any) {
      setError(err?.message || String(err));
    } finally {
      setIsLoading(false);
    }
  };

  // Trace forward / backward data flow for a target variable
  const traceVariable = async (variable: string, direction: 'out' | 'in' = 'out') => {
    setIsLoading(true);
    setError(null);
    setActiveVariable(variable);
    setDataFlowDirection(direction);
    try {
      const res = await container.dataFlowService.executeTarget(
        projectPath,
        variable,
        direction,
        'simplified'
      );
      setActiveGraph(res.graph);
      setSelectedNodeId(null);
      setSelectedNode(null);
      setSourceCode(null);
    } catch (err: any) {
      setError(err?.message || String(err));
    } finally {
      setIsLoading(false);
    }
  };

  // Select node and load its source snippet if available
  const selectNode = async (nodeId: string | null) => {
    setSelectedNodeId(nodeId);
    if (!nodeId || !activeGraph) {
      setSelectedNode(null);
      setSelectedDetection(null);
      setSourceCode(null);
      return;
    }

    const node = activeGraph.nodes.find((n) => n.id === nodeId) || null;
    setSelectedNode(node);

    // If it's a pattern, locate corresponding detection
    if (node?.metadata?.patternType && report) {
      const det = report.detections.find(
        (d) => d.patternType === node.metadata?.patternType && node.id.includes(d.patternType)
      );
      setSelectedDetection(det || null);
    } else {
      setSelectedDetection(null);
    }

    // Load source code preview if filePath is known
    const filePath = node?.metadata?.filePath;
    if (filePath) {
      try {
        const code = await container.sourceCodeService.execute(filePath);
        setSourceCode(code);
      } catch (err) {
        setSourceCode(`// Could not load file: ${filePath}`);
      }
    } else {
      setSourceCode(null);
    }
  };

  // Re-filter graph when search/category/confidence changes
  useEffect(() => {
    if (!activeGraph) {
      setFilteredGraph(null);
      return;
    }

    const filtered = container.filterService.execute(activeGraph, {
      query: searchQuery,
      category: selectedCategory || undefined,
      minConfidence: minConfidence > 0 ? minConfidence : undefined,
    });
    setFilteredGraph(filtered);
  }, [activeGraph, searchQuery, selectedCategory, minConfidence]);

  // Initial load
  useEffect(() => {
    scan();
  }, []);

  const switchView = (view: 'patterns' | 'dataflow') => {
    setCurrentView(view);
    if (view === 'dataflow' && !dataFlowSummary) {
      loadDataFlow();
    }
  };

  return (
    <ViewerContext.Provider
      value={{
        currentView,
        projectPath,
        setProjectPath,
        isLoading,
        error,
        report,
        selectedDetection,
        dataFlowSummary,
        activeVariable,
        dataFlowDirection,
        activeGraph,
        filteredGraph,
        selectedNodeId,
        selectedNode,
        sourceCode,
        searchQuery,
        setSearchQuery,
        selectedCategory,
        setSelectedCategory,
        minConfidence,
        setMinConfidence,
        layoutAlgorithm,
        setLayoutAlgorithm,
        scan,
        loadDataFlow,
        traceVariable,
        selectNode,
        switchView,
      }}
    >
      {children}
    </ViewerContext.Provider>
  );
};

export const useViewer = (): ViewerContextType => {
  const context = useContext(ViewerContext);
  if (!context) {
    throw new Error('useViewer must be used within a ViewerProvider');
  }
  return context;
};
