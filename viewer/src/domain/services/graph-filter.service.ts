import { ArchitectureGraph, GraphNode } from '../models/architecture-graph';

export interface FilterOptions {
  query?: string;
  category?: string;
  minConfidence?: number;
  nodeKind?: string;
}

export class GraphFilterService {
  public filter(graph: ArchitectureGraph, options: FilterOptions): ArchitectureGraph {
    const { query, category, minConfidence, nodeKind } = options;

    if (!query && !category && (minConfidence === undefined || minConfidence <= 0) && !nodeKind) {
      return graph;
    }

    const lowerQuery = query ? query.toLowerCase() : '';

    // First filter candidate nodes (excluding clusters initially)
    const matchingNodeIds = new Set<string>();

    graph.nodes.forEach((node) => {
      if (node.kind === 'cluster') return;

      let matches = true;

      if (lowerQuery) {
        const matchesName = node.label.toLowerCase().includes(lowerQuery);
        const matchesId = node.id.toLowerCase().includes(lowerQuery);
        const matchesDetails = node.metadata?.details?.toLowerCase().includes(lowerQuery) || false;
        if (!matchesName && !matchesId && !matchesDetails) {
          matches = false;
        }
      }

      if (category && node.metadata?.category && node.metadata.category !== category) {
        matches = false;
      }

      if (
        minConfidence !== undefined &&
        node.metadata?.confidenceScore !== undefined &&
        node.metadata.confidenceScore < minConfidence
      ) {
        matches = false;
      }

      if (nodeKind && node.kind !== nodeKind) {
        matches = false;
      }

      if (matches) {
        matchingNodeIds.add(node.id);
      }
    });

    // Keep edges that connect matching nodes
    const filteredEdges = graph.edges.filter(
      (edge) => matchingNodeIds.has(edge.source) && matchingNodeIds.has(edge.target)
    );

    // Keep clusters that contain any matching nodes
    const filteredNodes: GraphNode[] = [];
    const usedClusters = new Set<string>();

    graph.nodes.forEach((node) => {
      if (matchingNodeIds.has(node.id)) {
        filteredNodes.push(node);
        if (node.parent) {
          usedClusters.add(node.parent);
        }
      }
    });

    // Add required cluster nodes
    graph.nodes.forEach((node) => {
      if (node.kind === 'cluster' && usedClusters.has(node.id)) {
        filteredNodes.push(node);
      }
    });

    return {
      title: `${graph.title} (Filtered: ${matchingNodeIds.size} nodes)`,
      nodes: filteredNodes,
      edges: filteredEdges,
    };
  }
}
