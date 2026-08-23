package com.example.patterns.behavioral;

// ============================================================================
// 1. STRATEGY PATTERN
// ============================================================================
interface PaymentStrategy {
    void pay(int amount);
}

class CreditCardStrategy implements PaymentStrategy {
    public void pay(int amount) {
        System.out.println("Paid " + amount + " via Credit Card");
    }
}

class CryptoStrategy implements PaymentStrategy {
    public void pay(int amount) {
        System.out.println("Paid " + amount + " via Crypto");
    }
}

// ============================================================================
// 2. MEDIATOR PATTERN
// ============================================================================
interface EventBroker {
    void publish(String topic, Object event);
    void subscribe(String topic, Object handler);
}

class CentralMessageHub implements EventBroker {
    public void publish(String topic, Object event) {}
    public void subscribe(String topic, Object handler) {}
}
