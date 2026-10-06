import { CodeLocation, ConfidenceInfo, PatternCategory } from '../value-objects/types';

export interface Detection {
  id: string;
  patternType: string;
  patternCategory: PatternCategory;
  targetName: string;
  targetKind: string;
  confidence: ConfidenceInfo;
  primaryLocation?: CodeLocation;
  relatedLocations: CodeLocation[];
  summary?: string;
}

export interface DetectionReport {
  projectPath: string;
  scannedFilesCount: number;
  totalDetections: number;
  elapsedSeconds: number;
  summaryByCategory: Record<string, number>;
  summaryByType: Record<string, number>;
  summaryByConfidenceLevel: Record<string, number>;
  detections: Detection[];
}
