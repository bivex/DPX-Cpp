# 🔍 Software Design Pattern Detection Report

> **Project:** `/Volumes/External/Code/DPX-Cpp/tmp_real_project`  
> **Scanned Files:** 24  
> **Total Detections:** 78  
> **Duration:** 6.219s  

---

## 📊 Summary by Category

| Category | Detections Count |
| :--- | :---: |
| **CREATIONAL** | 6 |
| **STRUCTURAL** | 1 |
| **BEHAVIORAL** | 25 |
| **PRINCIPLE** | 46 |

---

## 📋 Identified Design Patterns

### #1 ABSTRACT_FACTORY on abstract_factory_protocol `Builder`
- **Confidence:** 89% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- **Summary:** Abstract Factory: protocol 'Builder' declares family of object creation interfaces

#### 🔎 Evidence Trail:
- **+60%** `[ABSTRACT_FACTORY_FACTORY_PROTOCOL_METHODS]` Protocol 'Builder' defines family of 3 creation methods: buildPartA, buildPartB, buildPartC _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_
- **+35%** `[ABSTRACT_FACTORY_FACTORY_PROTOCOL_NAMING]` Protocol 'Builder' follows Abstract Factory naming convention _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_
- **+40%** `[ABSTRACT_FACTORY_CONCRETE_FACTORY_RECORDS]` Implemented by 2 concrete factory record(s): ConcreteBuilderX, ConcreteBuilderY _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:73:1-89:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:73:1-89:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:91:1-107:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)

---

### #2 ABSTRACT_FACTORY on abstract_factory_protocol `AbstractFactory`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** Abstract Factory: protocol 'AbstractFactory' declares family of object creation interfaces

#### 🔎 Evidence Trail:
- **+55%** `[ABSTRACT_FACTORY_FACTORY_PROTOCOL_METHODS]` Protocol 'AbstractFactory' defines family of 2 creation methods: createProductA, createProductB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_
- **+35%** `[ABSTRACT_FACTORY_FACTORY_PROTOCOL_NAMING]` Protocol 'AbstractFactory' follows Abstract Factory naming convention _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_
- **+40%** `[ABSTRACT_FACTORY_CONCRETE_FACTORY_RECORDS]` Implemented by 2 concrete factory record(s): ConcreteFactoryX, ConcreteFactoryY _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:115:1-129:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:115:1-129:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:131:1-145:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #3 COMPOSITE on composite_hierarchy `Component`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- **Summary:** Composite pattern: protocol 'Component' unifies leaf and composite container records in part-whole hierarchy

#### 🔎 Evidence Trail:
- **+50%** `[COMPOSITE_COMPOSITE_PROTOCOL]` Protocol 'Component' defines uniform component interface for both leaves and containers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`)_
- **+45%** `[COMPOSITE_COMPOSITE_CONTAINER_RECORDS]` Identified composite container record(s) holding child hierarchies: Composite _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:40:1-78:2`)_
- **+35%** `[COMPOSITE_LEAF_ELEMENT_RECORDS]` Identified leaf element record(s): ConcreteComponent, Decorator, Leaf _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:32:1-42:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:40:1-78:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:85:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)

---

### #4 OPEN_CLOSED on ocp_polymorphic_hierarchy `Subject`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)
- **Summary:** OCP Adherence: Interface 'Subject' supports open extension with 3 implementations

#### 🔎 Evidence Trail:
- **+70%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Subject' enables open extension through 3 polymorphic implementations: RealSubject, Proxy, ConcreteSubject _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:31:1-39:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)

---

### #5 OPEN_CLOSED on ocp_polymorphic_hierarchy `Component`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- **Summary:** OCP Adherence: Interface 'Component' supports open extension with 4 implementations

#### 🔎 Evidence Trail:
- **+70%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Component' enables open extension through 4 polymorphic implementations: ConcreteComponent, Decorator, Composite, Leaf _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:40:1-78:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:85:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)

---

### #6 OPEN_CLOSED on ocp_polymorphic_hierarchy `Strategy`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- **Summary:** OCP Adherence: Interface 'Strategy' supports open extension with 3 implementations

#### 🔎 Evidence Trail:
- **+70%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Strategy' enables open extension through 3 polymorphic implementations: ConcreteStrategyA, ConcreteStrategyB, ConcreteStrategyC _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:29:1-39:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:41:1-51:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:53:1-63:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)

---

### #7 STRATEGY on protocol_strategy `Component`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- **Summary:** Strategy pattern: protocol 'Component' with 4 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Component' defines strategy interface with methods: operation _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteComponent' provides concrete strategy implementation for protocol 'Component' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:32:1-42:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'Decorator' provides concrete strategy implementation for protocol 'Component' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'Composite' provides concrete strategy implementation for protocol 'Component' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:40:1-78:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'Leaf' provides concrete strategy implementation for protocol 'Component' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:85:1-99:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:40:1-78:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:85:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)

---

### #8 ABSTRACT_FACTORY on abstract_factory_protocol `Creator`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:65:1-76:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- **Summary:** Abstract Factory: protocol 'Creator' declares family of object creation interfaces

#### 🔎 Evidence Trail:
- **+55%** `[ABSTRACT_FACTORY_FACTORY_PROTOCOL_METHODS]` Protocol 'Creator' defines family of 2 creation methods: createProductA, createProductB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:65:1-76:2`)_
- **+35%** `[ABSTRACT_FACTORY_FACTORY_PROTOCOL_NAMING]` Protocol 'Creator' follows Abstract Factory naming convention _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:65:1-76:2`)_
- **+30%** `[ABSTRACT_FACTORY_CONCRETE_FACTORY_RECORDS]` Implemented by 1 concrete factory record(s): ConcreteCreator _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:84:1-104:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:84:1-104:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)

---

### #9 OPEN_CLOSED on ocp_polymorphic_hierarchy `Product`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- **Summary:** OCP Adherence: Interface 'Product' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Product' enables open extension through 2 polymorphic implementations: ConcreteProductA, ConcreteProductB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:48:1-58:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)

---

### #10 OPEN_CLOSED on ocp_polymorphic_hierarchy `Implementor`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- **Summary:** OCP Adherence: Interface 'Implementor' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Implementor' enables open extension through 2 polymorphic implementations: ConcreteImplementorA, ConcreteImplementorB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:30:1-40:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:42:1-52:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)

---

### #11 OPEN_CLOSED on ocp_polymorphic_hierarchy `Prototype`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- **Summary:** OCP Adherence: Interface 'Prototype' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Prototype' enables open extension through 2 polymorphic implementations: ConcretePrototypeA, ConcretePrototypeB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:32:1-46:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:48:1-62:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)

---

### #12 OPEN_CLOSED on ocp_polymorphic_hierarchy `State`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)
- **Summary:** OCP Adherence: Interface 'State' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'State' enables open extension through 2 polymorphic implementations: ConcreteStateA, ConcreteStateB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:31:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:43:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)

---

### #13 OPEN_CLOSED on ocp_polymorphic_hierarchy `Visitor`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** OCP Adherence: Interface 'Visitor' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Visitor' enables open extension through 2 polymorphic implementations: ConcreteVisitor1, ConcreteVisitor2 _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:38:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:55:1-70:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #14 OPEN_CLOSED on ocp_polymorphic_hierarchy `Element`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** OCP Adherence: Interface 'Element' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Element' enables open extension through 2 polymorphic implementations: ConcreteElementA, ConcreteElementB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:89:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:101:1-111:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #15 OPEN_CLOSED on ocp_polymorphic_hierarchy `ProductA`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** OCP Adherence: Interface 'ProductA' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'ProductA' enables open extension through 2 polymorphic implementations: ConcreteProductAX, ConcreteProductAY _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:31:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:43:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #16 OPEN_CLOSED on ocp_polymorphic_hierarchy `ProductB`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** OCP Adherence: Interface 'ProductB' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'ProductB' enables open extension through 2 polymorphic implementations: ConcreteProductBX, ConcreteProductBY _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:73:1-83:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:85:1-95:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #17 OPEN_CLOSED on ocp_polymorphic_hierarchy `AbstractFactory`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** OCP Adherence: Interface 'AbstractFactory' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'AbstractFactory' enables open extension through 2 polymorphic implementations: ConcreteFactoryX, ConcreteFactoryY _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:115:1-129:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:131:1-145:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #18 OPEN_CLOSED on ocp_polymorphic_hierarchy `Handler`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)
- **Summary:** OCP Adherence: Interface 'Handler' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Handler' enables open extension through 2 polymorphic implementations: ConcreteHandler1, ConcreteHandler2 _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:44:1-69:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:71:1-97:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)

---

### #19 OPEN_CLOSED on ocp_polymorphic_hierarchy `Flyweight`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- **Summary:** OCP Adherence: Interface 'Flyweight' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Flyweight' enables open extension through 2 polymorphic implementations: UnsharedConcreteFlyweight, ConcreteFlyweight _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)

---

### #20 OPEN_CLOSED on ocp_polymorphic_hierarchy `Builder`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- **Summary:** OCP Adherence: Interface 'Builder' supports open extension with 2 implementations

#### 🔎 Evidence Trail:
- **+60%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'Builder' enables open extension through 2 polymorphic implementations: ConcreteBuilderX, ConcreteBuilderY _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:73:1-89:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:91:1-107:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)

---

### #21 DEPENDENCY_INVERSION on dip_interface_dependency `Context`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:69:1-88:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- **Summary:** DIP Adherence: 'Context' depends on interface abstraction(s) (Strategy)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Context' depends on abstracted interface(s): Strategy adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:69:1-88:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:69:1-88:2`)_

---

### #22 DEPENDENCY_INVERSION on dip_interface_dependency `Subject`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)
- **Summary:** DIP Adherence: 'Subject' depends on interface abstraction(s) (Observer)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Subject' depends on abstracted interface(s): Observer adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_

---

### #23 DEPENDENCY_INVERSION on dip_interface_dependency `Proxy`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- **Summary:** DIP Adherence: 'Proxy' depends on interface abstraction(s) (Subject)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Proxy' depends on abstracted interface(s): Subject adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`)_

---

### #24 DEPENDENCY_INVERSION on dip_interface_dependency `Decorator`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- **Summary:** DIP Adherence: 'Decorator' depends on interface abstraction(s) (Component)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Decorator' depends on abstracted interface(s): Component adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`)_

---

### #25 DEPENDENCY_INVERSION on dip_interface_dependency `RefinedAbstraction`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:71:1-86:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- **Summary:** DIP Adherence: 'RefinedAbstraction' depends on interface abstraction(s) (Implementor)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'RefinedAbstraction' depends on abstracted interface(s): Implementor adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:71:1-86:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:71:1-86:2`)_

---

### #26 DEPENDENCY_INVERSION on dip_interface_dependency `ConcreteObserver`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:36:1-55:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)
- **Summary:** DIP Adherence: 'ConcreteObserver' depends on interface abstraction(s) (Observer, State)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'ConcreteObserver' depends on abstracted interface(s): Observer, State adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:36:1-55:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:36:1-55:2`)_

---

### #27 DEPENDENCY_INVERSION on dip_interface_dependency `ConcreteSubject`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)
- **Summary:** DIP Adherence: 'ConcreteSubject' depends on interface abstraction(s) (State, Subject)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'ConcreteSubject' depends on abstracted interface(s): State, Subject adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`)_

---

### #28 DEPENDENCY_INVERSION on dip_interface_dependency `Memento`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:19:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- **Summary:** DIP Adherence: 'Memento' depends on interface abstraction(s) (State)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Memento' depends on abstracted interface(s): State adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:19:1-41:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:19:1-41:2`)_

---

### #29 DEPENDENCY_INVERSION on dip_interface_dependency `Originator`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:48:1-77:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- **Summary:** DIP Adherence: 'Originator' depends on interface abstraction(s) (State)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Originator' depends on abstracted interface(s): State adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:48:1-77:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:48:1-77:2`)_

---

### #30 DEPENDENCY_INVERSION on dip_interface_dependency `Invoker`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:76:1-96:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp)
- **Summary:** DIP Adherence: 'Invoker' depends on interface abstraction(s) (Command)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Invoker' depends on abstracted interface(s): Command adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:76:1-96:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:76:1-96:2`)_

---

### #31 DEPENDENCY_INVERSION on dip_interface_dependency `UnsharedConcreteFlyweight`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- **Summary:** DIP Adherence: 'UnsharedConcreteFlyweight' depends on interface abstraction(s) (State)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'UnsharedConcreteFlyweight' depends on abstracted interface(s): State adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`)_

---

### #32 DEPENDENCY_INVERSION on dip_interface_dependency `ConcreteFlyweight`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- **Summary:** DIP Adherence: 'ConcreteFlyweight' depends on interface abstraction(s) (State)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'ConcreteFlyweight' depends on abstracted interface(s): State adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`)_

---

### #33 DEPENDENCY_INVERSION on dip_interface_dependency `Builder`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- **Summary:** DIP Adherence: 'Builder' depends on interface abstraction(s) (Product, ProductA, ProductB)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Builder' depends on abstracted interface(s): Product, ProductA, ProductB adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_

---

### #34 DEPENDENCY_INVERSION on dip_interface_dependency `Director`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:113:1-150:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- **Summary:** DIP Adherence: 'Director' depends on interface abstraction(s) (Builder)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Director' depends on abstracted interface(s): Builder adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:113:1-150:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:113:1-150:2`)_

---

### #35 DEPENDENCY_INVERSION on dip_interface_dependency `Colleague`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:22:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp)
- **Summary:** DIP Adherence: 'Colleague' depends on interface abstraction(s) (Mediator)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'Colleague' depends on abstracted interface(s): Mediator adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:22:1-41:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:22:1-41:2`)_

---

### #36 DEPENDENCY_INVERSION on dip_interface_dependency `ConcreteMediator`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp)
- **Summary:** DIP Adherence: 'ConcreteMediator' depends on interface abstraction(s) (Colleague)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'ConcreteMediator' depends on abstracted interface(s): Colleague adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`)_

---

### #37 MEDIATOR on mediator_protocol `Mediator`
- **Confidence:** 82% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:63:1-73:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp)
- **Summary:** Mediator pattern: protocol 'Mediator' acts as central event/message broker decoupling components

#### 🔎 Evidence Trail:
- **+60%** `[MEDIATOR_MEDIATOR_PROTOCOL]` Protocol 'Mediator' defines central mediator message coordination methods: add, distribute _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:63:1-73:2`)_
- **+35%** `[MEDIATOR_MEDIATOR_RECORD_IMPL]` Implemented by concrete mediator hub record(s): ConcreteMediator _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp)

---

### #38 STRATEGY on protocol_strategy `Subject`
- **Confidence:** 81% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)
- **Summary:** Strategy pattern: protocol 'Subject' with 3 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Subject' defines strategy interface with methods: getState, setState _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'RealSubject' provides concrete strategy implementation for protocol 'Subject' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:31:1-39:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'Proxy' provides concrete strategy implementation for protocol 'Subject' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteSubject' provides concrete strategy implementation for protocol 'Subject' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:31:1-39:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)

---

### #39 STRATEGY on protocol_strategy `Strategy`
- **Confidence:** 81% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- **Summary:** Strategy pattern: protocol 'Strategy' with 3 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Strategy' defines strategy interface with methods: algorithmInterface _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteStrategyA' provides concrete strategy implementation for protocol 'Strategy' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:29:1-39:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteStrategyB' provides concrete strategy implementation for protocol 'Strategy' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:41:1-51:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteStrategyC' provides concrete strategy implementation for protocol 'Strategy' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:53:1-63:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:29:1-39:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:41:1-51:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:53:1-63:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)

---

### #40 PROTOTYPE on prototype_protocol `Prototype`
- **Confidence:** 80% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- **Summary:** Prototype pattern: protocol 'Prototype' defines instance cloning and derivation interface

#### 🔎 Evidence Trail:
- **+55%** `[PROTOTYPE_PROTOTYPE_PROTOCOL]` Protocol 'Prototype' defines prototype cloning methods: clone, type _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`)_
- **+35%** `[PROTOTYPE_CONCRETE_PROTOTYPES]` Implemented by 2 prototype records: ConcretePrototypeA, ConcretePrototypeB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:32:1-46:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:32:1-46:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:48:1-62:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)

---

### #41 VISITOR on visitor_interface `Visitor`
- **Confidence:** 80% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** Visitor pattern: 'Visitor' defines double-dispatch visitor operations over element hierarchy

#### 🔎 Evidence Trail:
- **+56%** `[VISITOR_VISITOR_INTERFACE_METHODS]` Interface 'Visitor' defines Visitor contract with 2 visit() method overload(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`)_
- **+30%** `[VISITOR_CONCRETE_VISITOR_IMPLEMENTATIONS]` Concrete visitor classes implemented: ConcreteVisitor1, ConcreteVisitor2 _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:38:1-53:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:38:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:55:1-70:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #42 VISITOR on element_accept_method `ConcreteElementA.ConcreteElementA::accept`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:94:3-97:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** Visitor Element: 'ConcreteElementA' participates in visitor double-dispatch via accept()

#### 🔎 Evidence Trail:
- **+65%** `[VISITOR_ELEMENT_ACCEPT_DOUBLE_DISPATCH]` Class 'ConcreteElementA' implements double-dispatch accept() method delegating to visitor.visit(this) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:94:3-97:4`)_

---

### #43 VISITOR on element_accept_method `ConcreteElementB.ConcreteElementB::accept`
- **Confidence:** 77% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:106:3-109:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** Visitor Element: 'ConcreteElementB' participates in visitor double-dispatch via accept()

#### 🔎 Evidence Trail:
- **+65%** `[VISITOR_ELEMENT_ACCEPT_DOUBLE_DISPATCH]` Class 'ConcreteElementB' implements double-dispatch accept() method delegating to visitor.visit(this) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:106:3-109:4`)_

---

### #44 STRATEGY on protocol_strategy `Product`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- **Summary:** Strategy pattern: protocol 'Product' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Product' defines strategy interface with methods: getName _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteProductA' provides concrete strategy implementation for protocol 'Product' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:32:1-42:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteProductB' provides concrete strategy implementation for protocol 'Product' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:48:1-58:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:48:1-58:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)

---

### #45 STRATEGY on protocol_strategy `Implementor`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- **Summary:** Strategy pattern: protocol 'Implementor' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Implementor' defines strategy interface with methods: action _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteImplementorA' provides concrete strategy implementation for protocol 'Implementor' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:30:1-40:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteImplementorB' provides concrete strategy implementation for protocol 'Implementor' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:42:1-52:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:30:1-40:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:42:1-52:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)

---

### #46 STRATEGY on protocol_strategy `Prototype`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- **Summary:** Strategy pattern: protocol 'Prototype' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Prototype' defines strategy interface with methods: clone, type _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcretePrototypeA' provides concrete strategy implementation for protocol 'Prototype' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:32:1-46:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcretePrototypeB' provides concrete strategy implementation for protocol 'Prototype' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:48:1-62:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:32:1-46:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:48:1-62:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)

---

### #47 STRATEGY on protocol_strategy `State`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)
- **Summary:** Strategy pattern: protocol 'State' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'State' defines strategy interface with methods: handle _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteStateA' provides concrete strategy implementation for protocol 'State' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:31:1-41:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteStateB' provides concrete strategy implementation for protocol 'State' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:43:1-53:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:31:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:43:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)

---

### #48 STRATEGY on protocol_strategy `Visitor`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** Strategy pattern: protocol 'Visitor' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Visitor' defines strategy interface with methods: visitElementA, visitElementB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteVisitor1' provides concrete strategy implementation for protocol 'Visitor' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:38:1-53:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteVisitor2' provides concrete strategy implementation for protocol 'Visitor' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:55:1-70:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:38:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:55:1-70:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #49 STRATEGY on protocol_strategy `Element`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** Strategy pattern: protocol 'Element' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Element' defines strategy interface with methods: accept _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteElementA' provides concrete strategy implementation for protocol 'Element' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:89:1-99:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteElementB' provides concrete strategy implementation for protocol 'Element' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:101:1-111:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:89:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:101:1-111:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #50 STRATEGY on protocol_strategy `ProductA`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** Strategy pattern: protocol 'ProductA' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'ProductA' defines strategy interface with methods: getName _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteProductAX' provides concrete strategy implementation for protocol 'ProductA' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:31:1-41:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteProductAY' provides concrete strategy implementation for protocol 'ProductA' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:43:1-53:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:31:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:43:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #51 STRATEGY on protocol_strategy `ProductB`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** Strategy pattern: protocol 'ProductB' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'ProductB' defines strategy interface with methods: getName _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteProductBX' provides concrete strategy implementation for protocol 'ProductB' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:73:1-83:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteProductBY' provides concrete strategy implementation for protocol 'ProductB' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:85:1-95:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:73:1-83:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:85:1-95:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #52 STRATEGY on protocol_strategy `AbstractFactory`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** Strategy pattern: protocol 'AbstractFactory' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'AbstractFactory' defines strategy interface with methods: createProductA, createProductB _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteFactoryX' provides concrete strategy implementation for protocol 'AbstractFactory' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:115:1-129:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteFactoryY' provides concrete strategy implementation for protocol 'AbstractFactory' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:131:1-145:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:115:1-129:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:131:1-145:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #53 STRATEGY on protocol_strategy `Handler`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)
- **Summary:** Strategy pattern: protocol 'Handler' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Handler' defines strategy interface with methods: ~Handler, setHandler, handleRequest _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteHandler1' provides concrete strategy implementation for protocol 'Handler' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:44:1-69:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteHandler2' provides concrete strategy implementation for protocol 'Handler' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:71:1-97:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:44:1-69:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:71:1-97:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)

---

### #54 STRATEGY on protocol_strategy `Flyweight`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- **Summary:** Strategy pattern: protocol 'Flyweight' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Flyweight' defines strategy interface with methods: operation _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'UnsharedConcreteFlyweight' provides concrete strategy implementation for protocol 'Flyweight' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteFlyweight' provides concrete strategy implementation for protocol 'Flyweight' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)

---

### #55 STRATEGY on protocol_strategy `Builder`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- **Summary:** Strategy pattern: protocol 'Builder' with 2 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'Builder' defines strategy interface with methods: buildPartA, buildPartB, buildPartC _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteBuilderX' provides concrete strategy implementation for protocol 'Builder' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:73:1-89:2`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ConcreteBuilderY' provides concrete strategy implementation for protocol 'Builder' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:91:1-107:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:73:1-89:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:91:1-107:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)

---

### #56 COMMAND on command_protocol `Abstraction`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:58:1-65:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- **Summary:** Command pattern: protocol 'Abstraction' implemented by 1 command records

#### 🔎 Evidence Trail:
- **+50%** `[COMMAND_COMMAND_PROTOCOL]` Protocol 'Abstraction' defines Command interface with methods: operation _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:58:1-65:2`)_
- **+30%** `[COMMAND_COMMAND_RECORD]` Record 'RefinedAbstraction' encapsulates executable command parameters and behavior _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:71:1-86:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:71:1-86:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)

---

### #57 COMMAND on command_protocol `Command`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:32:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp)
- **Summary:** Command pattern: protocol 'Command' implemented by 1 command records

#### 🔎 Evidence Trail:
- **+50%** `[COMMAND_COMMAND_PROTOCOL]` Protocol 'Command' defines Command interface with methods: execute _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:32:1-41:2`)_
- **+30%** `[COMMAND_COMMAND_RECORD]` Record 'ConcreteCommand' encapsulates executable command parameters and behavior _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:48:1-70:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp:48:1-70:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/command/Command.cpp)

---

### #58 ITERATOR on iterator_protocol `Iterator`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/iterator/Iterator.cpp:76:1-86:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/iterator/Iterator.cpp)
- **Summary:** Iterator pattern: protocol 'Iterator' defines sequential iteration contract

#### 🔎 Evidence Trail:
- **+65%** `[ITERATOR_ITERATOR_PROTOCOL]` Protocol 'Iterator' defines iterator traversal methods: first, next, isDone, currentItem _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/iterator/Iterator.cpp:76:1-86:2`)_

---

### #59 MEDIATOR on mediator_hub_record `Mediator`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:63:1-73:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp)
- **Summary:** Mediator pattern: record 'Mediator' mediates communication between decoupled subsystems

#### 🔎 Evidence Trail:
- **+65%** `[MEDIATOR_MEDIATOR_RECORD]` Record 'Mediator' encapsulates centralized mediator broker state and subscriber registry _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:63:1-73:2`)_

---

### #60 MEDIATOR on mediator_hub_record `ConcreteMediator`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp)
- **Summary:** Mediator pattern: record 'ConcreteMediator' mediates communication between decoupled subsystems

#### 🔎 Evidence Trail:
- **+65%** `[MEDIATOR_MEDIATOR_RECORD]` Record 'ConcreteMediator' encapsulates centralized mediator broker state and subscriber registry _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/mediator/Mediator.cpp:80:1-110:2`)_

---

### #61 MEMENTO on memento_history_manager `Memento::Memento`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:25:3`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- **Summary:** Memento pattern: snapshot & history management in namespace 'global' (6 functions)

#### 🔎 Evidence Trail:
- **+65%** `[MEMENTO_MEMENTO_SNAPSHOT_FNS]` Namespace 'global' defines 6 state snapshot/restore functions: Memento::Memento, Memento::setState, Memento::getState, Originator::setMemento, Originator::*createMemento, CareTaker::undo _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:25:3`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:25:3`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:27:3-30:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:32:3-35:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:64:3-67:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:69:3-72:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp:103:3-117:4`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/memento/Memento.cpp)

---

### #62 INTERFACE_SEGREGATION on segregated_role_interface `Subject`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)
- **Summary:** ISP Adherence: Role interface 'Subject' is segregated and focused (2 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Subject' follows ISP as a cohesive role interface with only 2 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 3 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:62:1-92:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:31:1-39:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp:45:1-66:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/proxy/Proxy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp:98:1-117:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/observer/Observer.cpp)

---

### #63 INTERFACE_SEGREGATION on segregated_role_interface `Component`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- **Summary:** ISP Adherence: Role interface 'Component' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Component' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 4 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:19:1-33:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp:49:1-64:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/decorator/Decorator.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:40:1-78:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp:85:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/composite/Composite.cpp)

---

### #64 INTERFACE_SEGREGATION on segregated_role_interface `Product`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- **Summary:** ISP Adherence: Role interface 'Product' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Product' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:19:1-26:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:32:1-42:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp:48:1-58:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/factory-method/FactoryMethod.cpp)

---

### #65 INTERFACE_SEGREGATION on segregated_role_interface `Implementor`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- **Summary:** ISP Adherence: Role interface 'Implementor' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Implementor' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:17:1-24:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:30:1-40:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp:42:1-52:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/bridge/Bridge.cpp)

---

### #66 INTERFACE_SEGREGATION on segregated_role_interface `Prototype`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- **Summary:** ISP Adherence: Role interface 'Prototype' is segregated and focused (2 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Prototype' follows ISP as a cohesive role interface with only 2 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:18:1-26:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:32:1-46:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp:48:1-62:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/prototype/Prototype.cpp)

---

### #67 INTERFACE_SEGREGATION on segregated_role_interface `State`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)
- **Summary:** ISP Adherence: Role interface 'State' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'State' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:18:1-24:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:31:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp:43:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/state/State.cpp)

---

### #68 INTERFACE_SEGREGATION on segregated_role_interface `Visitor`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** ISP Adherence: Role interface 'Visitor' is segregated and focused (2 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Visitor' follows ISP as a cohesive role interface with only 2 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:22:1-30:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:38:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:55:1-70:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #69 INTERFACE_SEGREGATION on segregated_role_interface `Element`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- **Summary:** ISP Adherence: Role interface 'Element' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Element' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:76:1-83:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:89:1-99:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp:101:1-111:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/visitor/Visitor.cpp)

---

### #70 INTERFACE_SEGREGATION on segregated_role_interface `ProductA`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** ISP Adherence: Role interface 'ProductA' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'ProductA' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:18:1-25:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:31:1-41:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:43:1-53:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #71 INTERFACE_SEGREGATION on segregated_role_interface `ProductB`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** ISP Adherence: Role interface 'ProductB' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'ProductB' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:60:1-67:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:73:1-83:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:85:1-95:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #72 INTERFACE_SEGREGATION on segregated_role_interface `AbstractFactory`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- **Summary:** ISP Adherence: Role interface 'AbstractFactory' is segregated and focused (2 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'AbstractFactory' follows ISP as a cohesive role interface with only 2 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:101:1-108:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:115:1-129:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp:131:1-145:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/abstract-factory/AbstractFactory.cpp)

---

### #73 INTERFACE_SEGREGATION on segregated_role_interface `Handler`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)
- **Summary:** ISP Adherence: Role interface 'Handler' is segregated and focused (3 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Handler' follows ISP as a cohesive role interface with only 3 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:17:1-38:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:44:1-69:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp:71:1-97:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/chain-of-responsibility/ChainOfResponsibility.cpp)

---

### #74 INTERFACE_SEGREGATION on segregated_role_interface `Flyweight`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- **Summary:** ISP Adherence: Role interface 'Flyweight' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Flyweight' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:19:1-25:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:31:1-48:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp:55:1-72:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/flyweight/Flyweight.cpp)

---

### #75 INTERFACE_SEGREGATION on segregated_role_interface `Builder`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- **Summary:** ISP Adherence: Role interface 'Builder' is segregated and focused (3 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Builder' follows ISP as a cohesive role interface with only 3 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 2 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:50:1-67:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:73:1-89:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp:91:1-107:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/builder/Builder.cpp)

---

### #76 INTERFACE_SEGREGATION on segregated_role_interface `Strategy`
- **Confidence:** 75% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- **Summary:** ISP Adherence: Role interface 'Strategy' is segregated and focused (1 methods)

#### 🔎 Evidence Trail:
- **+50%** `[INTERFACE_SEGREGATION_ISP_ROLE_INTERFACE]` Interface 'Strategy' follows ISP as a cohesive role interface with only 1 method(s) _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`)_
- **+30%** `[INTERFACE_SEGREGATION_ISP_CLEAN_IMPLEMENTATION]` Implemented by 3 targeted classes without bloated contract obligations _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:17:1-23:2`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:29:1-39:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:41:1-51:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)
- [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp:53:1-63:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/strategy/Strategy.cpp)

---

### #77 SINGLETON on static_singleton_state `Singleton::instance`
- **Confidence:** 74% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/singleton/Singleton.cpp:56:3`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/singleton/Singleton.cpp)
- **Summary:** Singleton pattern: static single-instance management for 'Singleton::instance'

#### 🔎 Evidence Trail:
- **+60%** `[SINGLETON_STATIC_SINGLETON_INSTANCE]` Static singleton instance managed for 'Singleton::instance' _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/singleton/Singleton.cpp:56:3`)_

---

### #78 SINGLETON on cpp_singleton_class `Singleton`
- **Confidence:** 57% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_real_project/singleton/Singleton.cpp:18:1-58:2`](/Volumes/External/Code/DPX-Cpp/tmp_real_project/singleton/Singleton.cpp)
- **Summary:** Singleton pattern: class 'Singleton' guarantees a single global instance

#### 🔎 Evidence Trail:
- **+35%** `[SINGLETON_STATIC_INSTANCE_FIELD]` Class 'Singleton' maintains static instance field _(at `/Volumes/External/Code/DPX-Cpp/tmp_real_project/singleton/Singleton.cpp:18:1-58:2`)_

---
