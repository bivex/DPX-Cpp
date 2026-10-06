import { DataFlowGraph, DataFlowSummary } from '../../../domain/models/data-flow';
import { DetectionReport } from '../../../domain/models/pattern-detection';
import { AnalyzerPort } from '../../../ports/outbound/analyzer.port';
import {
  SAMPLE_DATA_FLOW_GRAPH,
  SAMPLE_DATA_FLOW_SUMMARY,
  SAMPLE_DETECTION_REPORT,
} from './sample-data';

export class MockAnalyzerAdapter implements AnalyzerPort {
  public async scan(_projectPath: string, _minConfidence?: number): Promise<DetectionReport> {
    return SAMPLE_DETECTION_REPORT;
  }

  public async traceDataFlowAll(_projectPath: string): Promise<DataFlowSummary> {
    return SAMPLE_DATA_FLOW_SUMMARY;
  }

  public async traceDataFlowTarget(
    _projectPath: string,
    target: string,
    _direction?: string,
    _variant?: string
  ): Promise<DataFlowGraph> {
    return {
      ...SAMPLE_DATA_FLOW_GRAPH,
      root: target || SAMPLE_DATA_FLOW_GRAPH.root,
    };
  }
}
