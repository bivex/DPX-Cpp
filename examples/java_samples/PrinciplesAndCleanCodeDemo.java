package com.example.principles;

import java.util.List;
import java.util.ArrayList;

// ============================================================================
// 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP) & CLEAN CODE
// ============================================================================
class OrderReceiptPrinter {
    public void printReceipt(String orderId, double amount) {
        System.out.println("Receipt for Order: " + orderId + " Total: $" + amount);
    }
}

class OrderRepository {
    public void saveOrder(String orderId) {
        System.out.println("Saved order: " + orderId);
    }
}

// ============================================================================
// 2. OPEN/CLOSED PRINCIPLE (OCP)
// ============================================================================
interface TaxCalculator {
    double calculateTax(double amount);
}

class StandardTaxCalculator implements TaxCalculator {
    public double calculateTax(double amount) {
        return amount * 0.20;
    }
}

class ReducedTaxCalculator implements TaxCalculator {
    public double calculateTax(double amount) {
        return amount * 0.07;
    }
}

class ZeroTaxCalculator implements TaxCalculator {
    public double calculateTax(double amount) {
        return 0.0;
    }
}

// ============================================================================
// 3. INTERFACE SEGREGATION PRINCIPLE (ISP)
// ============================================================================
interface Printable {
    void print();
}

interface SerializableEntity {
    String serialize();
}

class InvoiceDocument implements Printable, SerializableEntity {
    public void print() {
        System.out.println("Printing Invoice");
    }

    public String serialize() {
        return "{\"type\": \"invoice\"}";
    }
}

class SummaryDocument implements Printable {
    public void print() {
        System.out.println("Printing Summary");
    }
}

// ============================================================================
// 4. DEPENDENCY INVERSION PRINCIPLE (DIP)
// ============================================================================
interface NotificationGateway {
    void sendNotification(String message);
}

class EmailNotificationGateway implements NotificationGateway {
    public void sendNotification(String message) {
        System.out.println("Email: " + message);
    }
}

class CheckoutService {
    private NotificationGateway notificationGateway;

    public CheckoutService(NotificationGateway notificationGateway) {
        this.notificationGateway = notificationGateway;
    }

    public void completeCheckout(String orderId) {
        notificationGateway.sendNotification("Order " + orderId + " completed!");
    }
}

// ============================================================================
// 5. COMPOSITION OVER INHERITANCE (DELEGATION)
// ============================================================================
class LogEngine {
    public void log(String msg) {
        System.out.println("[LOG] " + msg);
    }
}

class PaymentProcessor {
    private LogEngine logEngine = new LogEngine();

    public void processPayment(double amount) {
        logEngine.log("Processing payment: $" + amount);
    }
}
