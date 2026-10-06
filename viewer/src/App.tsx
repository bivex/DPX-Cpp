import React from 'react';
import { CytoscapeCanvas } from './adapters/driving/components/CytoscapeCanvas';
import { HeaderBar } from './adapters/driving/components/HeaderBar';
import { InspectorPanel } from './adapters/driving/components/InspectorPanel';
import { Sidebar } from './adapters/driving/components/Sidebar';
import { ViewerProvider, useViewer } from './application/state/viewer-context';
import './App.css';

const MainLayout: React.FC = () => {
  const { error, isLoading } = useViewer();

  return (
    <div className="app-container">
      <HeaderBar />

      {error && (
        <div className="error-banner">
          <span className="error-icon">⚠️</span>
          <span className="error-text">{error}</span>
        </div>
      )}

      {isLoading && (
        <div className="loading-bar-indicator">
          <div className="loading-bar-fill" />
        </div>
      )}

      <main className="main-content">
        <Sidebar />
        <section className="viewport-area">
          <CytoscapeCanvas />
        </section>
        <InspectorPanel />
      </main>
    </div>
  );
};

export function App() {
  return (
    <ViewerProvider>
      <MainLayout />
    </ViewerProvider>
  );
}

export default App;
