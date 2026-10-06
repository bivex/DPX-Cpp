import { ArchitectureGraph } from '../../domain/models/architecture-graph';
import { DataFlowGraph, DataFlowSummary } from '../../domain/models/data-flow';
import { GraphTransformerService } from '../../domain/services/graph-transformer.service';
import { TraceDataFlowUseCase } from '../../ports/inbound/use-cases';
import { AnalyzerPort } from '../../ports/outbound/analyzer.port';

export class DataFlowService implements TraceDataFlowUseCase {
  constructor(
    private readonly analyzerPort: AnalyzerPort,
    private readonly transformerService: GraphTransformerService
  ) {}

  public async executeSummary(projectPath: string): Promise<DataFlowSummary> {
    return this.analyzerPort.traceDataFlowAll(projectPath);
  }

  public async executeTarget(
    projectPath: string,
    target: string,
    direction: string = 'out',
    variant: string = 'simplified'
  ): Promise<{ dataFlowGraph: DataFlowGraph; graph: ArchitectureGraph }> {
    const dataFlowGraph = await this.analyzerPort.traceDataFlowTarget(
      projectPath,
      target,
      direction,
      variant
    );
    const graph = this.transformerService.fromDataFlowGraph(dataFlowGraph);
    return { dataFlowGraph, graph };
  }
}
