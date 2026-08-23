#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <stdexcept>

namespace principles {

// 1. SOLID: SRP Violation (God Object)
class SuperManagerService {
public:
    void calculateSalary() {}
    void generateInvoicePdf() {}
    void sendSlackNotification() {}
    void connectToPostgres() {}
    void flushRedisCache() {}
    void authenticateJwt() {}
    void renderHtmlHeader() {}
    void exportTaxAuditReport() {}
    void dispatchWebhook() {}
    void validateCreditCard() {}
    void syncElasticsearchIndex() {}
    void compressLogArchive() {}
    void restartWorkerPool() {}
    void backupDatabaseToS3() {}
    void parseXmlPayload() {}
    void printFiscalReceipt() {}
};

// 2. SOLID: OCP Violation (dynamic_cast / RTTI cascade)
class ShapeBase {
public:
    virtual ~ShapeBase() = default;
};

class CircleShape : public ShapeBase {};
class SquareShape : public ShapeBase {};
class TriangleShape : public ShapeBase {};

class ShapeAreaCalculator {
public:
    double calculateArea(ShapeBase* shape) {
        if (dynamic_cast<CircleShape*>(shape)) {
            return 3.14 * 10 * 10;
        } else if (dynamic_cast<SquareShape*>(shape)) {
            return 10 * 10;
        } else if (dynamic_cast<TriangleShape*>(shape)) {
            return 0.5 * 10 * 10;
        }
        return 0.0;
    }
};

// 3. SOLID: LSP Violation (Unsupported Exception in derived class)
class ReadOnlyDocument {
public:
    virtual ~ReadOnlyDocument() = default;
    virtual void save() {
        std::cout << "Saving document..." << std::endl;
    }
};

class LockedDocument : public ReadOnlyDocument {
public:
    void save() override {
        throw std::runtime_error("UnsupportedOperation: Document is strictly locked!");
    }
};

// 4. SOLID: ISP Violation (Fat Interface) vs Role Interface
class IUniversalDevice {
public:
    virtual ~IUniversalDevice() = default;
    virtual void printDocument() = 0;
    virtual void scanDocument() = 0;
    virtual void faxDocument() = 0;
    virtual void bindBooklet() = 0;
    virtual void staplePages() = 0;
    virtual void laminatePaper() = 0;
    virtual void sendEmailCopy() = 0;
    virtual void shredOldDocuments() = 0;
    virtual void calibrateSensors() = 0;
};

// 5. SOLID: DIP Violation (Hardcoded concrete dependency)
class SqliteDatabase {
public:
    void query(const std::string& sql) {}
};

class OrderService {
public:
    void placeOrder() {
        auto db = std::make_unique<SqliteDatabase>();
        db->query("INSERT INTO orders VALUES (1)");
    }
};

// 6. KISS Violation: Long Parameter List & Cyclomatic Branching
class PaymentProcessor {
public:
    void processTransaction(
        std::string apiKey,
        std::string accountId,
        double amount,
        std::string currency,
        std::string customerEmail,
        std::string ipAddress,
        int flags
    ) {
        int status = 0;
        if (amount > 0) {
            if (currency == "USD") {
                status = 1;
            } else if (currency == "EUR") {
                status = 2;
            } else if (currency == "GBP") {
                status = 3;
            } else {
                status = 4;
            }
        } else {
            status = -1;
        }
    }
};

// 7. DRY Violation: Duplicate Code Logic
class CustomerDataService {
public:
    std::string formatCustomerRecord(const std::string& id, const std::string& name) {
        std::string header = "HEADER_V1:";
        std::string normalized = name;
        for (auto& c : normalized) c = toupper(c);
        return header + "[" + id + "] " + normalized + " (VALIDATED)";
    }
};

class ClientReportService {
public:
    std::string formatClientRecord(const std::string& id, const std::string& name) {
        std::string header = "HEADER_V1:";
        std::string normalized = name;
        for (auto& c : normalized) c = toupper(c);
        return header + "[" + id + "] " + normalized + " (VALIDATED)";
    }
};

} // namespace principles
