export interface SourceProviderPort {
  readFile(filePath: string): Promise<string>;
}
