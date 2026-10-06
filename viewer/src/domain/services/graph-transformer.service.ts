import { ArchitectureGraph, GraphEdge, GraphNode } from '../models/architecture-graph';
import { DataFlowGraph } from '../models/data-flow';
import { DetectionReport } from '../models/pattern-detection';

export class GraphTransformerService {
  /**
   * Convert DetectionReport (patterns & principles) into Cytoscape architecture graph
   */
  public fromDetectionReport(report: DetectionReport): ArchitectureGraph {
    const nodes: GraphNode[] = [];
    const edges: GraphEdge[] = [];
    const clusterMap = new Set<string>();

    report.detections.forEach((det, index) => {
      // 1. Cluster node for category
      const clusterId = `cluster_${det.patternCategory}`;
      if (!clusterMap.has(clusterId)) {
        clusterMap.add(clusterId);
        nodes.push({
          id: clusterId,
          label: det.patternCategory.toUpperCase(),
          kind: 'cluster',
        });
      }

      // 2. Pattern node
      const patternNodeId = `pattern_${det.patternType}_${index}`;
      nodes.push({
        id: patternNodeId,
        label: det.patternType.replace(/_/g, ' ').toUpperCase(),
        kind: 'pattern',
        parent: clusterId,
        metadata: {
          patternType: det.patternType,
          category: det.patternCategory,
          confidenceScore: det.confidence.score,
          filePath: det.primaryLocation?.filePath,
          line: det.primaryLocation?.line,
          details: det.summary || `${det.patternType} on ${det.targetName}`,
        },
      });

      // 3. Target entity node (Class / Interface / Function)
      const targetNodeId = `target_${det.targetName}`;
      if (!nodes.some((n) => n.id === targetNodeId)) {
        nodes.push({
          id: targetNodeId,
          label: det.targetName,
          kind: det.targetKind.includes('interface') || det.targetKind.includes('protocol')
            ? 'interface'
            : det.targetKind.includes('fn') || det.targetName.includes('(')
            ? 'function'
            : 'class',
          metadata: {
            filePath: det.primaryLocation?.filePath,
            line: det.primaryLocation?.line,
            details: `Target of ${det.patternType}`,
          },
        });
      }

      // Edge from Target to Pattern
      edges.push({
        id: `edge_${targetNodeId}_to_${patternNodeId}`,
        source: targetNodeId,
        target: patternNodeId,
        kind: 'IMPLEMENTS',
        label: `${Math.round(det.confidence.score * 100)}%`,
      });

      // Related locations
      det.relatedLocations.forEach((loc, relIdx) => {
        const relName = loc.filePath ? loc.filePath.split('/').pop() || 'Related' : 'Related';
        const relNodeId = `rel_${index}_${relIdx}`;
        if (!nodes.some((n) => n.id === relNodeId)) {
          nodes.push({
            id: relNodeId,
            label: `${relName}:${loc.line}`,
            kind: 'class',
            metadata: {
              filePath: loc.filePath,
              line: loc.line,
            },
          });
          edges.push({
            id: `edge_${patternNodeId}_to_${relNodeId}`,
            source: patternNodeId,
            target: relNodeId,
            kind: 'DEPENDS',
            label: 'related',
          });
        }
      });
    });

    return {
      title: `Pattern Architecture (${report.totalDetections} detections)`,
      nodes,
      edges,
    };
  }

  /**
   * Convert DataFlowGraph into Cytoscape ArchitectureGraph
   */
  public fromDataFlowGraph(dfGraph: DataFlowGraph): ArchitectureGraph {
    const nodes: GraphNode[] = [];
    const edges: GraphEdge[] = [];
    const clusters = new Set<string>();

    dfGraph.nodes.forEach((dfNode) => {
      // Cluster for namespace/cluster
      if (dfNode.cluster && dfNode.cluster !== 'default') {
        const clusterId = `cluster_${dfNode.cluster}`;
        if (!clusters.has(clusterId)) {
          clusters.add(clusterId);
          nodes.push({
            id: clusterId,
            label: dfNode.cluster,
            kind: 'cluster',
          });
        }
      }

      nodes.push({
        id: dfNode.id,
        label: dfNode.name,
        kind: dfNode.kind === 'variable' ? 'variable' : 'function',
        isRoot: dfNode.isRoot,
        parent: dfNode.cluster && dfNode.cluster !== 'default' ? `cluster_${dfNode.cluster}` : undefined,
        metadata: {
          filePath: dfNode.filePath,
          line: dfNode.line,
          details: `${dfNode.kind} (${dfNode.cluster})`,
        },
      });
    });

    dfGraph.edges.forEach((dfEdge, idx) => {
      edges.push({
        id: `df_edge_${idx}_${dfEdge.from}_${dfEdge.to}`,
        source: dfEdge.from,
        target: dfEdge.to,
        kind: dfEdge.kind,
        label: dfEdge.kind.toLowerCase(),
      });
    });

    return {
      title: `Data Flow ${dfGraph.direction} for '${dfGraph.root}'`,
      nodes,
      edges,
    };
  }
}
