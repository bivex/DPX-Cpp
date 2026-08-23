#pragma once

#include <iostream>
#include <vector>
#include <memory>
#include <string>

namespace patterns {

// 1. SINGLETON (Meyers' Singleton)
class AppConfig {
public:
    static AppConfig& getInstance() {
        static AppConfig instance;
        return instance;
    }

    void load(const std::string& path) {
        std::cout << "Loading config from " << path << std::endl;
    }

private:
    AppConfig() = default;
    AppConfig(const AppConfig&) = delete;
    AppConfig& operator=(const AppConfig&) = delete;
};

// 2. STRATEGY PATTERN
class ICompressionStrategy {
public:
    virtual ~ICompressionStrategy() = default;
    virtual void compress(const std::string& file) = 0;
};

class ZipCompression : public ICompressionStrategy {
public:
    void compress(const std::string& file) override {
        std::cout << "Compressing " << file << " as ZIP" << std::endl;
    }
};

class RarCompression : public ICompressionStrategy {
public:
    void compress(const std::string& file) override {
        std::cout << "Compressing " << file << " as RAR" << std::endl;
    }
};

class CompressionContext {
public:
    explicit CompressionContext(std::shared_ptr<ICompressionStrategy> strategy)
        : strategy_(std::move(strategy)) {}

    void execute(const std::string& file) {
        if (strategy_) {
            strategy_->compress(file);
        }
    }

private:
    std::shared_ptr<ICompressionStrategy> strategy_;
};

// 3. COMPOSITE PATTERN
class IGraphicNode {
public:
    virtual ~IGraphicNode() = default;
    virtual void render() = 0;
};

class ShapeLeaf : public IGraphicNode {
public:
    explicit ShapeLeaf(std::string name) : name_(std::move(name)) {}
    void render() override {
        std::cout << "Rendering leaf shape: " << name_ << std::endl;
    }
private:
    std::string name_;
};

class GraphicGroup : public IGraphicNode {
public:
    void add(std::shared_ptr<IGraphicNode> child) {
        children_.push_back(std::move(child));
    }

    void render() override {
        for (const auto& child : children_) {
            child->render();
        }
    }

private:
    std::vector<std::shared_ptr<IGraphicNode>> children_;
};

// 4. BRIDGE / PIMPL IDIOM
class IDisplayBackend {
public:
    virtual ~IDisplayBackend() = default;
    virtual void drawLine(int x1, int y1, int x2, int y2) = 0;
};

class WindowAbstraction {
public:
    explicit WindowAbstraction(std::shared_ptr<IDisplayBackend> backend)
        : backend_(std::move(backend)) {}

    void drawBorder() {
        if (backend_) {
            backend_->drawLine(0, 0, 100, 100);
        }
    }

private:
    std::shared_ptr<IDisplayBackend> backend_;
};

} // namespace patterns
