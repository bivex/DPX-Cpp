package com.example.patterns.creational;

// ============================================================================
// 1. SINGLETON PATTERN
// ============================================================================
class DatabaseConnectionPool {
    private static final DatabaseConnectionPool INSTANCE = new DatabaseConnectionPool();

    private DatabaseConnectionPool() {}

    public static DatabaseConnectionPool getInstance() {
        return INSTANCE;
    }
}

// ============================================================================
// 2. ABSTRACT FACTORY PATTERN
// ============================================================================
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

interface Button {
    void render();
}

interface Checkbox {
    void check();
}

class WindowsButton implements Button {
    public void render() {
        System.out.println("Rendering Windows Button");
    }
}

class WindowsCheckbox implements Checkbox {
    public void check() {
        System.out.println("Checking Windows Checkbox");
    }
}

class WindowsGUIFactory implements GUIFactory {
    public Button createButton() {
        return new WindowsButton();
    }

    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}
