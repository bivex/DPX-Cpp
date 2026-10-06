import cytoscape, { Core, ElementDefinition } from 'cytoscape';
import dagre from 'cytoscape-dagre';
import { ArchitectureGraph } from '../../../domain/models/architecture-graph';
import { GraphLayoutAlgorithm, GraphRendererPort } from '../../../ports/outbound/graph-renderer.port';
import { CYTOSCAPE_THEME } from './cytoscape-theme';

// Register dagre layout plugin
try {
  cytoscape.use(dagre);
} catch (e) {
  // Ignore duplicate registration
}

export class CytoscapeGraphAdapter implements GraphRendererPort {
  private cy: Core | null = null;
  private container: HTMLElement | null = null;
  private nodeClickCallback: ((nodeId: string) => void) | null = null;

  public mount(container: HTMLElement): void {
    this.container = container;
    this.cy = cytoscape({
      container: this.container,
      elements: [],
      style: CYTOSCAPE_THEME,
      wheelSensitivity: 0.25,
      minZoom: 0.1,
      maxZoom: 3.5,
      layout: { name: 'preset' },
    });

    this.cy.on('tap', 'node', (evt) => {
      const node = evt.target;
      const nodeId = node.id();
      if (this.nodeClickCallback) {
        this.nodeClickCallback(nodeId);
      }
    });
  }

  public unmount(): void {
    if (this.cy) {
      this.cy.destroy();
      this.cy = null;
    }
    this.container = null;
  }

  public render(graph: ArchitectureGraph, layoutAlgorithm: GraphLayoutAlgorithm = 'dagre'): void {
    if (!this.cy) return;

    this.cy.elements().remove();

    const elements: ElementDefinition[] = [];

    // First add parent/cluster nodes
    graph.nodes
      .filter((n) => n.kind === 'cluster')
      .forEach((node) => {
        elements.push({
          group: 'nodes',
          data: {
            id: node.id,
            label: node.label,
            kind: node.kind,
            ...node.metadata,
          },
        });
      });

    // Then add standard nodes
    graph.nodes
      .filter((n) => n.kind !== 'cluster')
      .forEach((node) => {
        elements.push({
          group: 'nodes',
          data: {
            id: node.id,
            label: node.label,
            kind: node.kind,
            parent: node.parent,
            isRoot: node.isRoot,
            ...node.metadata,
          },
        });
      });

    // Then add edges
    graph.edges.forEach((edge) => {
      elements.push({
        group: 'edges',
        data: {
          id: edge.id,
          source: edge.source,
          target: edge.target,
          kind: edge.kind,
          label: edge.label || '',
        },
      });
    });

    this.cy.add(elements);

    // Apply layout
    this.applyLayout(layoutAlgorithm);
  }

  private applyLayout(algorithm: GraphLayoutAlgorithm): void {
    if (!this.cy) return;

    let layoutOptions: any;

    switch (algorithm) {
      case 'dagre':
        layoutOptions = {
          name: 'dagre',
          rankDir: 'LR',
          nodeSep: 50,
          rankSep: 80,
          edgeSep: 20,
          animate: true,
          animationDuration: 400,
        };
        break;
      case 'cose':
        layoutOptions = {
          name: 'cose',
          animate: true,
          animationDuration: 400,
          nodeOverlap: 20,
          idealEdgeLength: 80,
        };
        break;
      case 'breadthfirst':
        layoutOptions = {
          name: 'breadthfirst',
          directed: true,
          padding: 30,
          spacingFactor: 1.25,
          animate: true,
        };
        break;
      case 'concentric':
        layoutOptions = {
          name: 'concentric',
          padding: 30,
          animate: true,
        };
        break;
      case 'circle':
        layoutOptions = {
          name: 'circle',
          padding: 30,
          animate: true,
        };
        break;
      default:
        layoutOptions = {
          name: 'dagre',
          rankDir: 'LR',
          animate: true,
        };
    }

    const layout = this.cy.layout(layoutOptions);
    layout.run();
  }

  public fit(): void {
    if (this.cy) {
      this.cy.fit(undefined, 30);
    }
  }

  public centerNode(nodeId: string): void {
    if (!this.cy) return;
    const node = this.cy.getElementById(nodeId);
    if (node && node.length > 0) {
      this.cy.center(node);
      this.cy.zoom({
        level: 1.2,
        renderedPosition: { x: this.cy.width() / 2, y: this.cy.height() / 2 },
      });
      node.select();
    }
  }

  public onNodeClick(callback: (nodeId: string) => void): void {
    this.nodeClickCallback = callback;
  }

  public exportPng(): string {
    if (!this.cy) return '';
    return this.cy.png({
      output: 'base64uri',
      bg: '#090d16',
      full: true,
      scale: 2,
    });
  }
}
