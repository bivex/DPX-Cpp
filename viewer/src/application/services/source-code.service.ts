import { ReadSourceCodeUseCase } from '../../ports/inbound/use-cases';
import { SourceProviderPort } from '../../ports/outbound/source-provider.port';

export class SourceCodeService implements ReadSourceCodeUseCase {
  constructor(private readonly sourceProviderPort: SourceProviderPort) {}

  public async execute(filePath: string): Promise<string> {
    return this.sourceProviderPort.readFile(filePath);
  }
}
