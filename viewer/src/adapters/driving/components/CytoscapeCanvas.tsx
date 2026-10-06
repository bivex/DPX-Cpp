import React, { useEffect, useRef } from 'react';
import { useViewer } from '../../../application/state/viewer-context';
import { container } from '../../../bootstrap/container';
import { GraphLayoutAlgorithm, GraphRendererPort } from '../../../ports/outbound/graph-renderer.port';

export const CytoscapeCanvas: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const rendererRef = useRef<GraphRendererPort | null>(null);

  const {
    filteredGraph,
    layoutAlgorithm,
    setLayoutAlgorithm,
    selectNode,
    selectedNodeId,
  } = useViewer();

  // Initialize renderer once
  useEffect(() => {
    if (!containerRef.current) return;

    const renderer = container.createGraphRenderer();
    renderer.mount(containerRef.current);
    renderer.onNodeClick((nodeId) => {
      selectNode(nodeId);
    });
    rendererRef.current = renderer;

    return () => {
      renderer.unmount();
      rendererRef.current = null;
    };
  }, []);

  // Update render when graph or layout changes
  useEffect(() => {
    if (rendererRef.current && filteredGraph) {
      rendererRef.current.render(filteredGraph, layoutAlgorithm);
    }
  }, [filteredGraph, layoutAlgorithm]);

  // Center on node if selected externally
  useEffect(() => {
    if (rendererRef.current && selectedNodeId) {
      rendererRef.current.centerNode(selectedNodeId);
    }
  }, [selectedNodeId]);

  const handleFit = () => {
    rendererRef.current?.fit();
  };

  const handleExportPng = () => {
    if (!rendererRef.current) return;
    const dataUri = rendererRef.current.exportPng();
    if (!dataUri) return;
    const a = document.createElement('a');
    a.href = dataUri;
    a.download = `dpx-architecture-graph-${Date.now()}.png`;
    a.click();
  };

  const layouts: Array<{ id: GraphLayoutAlgorithm; label: string }> = [
    { id: 'dagre', label: 'Dagre (Hierarchical)' },
    { id: 'cose', label: 'CoSE (Physics / Force)' },
    { id: 'breadthfirst', label: 'Breadthfirst' },
    { id: 'concentric', label: 'Concentric' },
    { id: 'circle', label: 'Circle' },
  ];

  return (
    <div className="canvas-wrapper">
      <div className="canvas-toolbar">
        <div className="toolbar-group">
          <span className="toolbar-label">Layout:</span>
          <select
            className="layout-select"
            value={layoutAlgorithm}
            onChange={(e) => setLayoutAlgorithm(e.target.value as GraphLayoutAlgorithm)}
          >
            {layouts.map((l) => (
              <option key={l.id} value={l.id}>
                {l.label}
              </option>
            ))}
          </select>
        </div>

        <div className="toolbar-group">
          <button className="tool-btn" onClick={handleFit} title="Fit to viewport">
            ⛶ Fit View
          </button>
          <button className="tool-btn" onClick={handleExportPng} title="Export as PNG image">
            📷 Export PNG
          </button>
        </div>

        <div className="graph-stats">
          <span>{filteredGraph?.nodes.length || 0} nodes</span>
          <span>•</span>
          <span>{filteredGraph?.edges.length || 0} connections</span>
        </div>
      </div>

      <div ref={containerRef} className="cytoscape-container" />
    </div>
  );
};
