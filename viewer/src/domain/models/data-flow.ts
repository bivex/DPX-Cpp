export interface DataFlowSummaryItem {
  variableName: string;
  location: string;
  readersCount: number;
  writersCount: number;
  reachNodes: number;
  maxDepth: number;
  impactLevel: 'HIGH' | 'MEDIUM' | 'LOW';
}

export interface DataFlowSummary {
  direction: 'out' | 'in';
  totalVariables: number;
  summary: DataFlowSummaryItem[];
}

export interface DataFlowNode {
  id: string;
  name: string;
  kind: 'variable' | 'function' | 'class';
  cluster: string;
  filePath: string;
  line: number;
  isRoot: boolean;
}

export interface DataFlowEdge {
  from: string;
  to: string;
  kind: 'READS' | 'WRITES' | 'MODIFIES';
  location?: string;
}

export interface DataFlowGraph {
  root: string;
  direction: 'OUT' | 'IN';
  variant: 'simplified' | 'cluster' | 'relationship';
  nodes: DataFlowNode[];
  edges: DataFlowEdge[];
}
