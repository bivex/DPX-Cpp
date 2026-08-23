package com.example.patterns.structural;

import java.util.ArrayList;
import java.util.List;

// ============================================================================
// 1. COMPOSITE PATTERN
// ============================================================================
interface GraphicComponent {
    void draw();
}

class DotLeaf implements GraphicComponent {
    private int x;
    private int y;

    public void draw() {
        System.out.println("Drawing Dot at (" + x + "," + y + ")");
    }
}

class CompoundGraphicComposite implements GraphicComponent {
    private List<GraphicComponent> children = new ArrayList<>();

    public void add(GraphicComponent child) {
        children.add(child);
    }

    public void draw() {
        for (GraphicComponent child : children) {
            child.draw();
        }
    }
}

// ============================================================================
// 2. BRIDGE PATTERN
// ============================================================================
interface StorageEngineDriver {
    void writeBytes(String path, byte[] data);
    byte[] readBytes(String path);
}

class DocumentRepository {
    private StorageEngineDriver driver;

    public DocumentRepository(StorageEngineDriver driver) {
        this.driver = driver;
    }

    public void save(String path, byte[] content) {
        driver.writeBytes(path, content);
    }
}
