import { invoke } from '@tauri-apps/api/core';
import { SourceProviderPort } from '../../../ports/outbound/source-provider.port';
import { MockSourceProviderAdapter } from '../mock/mock-source.adapter';

export class TauriSourceProviderAdapter implements SourceProviderPort {
  private mockFallback = new MockSourceProviderAdapter();

  private isTauriAvailable(): boolean {
    return typeof window !== 'undefined' && '__TAURI_INTERNALS__' in window;
  }

  public async readFile(filePath: string): Promise<string> {
    if (!this.isTauriAvailable()) {
      return this.mockFallback.readFile(filePath);
    }

    try {
      return await invoke<string>('read_source_file', { filePath });
    } catch (err) {
      console.error(`Failed to read source file '${filePath}':`, err);
      return this.mockFallback.readFile(filePath);
    }
  }
}
