import { SourceProviderPort } from '../../../ports/outbound/source-provider.port';

export class MockSourceProviderAdapter implements SourceProviderPort {
  public async readFile(filePath: string): Promise<string> {
    return `// Mock C++ source file: ${filePath}
#include <iostream>
#include <memory>
#include <vector>

class AppConfig {
private:
    static AppConfig* instance;
    AppConfig() = default;
public:
    static AppConfig& getInstance() {
        static AppConfig inst;
        return inst;
    }
    AppConfig(const AppConfig&) = delete;
    AppConfig& operator=(const AppConfig&) = delete;
};

// Architecture inspected by DPX-Cpp static engine
void runPipeline() {
    auto& cfg = AppConfig::getInstance();
    std::cout << "DPX Architecture Viewer running" << std::endl;
}
`;
  }

  public async pickFolder(): Promise<string | null> {
    const input = window.prompt('Enter C++ Project Directory path:', 'examples/cpp_samples');
    return input ? input.trim() : null;
  }
}
