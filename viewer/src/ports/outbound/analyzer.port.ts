import { DataFlowGraph, DataFlowSummary } from '../../domain/models/data-flow';
import { DetectionReport } from '../../domain/models/pattern-detection';

export interface AnalyzerPort {
  scan(projectPath: string, minConfidence?: number): Promise<DetectionReport>;
  traceDataFlowAll(projectPath: string): Promise<DataFlowSummary>;
  traceDataFlowTarget(
    projectPath: string,
    target: string,
    direction?: string,
    variant?: string
  ): Promise<DataFlowGraph>;
}
