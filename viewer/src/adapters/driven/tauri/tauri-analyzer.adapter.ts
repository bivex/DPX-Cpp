import { invoke } from '@tauri-apps/api/core';
import { DataFlowGraph, DataFlowSummary } from '../../../domain/models/data-flow';
import { DetectionReport } from '../../../domain/models/pattern-detection';
import { AnalyzerPort } from '../../../ports/outbound/analyzer.port';
import { MockAnalyzerAdapter } from '../mock/mock-analyzer.adapter';

export class TauriAnalyzerAdapter implements AnalyzerPort {
  private mockFallback = new MockAnalyzerAdapter();

  private isTauriAvailable(): boolean {
    return typeof window !== 'undefined' && '__TAURI_INTERNALS__' in window;
  }

  public async scan(projectPath: string, minConfidence?: number): Promise<DetectionReport> {
    if (!this.isTauriAvailable()) {
      console.warn('Tauri runtime not detected, falling back to mock analyzer');
      return this.mockFallback.scan(projectPath, minConfidence);
    }

    try {
      const raw = await invoke<any>('scan_project', {
        projectPath,
        minConfidence: minConfidence ?? 0.0,
      });

      return {
        projectPath: raw.project_path || projectPath,
        scannedFilesCount: raw.scanned_files_count || 0,
        totalDetections: raw.total_detections || 0,
        elapsedSeconds: raw.elapsed_seconds || 0,
        summaryByCategory: raw.summary_by_category || {},
        summaryByType: raw.summary_by_type || {},
        summaryByConfidenceLevel: raw.summary_by_confidence_level || {},
        detections: (raw.detections || []).map((d: any, idx: number) => ({
          id: `det_${idx}`,
          patternType: d.pattern_type,
          patternCategory: d.pattern_category,
          targetName: d.target_name,
          targetKind: d.target_kind,
          confidence: {
            score: d.confidence?.score || 0,
            level: d.confidence?.level || 'LOW',
            percentage: d.confidence?.percentage || '0%',
            evidences: (d.confidence?.evidences || []).map((e: any) => ({
              description: e.description,
              weight: e.weight,
              ruleCode: e.rule_code,
              location: e.location ? {
                filePath: e.location.file_path,
                line: e.location.line,
                column: e.location.column,
                formatted: e.location.formatted,
              } : undefined,
              snippet: e.snippet,
            })),
          },
          primaryLocation: d.primary_location?.file_path ? {
            filePath: d.primary_location.file_path,
            line: d.primary_location.line,
            column: d.primary_location.column,
            formatted: d.primary_location.formatted,
          } : (d.confidence?.evidences?.[0]?.location ? {
            filePath: d.confidence.evidences[0].location.file_path,
            line: d.confidence.evidences[0].location.line,
            column: d.confidence.evidences[0].location.column,
            formatted: d.confidence.evidences[0].location.formatted,
          } : undefined),
          relatedLocations: (d.related_locations || []).map((l: any) => ({
            filePath: l.file_path,
            line: l.line,
            formatted: l.formatted,
          })),
          summary: d.summary,
        })),
      };
    } catch (err) {
      console.error('Tauri scan failed:', err);
      throw err;
    }
  }

  public async traceDataFlowAll(projectPath: string): Promise<DataFlowSummary> {
    if (!this.isTauriAvailable()) {
      return this.mockFallback.traceDataFlowAll(projectPath);
    }

    try {
      const raw = await invoke<any>('trace_dataflow_all', { projectPath });
      return {
        direction: raw.direction || 'out',
        totalVariables: raw.total_variables || raw.summary?.length || 0,
        summary: (raw.summary || []).map((item: any) => ({
          variableName: item.variable_name || item.name || '',
          location: item.location || '',
          readersCount: item.readers_count || item.readers || 0,
          writersCount: item.writers_count || item.writers || 0,
          reachNodes: item.reach_nodes || item.reach || 0,
          maxDepth: item.max_depth || item.depth || 0,
          impactLevel: item.impact_level || item.impact || 'LOW',
        })),
      };
    } catch (err) {
      console.error('Tauri dataflow all failed:', err);
      throw err;
    }
  }

  public async traceDataFlowTarget(
    projectPath: string,
    target: string,
    direction?: string,
    variant?: string
  ): Promise<DataFlowGraph> {
    if (!this.isTauriAvailable()) {
      return this.mockFallback.traceDataFlowTarget(projectPath, target, direction, variant);
    }

    try {
      const raw = await invoke<any>('trace_dataflow_target', {
        projectPath,
        target,
        direction,
        variant,
      });

      return {
        root: raw.root || target,
        direction: (raw.direction || 'OUT').toUpperCase() as 'OUT' | 'IN',
        variant: raw.variant || 'simplified',
        nodes: (raw.nodes || []).map((n: any) => ({
          id: n.id,
          name: n.name,
          kind: n.kind,
          cluster: n.cluster || 'default',
          filePath: n.file_path || '',
          line: n.line || 1,
          isRoot: !!n.is_root,
        })),
        edges: (raw.edges || []).map((e: any) => ({
          from: e.from,
          to: e.to,
          kind: e.kind,
          location: e.location,
        })),
      };
    } catch (err) {
      console.error('Tauri dataflow target failed:', err);
      throw err;
    }
  }
}
