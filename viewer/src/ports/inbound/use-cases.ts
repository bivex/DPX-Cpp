import { ArchitectureGraph } from '../../domain/models/architecture-graph';
import { DataFlowGraph, DataFlowSummary } from '../../domain/models/data-flow';
import { DetectionReport } from '../../domain/models/pattern-detection';
import { FilterOptions } from '../../domain/services/graph-filter.service';

export interface ScanCodebaseUseCase {
  execute(projectPath: string, minConfidence?: number): Promise<{
    report: DetectionReport;
    graph: ArchitectureGraph;
  }>;
}

export interface TraceDataFlowUseCase {
  executeSummary(projectPath: string): Promise<DataFlowSummary>;
  executeTarget(
    projectPath: string,
    target: string,
    direction?: string,
    variant?: string
  ): Promise<{
    dataFlowGraph: DataFlowGraph;
    graph: ArchitectureGraph;
  }>;
}

export interface FilterGraphUseCase {
  execute(graph: ArchitectureGraph, options: FilterOptions): ArchitectureGraph;
}

export interface ReadSourceCodeUseCase {
  execute(filePath: string): Promise<string>;
}
