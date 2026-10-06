import { EdgeKind, NodeKind } from '../value-objects/types';

export interface GraphNode {
  id: string;
  label: string;
  kind: NodeKind;
  parent?: string; // For compound cluster nodes
  isRoot?: boolean;
  metadata?: {
    filePath?: string;
    line?: number;
    patternType?: string;
    category?: string;
    confidenceScore?: number;
    readersCount?: number;
    writersCount?: number;
    impactLevel?: string;
    details?: string;
  };
}

export interface GraphEdge {
  id: string;
  source: string;
  target: string;
  kind: EdgeKind | string;
  label?: string;
  weight?: number;
}

export interface ArchitectureGraph {
  title: string;
  nodes: GraphNode[];
  edges: GraphEdge[];
}
