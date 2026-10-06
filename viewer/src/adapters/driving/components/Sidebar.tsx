import React from 'react';
import { useViewer } from '../../../application/state/viewer-context';

export const Sidebar: React.FC = () => {
  const {
    currentView,
    report,
    selectedDetection,
    selectNode,
    dataFlowSummary,
    activeVariable,
    dataFlowDirection,
    traceVariable,
    searchQuery,
    setSearchQuery,
    selectedCategory,
    setSelectedCategory,
    minConfidence,
    setMinConfidence,
  } = useViewer();

  const categories = [
    { id: null, label: 'All' },
    { id: 'creational', label: 'Creational' },
    { id: 'structural', label: 'Structural' },
    { id: 'behavioral', label: 'Behavioral' },
    { id: 'principle', label: 'SOLID / Clean' },
  ];

  return (
    <aside className="sidebar">
      {/* Search and Filters */}
      <div className="sidebar-filter-section">
        <input
          type="text"
          className="search-input"
          placeholder="Search entities, rules, variables..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />

        {currentView === 'patterns' && (
          <>
            <div className="category-pills">
              {categories.map((cat) => (
                <button
                  key={cat.label}
                  className={`pill-btn ${selectedCategory === cat.id ? 'active' : ''}`}
                  onClick={() => setSelectedCategory(cat.id)}
                >
                  {cat.label}
                </button>
              ))}
            </div>

            <div className="confidence-slider-group">
              <div className="slider-label">
                <span>Min Confidence:</span>
                <span className="slider-value">{Math.round(minConfidence * 100)}%</span>
              </div>
              <input
                type="range"
                min="0"
                max="1"
                step="0.05"
                value={minConfidence}
                onChange={(e) => setMinConfidence(parseFloat(e.target.value))}
                className="confidence-slider"
              />
            </div>
          </>
        )}

        {currentView === 'dataflow' && (
          <div className="direction-toggle-group">
            <span className="toggle-label">Propagation Flow:</span>
            <div className="toggle-buttons">
              <button
                className={`toggle-btn ${dataFlowDirection === 'out' ? 'active' : ''}`}
                onClick={() => activeVariable && traceVariable(activeVariable, 'out')}
              >
                Forward (OUT)
              </button>
              <button
                className={`toggle-btn ${dataFlowDirection === 'in' ? 'active' : ''}`}
                onClick={() => activeVariable && traceVariable(activeVariable, 'in')}
              >
                Backward (IN)
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Main List Content */}
      <div className="sidebar-list-container">
        {currentView === 'patterns' ? (
          <div className="detections-list">
            <div className="list-header">
              <span>Detections ({report?.detections.length || 0})</span>
              <span className="scanned-files">{report?.scannedFilesCount || 0} files</span>
            </div>

            {report?.detections.map((det) => {
              const isSelected = selectedDetection?.id === det.id;
              const confLevel = det.confidence.level.toLowerCase();

              return (
                <div
                  key={det.id}
                  className={`detection-card ${isSelected ? 'selected' : ''}`}
                  onClick={() => {
                    const patternNodeId = `pattern_${det.patternType}_${report.detections.indexOf(det)}`;
                    selectNode(patternNodeId);
                  }}
                >
                  <div className="card-top">
                    <span className="pattern-badge">{det.patternType.replace(/_/g, ' ')}</span>
                    <span className={`confidence-tag conf-${confLevel}`}>
                      {det.confidence.percentage}
                    </span>
                  </div>

                  <div className="target-name">{det.targetName}</div>

                  {det.summary && <div className="card-summary">{det.summary}</div>}

                  {det.primaryLocation && (
                    <div className="card-location">
                      📍 {det.primaryLocation.filePath.split('/').pop()}:{det.primaryLocation.line}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        ) : (
          <div className="variables-list">
            <div className="list-header">
              <span>Variables Matrix ({dataFlowSummary?.summary.length || 0})</span>
            </div>

            {dataFlowSummary?.summary.map((v) => {
              const isActive = activeVariable === v.variableName;
              return (
                <div
                  key={v.variableName}
                  className={`variable-card ${isActive ? 'active' : ''}`}
                  onClick={() => traceVariable(v.variableName, dataFlowDirection)}
                >
                  <div className="variable-card-top">
                    <span className="variable-name">🔷 {v.variableName}</span>
                    <span className={`impact-badge impact-${v.impactLevel.toLowerCase()}`}>
                      {v.impactLevel}
                    </span>
                  </div>

                  <div className="variable-metrics">
                    <span className="metric-tag">Reads: {v.readersCount}</span>
                    <span className="metric-tag">Writes: {v.writersCount}</span>
                    <span className="metric-tag">Reach: {v.reachNodes}</span>
                  </div>

                  {v.location && <div className="variable-loc">📍 {v.location}</div>}
                </div>
              );
            })}
          </div>
        )}
      </div>
    </aside>
  );
};
