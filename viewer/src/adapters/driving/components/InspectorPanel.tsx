import React, { useEffect, useRef } from 'react';
import { useViewer } from '../../../application/state/viewer-context';

export const InspectorPanel: React.FC = () => {
  const {
    selectedNode,
    selectedDetection,
    selectNode,
    sourceCode,
  } = useViewer();

  const targetLineRef = useRef<HTMLDivElement | null>(null);

  const highlightLine = selectedNode?.metadata?.line || selectedDetection?.primaryLocation?.line;

  // Auto-scroll code preview container so the exact targeted line is centered
  useEffect(() => {
    if (targetLineRef.current) {
      targetLineRef.current.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      });
    }
  }, [sourceCode, highlightLine]);

  if (!selectedNode && !selectedDetection) {
    return null;
  }

  const scrollToTarget = () => {
    targetLineRef.current?.scrollIntoView({
      behavior: 'smooth',
      block: 'center',
    });
  };

  return (
    <section className="inspector-panel">
      <div className="inspector-header">
        <div className="inspector-title-group">
          <span className="inspector-kind-badge">
            {selectedNode?.kind.toUpperCase() || 'ENTITY'}
          </span>
          <h3 className="inspector-title">{selectedNode?.label || selectedDetection?.targetName}</h3>
        </div>
        <button className="close-btn" onClick={() => selectNode(null)} title="Close Inspector">
          ✕
        </button>
      </div>

      <div className="inspector-content">
        {/* Detection Details (If Pattern / Principle) */}
        {selectedDetection && (
          <div className="inspector-section">
            <h4 className="section-title">Pattern Detection</h4>
            <div className="meta-grid">
              <div className="meta-item">
                <span className="meta-label">Category</span>
                <span className="meta-val">{selectedDetection.patternCategory}</span>
              </div>
              <div className="meta-item">
                <span className="meta-label">Confidence</span>
                <span className={`meta-val conf-${selectedDetection.confidence.level.toLowerCase()}`}>
                  {selectedDetection.confidence.percentage} ({selectedDetection.confidence.level})
                </span>
              </div>
            </div>

            {selectedDetection.summary && (
              <p className="detection-desc">{selectedDetection.summary}</p>
            )}

            {/* Evidence Trail */}
            {selectedDetection.confidence.evidences.length > 0 && (
              <div className="evidences-list">
                <h5 className="sub-title">Evidence Trail ({selectedDetection.confidence.evidences.length})</h5>
                {selectedDetection.confidence.evidences.map((ev, i) => (
                  <div key={i} className="evidence-item">
                    <div className="evidence-header">
                      <span className="rule-code">{ev.ruleCode}</span>
                      <span className="evidence-weight">+{Math.round(ev.weight * 100)}%</span>
                    </div>
                    <div className="evidence-desc">{ev.description}</div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Node Metadata (If DataFlow Variable/Function) */}
        {selectedNode && selectedNode.metadata && (
          <div className="inspector-section">
            <h4 className="section-title">Node Metadata</h4>
            <div className="meta-grid">
              {selectedNode.metadata.filePath && (
                <div className="meta-item full-width">
                  <span className="meta-label">File</span>
                  <span className="meta-val code-path">{selectedNode.metadata.filePath}</span>
                </div>
              )}
              {selectedNode.metadata.line && (
                <div className="meta-item">
                  <span className="meta-label">Exact Line</span>
                  <span className="meta-val">Line {selectedNode.metadata.line}</span>
                </div>
              )}
              {selectedNode.metadata.details && (
                <div className="meta-item full-width">
                  <span className="meta-label">Details</span>
                  <span className="meta-val">{selectedNode.metadata.details}</span>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Source Code Viewer with Auto-Scroll & Line Pinpointing */}
        {sourceCode && (
          <div className="inspector-section code-section">
            <div className="code-header">
              <h4 className="section-title">C++ Source Preview</h4>
              {highlightLine !== undefined && (
                <button className="line-jump-badge" onClick={scrollToTarget} title="Jump to line in code">
                  🎯 Line {highlightLine}
                </button>
              )}
            </div>
            <div className="code-viewer-container">
              <pre className="code-block">
                {sourceCode.split('\n').map((lineText, idx) => {
                  const lineNum = idx + 1;
                  const isTarget = highlightLine === lineNum;
                  const isNear = highlightLine !== undefined && Math.abs(lineNum - highlightLine) <= 2;
                  return (
                    <div
                      key={idx}
                      ref={isTarget ? targetLineRef : undefined}
                      className={`code-line ${isTarget ? 'target-line' : ''} ${
                        isNear && !isTarget ? 'highlight-range' : ''
                      }`}
                    >
                      <span className="line-num">{lineNum}</span>
                      <span className="line-code">{lineText || ' '}</span>
                    </div>
                  );
                })}
              </pre>
            </div>
          </div>
        )}
      </div>
    </section>
  );
};
