import { StylesheetStyle } from 'cytoscape';

export const CYTOSCAPE_THEME: StylesheetStyle[] = [
  // Generic Node
  {
    selector: 'node',
    style: {
      'label': 'data(label)',
      'color': '#f8fafc',
      'font-size': '11px',
      'font-family': 'Inter, system-ui, sans-serif',
      'text-valign': 'center',
      'text-halign': 'center',
      'background-color': '#1e293b',
      'border-color': '#475569',
      'border-width': 1.5,
      'border-opacity': 0.8,
      'padding': '8px',
      'shape': 'round-rectangle',
      'width': 'label',
      'height': '36px',
      'text-max-width': '160px',
      'text-wrap': 'ellipsis',
    },
  },

  // Compound / Cluster Node
  {
    selector: 'node[kind = "cluster"]',
    style: {
      'background-color': '#0f172a',
      'background-opacity': 0.6,
      'border-color': '#334155',
      'border-width': 1,
      'border-style': 'dashed',
      'text-valign': 'top',
      'text-halign': 'center',
      'font-size': '10px',
      'color': '#94a3b8',
      'font-weight': 'bold',
      'padding': '16px',
      'shape': 'round-rectangle',
    },
  },

  // Class Node
  {
    selector: 'node[kind = "class"]',
    style: {
      'background-color': '#0369a1',
      'border-color': '#38bdf8',
      'border-width': 2,
      'shape': 'round-rectangle',
    },
  },

  // Interface Node
  {
    selector: 'node[kind = "interface"]',
    style: {
      'background-color': '#4338ca',
      'border-color': '#818cf8',
      'border-width': 2,
      'shape': 'round-rectangle',
    },
  },

  // Function Node
  {
    selector: 'node[kind = "function"]',
    style: {
      'background-color': '#065f46',
      'border-color': '#34d399',
      'border-width': 1.5,
      'shape': 'ellipse',
      'width': 'label',
      'height': '34px',
    },
  },

  // Variable Node
  {
    selector: 'node[kind = "variable"]',
    style: {
      'background-color': '#854d0e',
      'border-color': '#facc15',
      'border-width': 1.5,
      'shape': 'round-diamond',
      'width': 'label',
      'height': '34px',
    },
  },

  // Pattern Node
  {
    selector: 'node[kind = "pattern"]',
    style: {
      'background-color': '#9f1239',
      'border-color': '#fb7185',
      'border-width': 2,
      'shape': 'hexagon',
      'font-weight': 'bold',
    },
  },

  // Root Node Highlight
  {
    selector: 'node[?isRoot]',
    style: {
      'background-color': '#2563eb',
      'border-color': '#60a5fa',
      'border-width': 3.5,
      'border-opacity': 1,
    },
  },

  // Node Selection
  {
    selector: 'node:selected',
    style: {
      'border-color': '#f43f5e',
      'border-width': 3.5,
      'border-opacity': 1,
    },
  },

  // Generic Edge
  {
    selector: 'edge',
    style: {
      'width': 1.5,
      'line-color': '#64748b',
      'target-arrow-color': '#64748b',
      'target-arrow-shape': 'triangle',
      'curve-style': 'bezier',
      'arrow-scale': 0.9,
      'font-size': '9px',
      'color': '#cbd5e1',
      'text-background-color': '#0f172a',
      'text-background-opacity': 0.8,
      'text-background-padding': '2px',
      'text-background-shape': 'roundrectangle',
      'label': 'data(label)',
    },
  },

  // Reads Edge
  {
    selector: 'edge[kind = "READS"]',
    style: {
      'line-color': '#38bdf8',
      'target-arrow-color': '#38bdf8',
    },
  },

  // Writes Edge
  {
    selector: 'edge[kind = "WRITES"]',
    style: {
      'line-color': '#f59e0b',
      'target-arrow-color': '#f59e0b',
      'line-style': 'dashed',
    },
  },

  // Modifies Edge
  {
    selector: 'edge[kind = "MODIFIES"]',
    style: {
      'line-color': '#ec4899',
      'target-arrow-color': '#ec4899',
      'line-style': 'dotted',
    },
  },

  // Implements Edge
  {
    selector: 'edge[kind = "IMPLEMENTS"]',
    style: {
      'line-color': '#34d399',
      'target-arrow-color': '#34d399',
    },
  },

  // Selected Edge
  {
    selector: 'edge:selected',
    style: {
      'width': 3,
      'line-color': '#f43f5e',
      'target-arrow-color': '#f43f5e',
    },
  },
];
