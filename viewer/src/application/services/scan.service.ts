import { ArchitectureGraph } from '../../domain/models/architecture-graph';
import { DetectionReport } from '../../domain/models/pattern-detection';
import { GraphTransformerService } from '../../domain/services/graph-transformer.service';
import { ScanCodebaseUseCase } from '../../ports/inbound/use-cases';
import { AnalyzerPort } from '../../ports/outbound/analyzer.port';

export class ScanService implements ScanCodebaseUseCase {
  constructor(
    private readonly analyzerPort: AnalyzerPort,
    private readonly transformerService: GraphTransformerService
  ) {}

  public async execute(
    projectPath: string,
    minConfidence: number = 0.0
  ): Promise<{ report: DetectionReport; graph: ArchitectureGraph }> {
    const report = await this.analyzerPort.scan(projectPath, minConfidence);
    const graph = this.transformerService.fromDetectionReport(report);
    return { report, graph };
  }
}
