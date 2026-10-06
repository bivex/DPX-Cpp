import { CytoscapeGraphAdapter } from '../adapters/driven/cytoscape/cytoscape-graph.adapter';
import { TauriAnalyzerAdapter } from '../adapters/driven/tauri/tauri-analyzer.adapter';
import { TauriSourceProviderAdapter } from '../adapters/driven/tauri/tauri-source.adapter';
import { DataFlowService } from '../application/services/data-flow.service';
import { FilterService } from '../application/services/filter.service';
import { ScanService } from '../application/services/scan.service';
import { SourceCodeService } from '../application/services/source-code.service';
import { GraphFilterService } from '../domain/services/graph-filter.service';
import { GraphTransformerService } from '../domain/services/graph-transformer.service';

export class AppContainer {
  public readonly transformerService: GraphTransformerService;
  public readonly filterDomainService: GraphFilterService;

  public readonly analyzerAdapter: TauriAnalyzerAdapter;
  public readonly sourceAdapter: TauriSourceProviderAdapter;

  public readonly scanService: ScanService;
  public readonly dataFlowService: DataFlowService;
  public readonly sourceCodeService: SourceCodeService;
  public readonly filterService: FilterService;

  constructor() {
    this.transformerService = new GraphTransformerService();
    this.filterDomainService = new GraphFilterService();

    this.analyzerAdapter = new TauriAnalyzerAdapter();
    this.sourceAdapter = new TauriSourceProviderAdapter();

    this.scanService = new ScanService(this.analyzerAdapter, this.transformerService);
    this.dataFlowService = new DataFlowService(this.analyzerAdapter, this.transformerService);
    this.sourceCodeService = new SourceCodeService(this.sourceAdapter);
    this.filterService = new FilterService(this.filterDomainService);
  }

  public createGraphRenderer(): CytoscapeGraphAdapter {
    return new CytoscapeGraphAdapter();
  }
}

// Global singleton container instance
export const container = new AppContainer();
