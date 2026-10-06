import React, { useState } from 'react';
import { useViewer } from '../../../application/state/viewer-context';

export const HeaderBar: React.FC = () => {
  const {
    projectPath,
    setProjectPath,
    currentView,
    switchView,
    scan,
    loadDataFlow,
    isLoading,
  } = useViewer();

  const [inputPath, setInputPath] = useState(projectPath);

  const handleScanClick = () => {
    setProjectPath(inputPath);
    if (currentView === 'patterns') {
      scan(inputPath);
    } else {
      loadDataFlow(inputPath);
    }
  };

  return (
    <header className="header-bar">
      <div className="header-left">
        <div className="brand">
          <span className="brand-icon">⚡</span>
          <span className="brand-title">DPX-Cpp</span>
          <span className="brand-badge">Viewer</span>
        </div>

        <nav className="view-switcher">
          <button
            className={`tab-btn ${currentView === 'patterns' ? 'active' : ''}`}
            onClick={() => switchView('patterns')}
          >
            🏛 Design Patterns & SOLID
          </button>
          <button
            className={`tab-btn ${currentView === 'dataflow' ? 'active' : ''}`}
            onClick={() => switchView('dataflow')}
          >
            🌲 Data Flow (SciTools Parity)
          </button>
        </nav>
      </div>

      <div className="header-right">
        <div className="path-input-group">
          <input
            type="text"
            className="path-input"
            value={inputPath}
            onChange={(e) => setInputPath(e.target.value)}
            placeholder="Target C++ directory / file..."
            disabled={isLoading}
          />
          <button
            className="action-btn"
            onClick={handleScanClick}
            disabled={isLoading}
          >
            {isLoading ? <span className="spinner">⏳</span> : '⚡ Scan'}
          </button>
        </div>
      </div>
    </header>
  );
};
