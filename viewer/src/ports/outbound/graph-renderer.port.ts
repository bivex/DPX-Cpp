import { ArchitectureGraph } from '../../domain/models/architecture-graph';

export type GraphLayoutAlgorithm = 'dagre' | 'cose' | 'breadthfirst' | 'concentric' | 'circle';

export interface GraphRendererPort {
  mount(container: HTMLElement): void;
  unmount(): void;
  render(graph: ArchitectureGraph, layout?: GraphLayoutAlgorithm): void;
  fit(): void;
  centerNode(nodeId: string): void;
  onNodeClick(callback: (nodeId: string) => void): void;
  exportPng(): string;
}
