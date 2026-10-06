export type PatternCategory =
  | 'creational'
  | 'structural'
  | 'behavioral'
  | 'principle'
  | 'architectural'
  | 'concurrency';

export type ConfidenceLevel = 'VERY_HIGH' | 'HIGH' | 'MEDIUM' | 'LOW';

export type NodeKind =
  | 'class'
  | 'interface'
  | 'function'
  | 'variable'
  | 'pattern'
  | 'cluster';

export type EdgeKind =
  | 'READS'
  | 'WRITES'
  | 'MODIFIES'
  | 'INHERITS'
  | 'IMPLEMENTS'
  | 'DEPENDS'
  | 'CREATES';

export interface CodeLocation {
  filePath: string;
  line: number;
  column?: number;
  endLine?: number | null;
  formatted?: string;
  snippet?: string | null;
}

export interface ConfidenceInfo {
  score: number;
  level: ConfidenceLevel;
  percentage: string;
  evidences: Array<{
    description: string;
    weight: number;
    ruleCode: string;
    location?: {
      filePath?: string;
      line?: number;
      column?: number;
      formatted?: string;
    };
    snippet?: string | null;
  }>;
}
