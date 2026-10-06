export interface SourceProviderPort {
  readFile(filePath: string): Promise<string>;
  pickFolder(): Promise<string | null>;
}
