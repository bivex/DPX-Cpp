# 🔍 Software Design Pattern Detection Report

> **Project:** `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks`  
> **Scanned Files:** 28  
> **Total Detections:** 102  
> **Duration:** 0.057s  

---

## 📊 Summary by Category

| Category | Detections Count |
| :--- | :---: |
| **CREATIONAL** | 2 |
| **BEHAVIORAL** | 1 |
| **ARCHITECTURAL** | 1 |
| **PRINCIPLE** | 98 |

---

## 📋 Identified Design Patterns

### #1 SINGLE_RESPONSIBILITY on god_class_srp_violation `qt_color_sink`
- **Confidence:** 89% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- **Summary:** SRP Violation (God Class): 'qt_color_sink' mixes 3 concerns across 32 methods

#### 🔎 Evidence Trail:
- **+60%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'qt_color_sink' mixes 3 disparate concerns (persistence (2 methods), http_web (2 methods), serialization (4 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`)_
- **+40%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_METHOD_COUNT]` High method count (32 methods) indicates bloated class responsibility _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`)_
- **+25%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_FIELD_COUNT]` High field count (13 fields) suggests multi-purpose state holder _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`)_

---

### #2 KISS on kiss_cyclomatic_complexity `hourly_file_sink::filenames_q_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::filenames_q_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::filenames_q_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #3 KISS on kiss_cyclomatic_complexity `hourly_file_sink::now`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::now' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::now' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #4 KISS on kiss_cyclomatic_complexity `hourly_file_sink::open`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::open' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::open' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #5 KISS on kiss_cyclomatic_complexity `hourly_file_sink::next_rotation_tp_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::next_rotation_tp_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::next_rotation_tp_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #6 KISS on kiss_cyclomatic_complexity `hourly_file_sink::init_filenames_q_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::init_filenames_q_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::init_filenames_q_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #7 KISS on kiss_cyclomatic_complexity `hourly_file_sink::filename`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::filename' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::filename' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #8 KISS on kiss_cyclomatic_complexity `hourly_file_sink::sink_it_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::sink_it_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::sink_it_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #9 KISS on kiss_cyclomatic_complexity `hourly_file_sink::close`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::close' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::close' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #10 KISS on kiss_cyclomatic_complexity `hourly_file_sink::format`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::format' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::format' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #11 KISS on kiss_cyclomatic_complexity `hourly_file_sink::write`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::write' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::write' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #12 KISS on kiss_cyclomatic_complexity `hourly_file_sink::delete_old_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::delete_old_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::delete_old_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #13 KISS on kiss_cyclomatic_complexity `hourly_file_sink::flush_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::flush_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::flush_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #14 KISS on kiss_cyclomatic_complexity `hourly_file_sink::flush`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::flush' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::flush' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #15 KISS on kiss_cyclomatic_complexity `hourly_file_sink::emplace_back`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::emplace_back' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::emplace_back' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #16 KISS on kiss_cyclomatic_complexity `hourly_file_sink::hours`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::hours' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::hours' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #17 KISS on kiss_cyclomatic_complexity `hourly_file_sink::rend`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::rend' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::rend' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #18 KISS on kiss_cyclomatic_complexity `hourly_file_sink::now_tm`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::now_tm' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::now_tm' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #19 KISS on kiss_cyclomatic_complexity `hourly_file_sink::to_time_t`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::to_time_t' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::to_time_t' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #20 KISS on kiss_cyclomatic_complexity `hourly_file_sink::localtime`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::localtime' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::localtime' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #21 KISS on kiss_cyclomatic_complexity `hourly_file_sink::pop_front`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'hourly_file_sink::pop_front' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'hourly_file_sink::pop_front' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #22 KISS on kiss_cyclomatic_complexity `daily_file_sink::filenames_q_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::filenames_q_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::filenames_q_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #23 KISS on kiss_cyclomatic_complexity `daily_file_sink::throw_spdlog_ex`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::throw_spdlog_ex' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::throw_spdlog_ex' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #24 KISS on kiss_cyclomatic_complexity `daily_file_sink::now`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::now' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::now' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #25 KISS on kiss_cyclomatic_complexity `daily_file_sink::open`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::open' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::open' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #26 KISS on kiss_cyclomatic_complexity `daily_file_sink::next_rotation_tp_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::next_rotation_tp_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::next_rotation_tp_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #27 KISS on kiss_cyclomatic_complexity `daily_file_sink::init_filenames_q_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::init_filenames_q_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::init_filenames_q_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #28 KISS on kiss_cyclomatic_complexity `daily_file_sink::filename`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::filename' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::filename' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #29 KISS on kiss_cyclomatic_complexity `daily_file_sink::sink_it_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::sink_it_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::sink_it_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #30 KISS on kiss_cyclomatic_complexity `daily_file_sink::format`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::format' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::format' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #31 KISS on kiss_cyclomatic_complexity `daily_file_sink::write`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::write' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::write' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #32 KISS on kiss_cyclomatic_complexity `daily_file_sink::delete_old_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::delete_old_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::delete_old_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #33 KISS on kiss_cyclomatic_complexity `daily_file_sink::flush_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::flush_' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::flush_' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #34 KISS on kiss_cyclomatic_complexity `daily_file_sink::flush`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::flush' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::flush' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #35 KISS on kiss_cyclomatic_complexity `daily_file_sink::emplace_back`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::emplace_back' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::emplace_back' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #36 KISS on kiss_cyclomatic_complexity `daily_file_sink::hours`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::hours' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::hours' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #37 KISS on kiss_cyclomatic_complexity `daily_file_sink::rend`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::rend' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::rend' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #38 KISS on kiss_cyclomatic_complexity `daily_file_sink::now_tm`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::now_tm' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::now_tm' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #39 KISS on kiss_cyclomatic_complexity `daily_file_sink::to_time_t`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::to_time_t' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::to_time_t' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #40 KISS on kiss_cyclomatic_complexity `daily_file_sink::localtime`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::localtime' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::localtime' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #41 KISS on kiss_cyclomatic_complexity `daily_file_sink::pop_front`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'daily_file_sink::pop_front' has 10 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'daily_file_sink::pop_front' has high cyclomatic complexity (10 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #42 KISS on kiss_cyclomatic_complexity `android_sink::sink_it_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::sink_it_' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::sink_it_' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #43 KISS on kiss_cyclomatic_complexity `android_sink::convert_to_android_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::convert_to_android_' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::convert_to_android_' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #44 KISS on kiss_cyclomatic_complexity `android_sink::append_string_view`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::append_string_view' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::append_string_view' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #45 KISS on kiss_cyclomatic_complexity `android_sink::format`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::format' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::format' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #46 KISS on kiss_cyclomatic_complexity `android_sink::push_back`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::push_back' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::push_back' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #47 KISS on kiss_cyclomatic_complexity `android_sink::data`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::data' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::data' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #48 KISS on kiss_cyclomatic_complexity `android_sink::sleep_for_millis`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::sleep_for_millis' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::sleep_for_millis' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #49 KISS on kiss_cyclomatic_complexity `android_sink::throw_spdlog_ex`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::throw_spdlog_ex' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::throw_spdlog_ex' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #50 KISS on kiss_cyclomatic_complexity `android_sink::flush_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::flush_' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::flush_' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #51 KISS on kiss_cyclomatic_complexity `android_sink::android_log`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::android_log' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::android_log' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #52 KISS on kiss_cyclomatic_complexity `android_sink::__android_log_write`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::__android_log_write' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::__android_log_write' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #53 KISS on kiss_cyclomatic_complexity `android_sink::__android_log_buf_write`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'android_sink::__android_log_buf_write' has 11 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'android_sink::__android_log_buf_write' has high cyclomatic complexity (11 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #54 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::throw_spdlog_ex`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::throw_spdlog_ex' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::throw_spdlog_ex' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #55 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::fdopen`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::fdopen' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::fdopen' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #56 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::close`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::close' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::close' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #57 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::systemd_namespace_sink`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::systemd_namespace_sink' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::systemd_namespace_sink' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #58 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::fclose`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::fclose' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::fclose' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #59 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::sink_it_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::sink_it_' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::sink_it_' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #60 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::format`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::format' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::format' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #61 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::find`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::find' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::find' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #62 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::substr`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::substr' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::substr' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #63 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::write_or_throw_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::write_or_throw_' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::write_or_throw_' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #64 KISS on kiss_cyclomatic_complexity `systemd_namespace_sink::flush_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'systemd_namespace_sink::flush_' has 13 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'systemd_namespace_sink::flush_' has high cyclomatic complexity (13 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #65 KISS on kiss_cyclomatic_complexity `eventlog::get_event_type`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'eventlog::get_event_type' has 8 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'eventlog::get_event_type' has high cyclomatic complexity (8 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

---

### #66 KISS on kiss_cyclomatic_complexity `eventlog::get_event_category`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** KISS Violation (High Complexity): Method 'eventlog::get_event_category' has 8 control flow branches

#### 🔎 Evidence Trail:
- **+70%** `[KISS_KISS_HIGH_CYCLOMATIC_COMPLEXITY]` Method 'eventlog::get_event_category' has high cyclomatic complexity (8 branch points), violating KISS _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[KISS_KISS_DECOMPOSITION_NEEDED]` Complex nested conditionals are difficult to test and maintain; decompose into smaller functions _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

---

### #67 DRY on dry_code_duplication `qt_color_sink::throw_spdlog_ex`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- **Summary:** DRY Violation: Duplicate logic shared across 22 methods (qt_color_sink::throw_spdlog_ex, qt_color_sink::currentCharFormat, qt_color_sink::setForeground, qt_color_sink::setBackground, qt_color_sink::qt_color_sink, qt_color_sink::flush_, qt_color_sink::set_default_color, qt_color_sink::set_level_color, qt_color_sink::get_level_color, qt_color_sink::get_default_color, qt_color_sink::sink_it_, qt_color_sink::size, qt_color_sink::invokeMethod, qt_color_sink::invoke_method_, qt_color_sink::document, qt_color_sink::cursor, qt_color_sink::select, qt_color_sink::removeSelectedText, qt_color_sink::deleteChar, qt_color_sink::movePosition, qt_color_sink::setCharFormat, qt_color_sink::insertText)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 22 methods: qt_color_sink::throw_spdlog_ex, qt_color_sink::currentCharFormat, qt_color_sink::setForeground, qt_color_sink::setBackground, qt_color_sink::qt_color_sink, qt_color_sink::flush_, qt_color_sink::set_default_color, qt_color_sink::set_level_color, qt_color_sink::get_level_color, qt_color_sink::get_default_color, qt_color_sink::sink_it_, qt_color_sink::size, qt_color_sink::invokeMethod, qt_color_sink::invoke_method_, qt_color_sink::document, qt_color_sink::cursor, qt_color_sink::select, qt_color_sink::removeSelectedText, qt_color_sink::deleteChar, qt_color_sink::movePosition, qt_color_sink::setCharFormat, qt_color_sink::insertText _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)

---

### #68 DRY on dry_code_duplication `hourly_file_sink::filenames_q_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 20 methods (hourly_file_sink::filenames_q_, hourly_file_sink::now, hourly_file_sink::open, hourly_file_sink::next_rotation_tp_, hourly_file_sink::init_filenames_q_, hourly_file_sink::filename, hourly_file_sink::sink_it_, hourly_file_sink::close, hourly_file_sink::format, hourly_file_sink::write, hourly_file_sink::delete_old_, hourly_file_sink::flush_, hourly_file_sink::flush, hourly_file_sink::emplace_back, hourly_file_sink::hours, hourly_file_sink::rend, hourly_file_sink::now_tm, hourly_file_sink::to_time_t, hourly_file_sink::localtime, hourly_file_sink::pop_front)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 20 methods: hourly_file_sink::filenames_q_, hourly_file_sink::now, hourly_file_sink::open, hourly_file_sink::next_rotation_tp_, hourly_file_sink::init_filenames_q_, hourly_file_sink::filename, hourly_file_sink::sink_it_, hourly_file_sink::close, hourly_file_sink::format, hourly_file_sink::write, hourly_file_sink::delete_old_, hourly_file_sink::flush_, hourly_file_sink::flush, hourly_file_sink::emplace_back, hourly_file_sink::hours, hourly_file_sink::rend, hourly_file_sink::now_tm, hourly_file_sink::to_time_t, hourly_file_sink::localtime, hourly_file_sink::pop_front _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)

---

### #69 DRY on dry_code_duplication `daily_file_sink::filenames_q_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 20 methods (daily_file_sink::filenames_q_, daily_file_sink::throw_spdlog_ex, daily_file_sink::now, daily_file_sink::open, daily_file_sink::next_rotation_tp_, daily_file_sink::init_filenames_q_, daily_file_sink::filename, daily_file_sink::sink_it_, daily_file_sink::format, daily_file_sink::write, daily_file_sink::delete_old_, daily_file_sink::flush_, daily_file_sink::flush, daily_file_sink::emplace_back, daily_file_sink::hours, daily_file_sink::rend, daily_file_sink::now_tm, daily_file_sink::to_time_t, daily_file_sink::localtime, daily_file_sink::pop_front)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 20 methods: daily_file_sink::filenames_q_, daily_file_sink::throw_spdlog_ex, daily_file_sink::now, daily_file_sink::open, daily_file_sink::next_rotation_tp_, daily_file_sink::init_filenames_q_, daily_file_sink::filename, daily_file_sink::sink_it_, daily_file_sink::format, daily_file_sink::write, daily_file_sink::delete_old_, daily_file_sink::flush_, daily_file_sink::flush, daily_file_sink::emplace_back, daily_file_sink::hours, daily_file_sink::rend, daily_file_sink::now_tm, daily_file_sink::to_time_t, daily_file_sink::localtime, daily_file_sink::pop_front _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)

---

### #70 DRY on dry_code_duplication `ringbuffer_sink::throw_spdlog_ex`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 8 methods (ringbuffer_sink::throw_spdlog_ex, ringbuffer_sink::last_raw, ringbuffer_sink::size, ringbuffer_sink::reserve, ringbuffer_sink::last_formatted, ringbuffer_sink::sink_it_, ringbuffer_sink::push_back, ringbuffer_sink::flush_)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 8 methods: ringbuffer_sink::throw_spdlog_ex, ringbuffer_sink::last_raw, ringbuffer_sink::size, ringbuffer_sink::reserve, ringbuffer_sink::last_formatted, ringbuffer_sink::sink_it_, ringbuffer_sink::push_back, ringbuffer_sink::flush_ _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ringbuffer_sink.h)

---

### #71 DRY on dry_code_duplication `systemd_sink::systemd_sink`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 7 methods (systemd_sink::systemd_sink, systemd_sink::sink_it_, systemd_sink::format, systemd_sink::size, systemd_sink::throw_spdlog_ex, systemd_sink::syslog_level, systemd_sink::flush_)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 7 methods: systemd_sink::systemd_sink, systemd_sink::sink_it_, systemd_sink::format, systemd_sink::size, systemd_sink::throw_spdlog_ex, systemd_sink::syslog_level, systemd_sink::flush_ _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_sink.h)

---

### #72 DRY on dry_code_duplication `dist_sink::add_sink`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 12 methods (dist_sink::add_sink, dist_sink::push_back, dist_sink::remove_sink, dist_sink::set_sinks, dist_sink::move, dist_sink::sinks, dist_sink::sink_it_, dist_sink::log, dist_sink::flush_, dist_sink::flush, dist_sink::set_pattern_, dist_sink::set_formatter_)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 12 methods: dist_sink::add_sink, dist_sink::push_back, dist_sink::remove_sink, dist_sink::set_sinks, dist_sink::move, dist_sink::sinks, dist_sink::sink_it_, dist_sink::log, dist_sink::flush_, dist_sink::flush, dist_sink::set_pattern_, dist_sink::set_formatter_ _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)

---

### #73 DRY on dry_code_duplication `msvc_sink::sink_it_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 4 methods (msvc_sink::sink_it_, msvc_sink::format, msvc_sink::push_back, msvc_sink::flush_)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 4 methods: msvc_sink::sink_it_, msvc_sink::format, msvc_sink::push_back, msvc_sink::flush_ _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/msvc_sink.h)

---

### #74 DRY on dry_code_duplication `android_sink::sink_it_`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 12 methods (android_sink::sink_it_, android_sink::convert_to_android_, android_sink::append_string_view, android_sink::format, android_sink::push_back, android_sink::data, android_sink::sleep_for_millis, android_sink::throw_spdlog_ex, android_sink::flush_, android_sink::android_log, android_sink::__android_log_write, android_sink::__android_log_buf_write)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 12 methods: android_sink::sink_it_, android_sink::convert_to_android_, android_sink::append_string_view, android_sink::format, android_sink::push_back, android_sink::data, android_sink::sleep_for_millis, android_sink::throw_spdlog_ex, android_sink::flush_, android_sink::android_log, android_sink::__android_log_write, android_sink::__android_log_buf_write _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)

---

### #75 DRY on dry_code_duplication `syslog_sink::syslog_sink`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 7 methods (syslog_sink::syslog_sink, syslog_sink::closelog, syslog_sink::sink_it_, syslog_sink::format, syslog_sink::size, syslog_sink::flush_, syslog_sink::syslog_prio_from_level)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 7 methods: syslog_sink::syslog_sink, syslog_sink::closelog, syslog_sink::sink_it_, syslog_sink::format, syslog_sink::size, syslog_sink::flush_, syslog_sink::syslog_prio_from_level _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/syslog_sink.h)

---

### #76 DRY on dry_code_duplication `sid_t::sid_t`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 8 methods (sid_t::sid_t, sid_t::duplicate_sid, sid_t::resize, sid_t::as_sid, sid_t::data, sid_t::get_current_user_sid, sid_t::process_token_t, sid_t::CloseHandle)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 8 methods: sid_t::sid_t, sid_t::duplicate_sid, sid_t::resize, sid_t::as_sid, sid_t::data, sid_t::get_current_user_sid, sid_t::process_token_t, sid_t::CloseHandle _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)

---

### #77 DRY on dry_code_duplication `win_eventlog_sink::event_log_handle`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 9 methods (win_eventlog_sink::event_log_handle, win_eventlog_sink::sink_it_, win_eventlog_sink::format, win_eventlog_sink::push_back, win_eventlog_sink::data, win_eventlog_sink::flush_, win_eventlog_sink::get_current_user_sid, win_eventlog_sink::win_eventlog_sink, win_eventlog_sink::DeregisterEventSource)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 9 methods: win_eventlog_sink::event_log_handle, win_eventlog_sink::sink_it_, win_eventlog_sink::format, win_eventlog_sink::push_back, win_eventlog_sink::data, win_eventlog_sink::flush_, win_eventlog_sink::get_current_user_sid, win_eventlog_sink::win_eventlog_sink, win_eventlog_sink::DeregisterEventSource _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)

---

### #78 DRY on dry_code_duplication `loki_sink::set_keep_alive`
- **Confidence:** 88% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 14 methods (loki_sink::set_keep_alive, loki_sink::set_connection_timeout, loki_sink::set_read_timeout, loki_sink::set_write_timeout, loki_sink::sink_it_, loki_sink::format, loki_sink::Post, loki_sink::throw_spdlog_ex, loki_sink::flush_, loki_sink::set_pattern_, loki_sink::build_json_, loki_sink::count, loki_sink::to_string_view, loki_sink::dump)

#### 🔎 Evidence Trail:
- **+70%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 14 methods: loki_sink::set_keep_alive, loki_sink::set_connection_timeout, loki_sink::set_read_timeout, loki_sink::set_write_timeout, loki_sink::sink_it_, loki_sink::format, loki_sink::Post, loki_sink::throw_spdlog_ex, loki_sink::flush_, loki_sink::set_pattern_, loki_sink::build_json_, loki_sink::count, loki_sink::to_string_view, loki_sink::dump _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)

---

### #79 OPEN_CLOSED on ocp_polymorphic_hierarchy `sink`
- **Confidence:** 87% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h)
- **Summary:** OCP Adherence: Interface 'sink' supports open extension with 4 implementations

#### 🔎 Evidence Trail:
- **+70%** `[OPEN_CLOSED_OCP_POLYMORPHIC_ABSTRACTION]` Abstract interface 'sink' enables open extension through 4 polymorphic implementations: stdout_sink_base, ansicolor_sink, base_sink, wincolor_sink _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h:1:1`)_
- **+35%** `[OPEN_CLOSED_OCP_EXTENSIBLE_DESIGN]` New behaviors can be added by implementing the interface without modifying existing consumers _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/stdout_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/stdout_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ansicolor_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ansicolor_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/base_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/base_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/wincolor_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/wincolor_sink.h)

---

### #80 STRATEGY on protocol_strategy `sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h)
- **Summary:** Strategy pattern: protocol 'sink' with 4 interchangeable concrete implementations

#### 🔎 Evidence Trail:
- **+45%** `[STRATEGY_PROTOCOL_STRATEGY_INTERFACE]` Protocol 'sink' defines strategy interface with methods: log, flush, set_pattern, set_formatter _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink.h:1:1`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'stdout_sink_base' provides concrete strategy implementation for protocol 'sink' _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/stdout_sinks.h:1:1`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'ansicolor_sink' provides concrete strategy implementation for protocol 'sink' _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ansicolor_sink.h:1:1`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'base_sink' provides concrete strategy implementation for protocol 'sink' _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/base_sink.h:1:1`)_
- **+25%** `[STRATEGY_RECORD_STRATEGY_IMPL]` Record 'wincolor_sink' provides concrete strategy implementation for protocol 'sink' _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/wincolor_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/stdout_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/stdout_sinks.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ansicolor_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/ansicolor_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/base_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/base_sink.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/wincolor_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/wincolor_sink.h)

---

### #81 SINGLE_RESPONSIBILITY on god_class_srp_violation `hourly_file_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** SRP Violation (God Class): 'hourly_file_sink' mixes 2 concerns across 30 methods

#### 🔎 Evidence Trail:
- **+50%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'hourly_file_sink' mixes 2 disparate concerns (persistence (2 methods), serialization (1 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+40%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_METHOD_COUNT]` High method count (30 methods) indicates bloated class responsibility _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+25%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_FIELD_COUNT]` High field count (8 fields) suggests multi-purpose state holder _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #82 SINGLE_RESPONSIBILITY on god_class_srp_violation `daily_file_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** SRP Violation (God Class): 'daily_file_sink' mixes 2 concerns across 30 methods

#### 🔎 Evidence Trail:
- **+50%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'daily_file_sink' mixes 2 disparate concerns (persistence (2 methods), serialization (1 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+40%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_METHOD_COUNT]` High method count (30 methods) indicates bloated class responsibility _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+25%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_FIELD_COUNT]` High field count (9 fields) suggests multi-purpose state holder _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #83 INTERFACE_SEGREGATION on fat_interface_isp_violation `hourly_file_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** ISP Violation (Fat Interface): 'hourly_file_sink' has 30 methods; should be split into smaller role interfaces

#### 🔎 Evidence Trail:
- **+65%** `[INTERFACE_SEGREGATION_ISP_FAT_INTERFACE]` Interface 'hourly_file_sink' is a Fat Interface defining 30 methods (filenames_q_, now, open, next_rotation_tp_, init_filenames_q_, filename...), violating ISP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[INTERFACE_SEGREGATION_ISP_UNNEEDED_DEPENDENCY]` Clients and implementors are forced to depend on methods they may not use _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

---

### #84 INTERFACE_SEGREGATION on fat_interface_isp_violation `daily_file_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** ISP Violation (Fat Interface): 'daily_file_sink' has 30 methods; should be split into smaller role interfaces

#### 🔎 Evidence Trail:
- **+65%** `[INTERFACE_SEGREGATION_ISP_FAT_INTERFACE]` Interface 'daily_file_sink' is a Fat Interface defining 30 methods (filenames_q_, throw_spdlog_ex, now, open, next_rotation_tp_, init_filenames_q_...), violating ISP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[INTERFACE_SEGREGATION_ISP_UNNEEDED_DEPENDENCY]` Clients and implementors are forced to depend on methods they may not use _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

---

### #85 INTERFACE_SEGREGATION on fat_interface_isp_violation `android_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h)
- **Summary:** ISP Violation (Fat Interface): 'android_sink' has 14 methods; should be split into smaller role interfaces

#### 🔎 Evidence Trail:
- **+65%** `[INTERFACE_SEGREGATION_ISP_FAT_INTERFACE]` Interface 'android_sink' is a Fat Interface defining 14 methods (sink_it_, convert_to_android_, append_string_view, format, push_back, data...), violating ISP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_
- **+35%** `[INTERFACE_SEGREGATION_ISP_UNNEEDED_DEPENDENCY]` Clients and implementors are forced to depend on methods they may not use _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/android_sink.h:1:1`)_

---

### #86 INTERFACE_SEGREGATION on fat_interface_isp_violation `systemd_namespace_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** ISP Violation (Fat Interface): 'systemd_namespace_sink' has 17 methods; should be split into smaller role interfaces

#### 🔎 Evidence Trail:
- **+65%** `[INTERFACE_SEGREGATION_ISP_FAT_INTERFACE]` Interface 'systemd_namespace_sink' is a Fat Interface defining 17 methods (throw_spdlog_ex, fdopen, close, throw_spdlog_ex, close, throw_spdlog_ex...), violating ISP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+35%** `[INTERFACE_SEGREGATION_ISP_UNNEEDED_DEPENDENCY]` Clients and implementors are forced to depend on methods they may not use _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #87 INTERFACE_SEGREGATION on fat_interface_isp_violation `sid_t`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** ISP Violation (Fat Interface): 'sid_t' has 9 methods; should be split into smaller role interfaces

#### 🔎 Evidence Trail:
- **+65%** `[INTERFACE_SEGREGATION_ISP_FAT_INTERFACE]` Interface 'sid_t' is a Fat Interface defining 9 methods (sid_t, duplicate_sid, resize, as_sid, data, get_current_user_sid...), violating ISP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[INTERFACE_SEGREGATION_ISP_UNNEEDED_DEPENDENCY]` Clients and implementors are forced to depend on methods they may not use _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

---

### #88 INTERFACE_SEGREGATION on fat_interface_isp_violation `loki_sink`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- **Summary:** ISP Violation (Fat Interface): 'loki_sink' has 14 methods; should be split into smaller role interfaces

#### 🔎 Evidence Trail:
- **+65%** `[INTERFACE_SEGREGATION_ISP_FAT_INTERFACE]` Interface 'loki_sink' is a Fat Interface defining 14 methods (set_keep_alive, set_connection_timeout, set_read_timeout, set_write_timeout, sink_it_, format...), violating ISP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`)_
- **+35%** `[INTERFACE_SEGREGATION_ISP_UNNEEDED_DEPENDENCY]` Clients and implementors are forced to depend on methods they may not use _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`)_

---

### #89 DRY on dry_code_duplication `hourly_filename_calculator::calc_filename`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 2 methods (hourly_filename_calculator::calc_filename, hourly_filename_calculator::split_by_extension)

#### 🔎 Evidence Trail:
- **+65%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 2 methods: hourly_filename_calculator::calc_filename, hourly_filename_calculator::split_by_extension _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/hourly_file_sink.h)

---

### #90 DRY on dry_code_duplication `daily_filename_calculator::calc_filename`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 2 methods (daily_filename_calculator::calc_filename, daily_filename_calculator::split_by_extension)

#### 🔎 Evidence Trail:
- **+65%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 2 methods: daily_filename_calculator::calc_filename, daily_filename_calculator::split_by_extension _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)

---

### #91 DRY on dry_code_duplication `daily_filename_format_calculator::calc_filename`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 2 methods (daily_filename_format_calculator::calc_filename, daily_filename_format_calculator::str)

#### 🔎 Evidence Trail:
- **+65%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 2 methods: daily_filename_format_calculator::calc_filename, daily_filename_format_calculator::str _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/daily_file_sink.h)

---

### #92 DRY on dry_code_duplication `dup_filter_sink::sink_it_`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dup_filter_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dup_filter_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 2 methods (dup_filter_sink::sink_it_, dup_filter_sink::filter_)

#### 🔎 Evidence Trail:
- **+65%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 2 methods: dup_filter_sink::sink_it_, dup_filter_sink::filter_ _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dup_filter_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dup_filter_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dup_filter_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dup_filter_sink.h)

---

### #93 DRY on dry_code_duplication `eventlog::get_event_type`
- **Confidence:** 86% (🟢 `VERY_HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** DRY Violation: Duplicate logic shared across 2 methods (eventlog::get_event_type, eventlog::get_event_category)

#### 🔎 Evidence Trail:
- **+65%** `[DRY_DRY_CODE_DUPLICATION]` Identical duplicate code logic detected across 2 methods: eventlog::get_event_type, eventlog::get_event_category _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[DRY_DRY_EXTRACTION_RECOMMENDED]` Duplicate logic creates maintenance hazards when business rules change; extract into shared utility or base class _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)

---

### #94 DEPENDENCY_INVERSION on dip_interface_dependency `dist_sink`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h)
- **Summary:** DIP Adherence: 'dist_sink' depends on interface abstraction(s) (sink)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'dist_sink' depends on abstracted interface(s): sink adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/dist_sink.h:1:1`)_

---

### #95 DEPENDENCY_INVERSION on dip_interface_dependency `win_eventlog_sink`
- **Confidence:** 83% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** DIP Adherence: 'win_eventlog_sink' depends on interface abstraction(s) (ringbuffer_sink)

#### 🔎 Evidence Trail:
- **+60%** `[DEPENDENCY_INVERSION_DIP_INJECTED_ABSTRACTION]` Class 'win_eventlog_sink' depends on abstracted interface(s): ringbuffer_sink adhering to DIP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_
- **+35%** `[DEPENDENCY_INVERSION_DIP_DECOUPLED_ARCHITECTURE]` Core domain logic is decoupled from infrastructure details via Dependency Injection _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

---

### #96 CIRCULAR_DEPENDENCY on namespace_cycle `global ⇄ sinks`
- **Confidence:** 82% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink-inl.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink-inl.h)
- **Summary:** Circular dependency detected between namespaces: global ➔ sinks ➔ global

#### 🔎 Evidence Trail:
- **+45%** `[CIRCULAR_DEPENDENCY_CYCLE_LINK]` Namespace 'global' references 'sinks' creating part of a circular loop _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink-inl.h:1:1`)_
- **+45%** `[CIRCULAR_DEPENDENCY_CYCLE_LINK]` Namespace 'sinks' references 'global' creating part of a circular loop _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`)_

**Related Locations:**
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink-inl.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/sink-inl.h)
- [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/qt_sinks.h)

---

### #97 SINGLE_RESPONSIBILITY on god_class_srp_violation `systemd_namespace_sink`
- **Confidence:** 82% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h)
- **Summary:** SRP Violation (God Class): 'systemd_namespace_sink' mixes 2 concerns across 17 methods

#### 🔎 Evidence Trail:
- **+50%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'systemd_namespace_sink' mixes 2 disparate concerns (persistence (1 methods), serialization (1 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_
- **+40%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_METHOD_COUNT]` High method count (17 methods) indicates bloated class responsibility _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/systemd_namespace_sink.h:1:1`)_

---

### #98 SINGLE_RESPONSIBILITY on god_class_srp_violation `loki_sink`
- **Confidence:** 82% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h)
- **Summary:** SRP Violation (God Class): 'loki_sink' mixes 2 concerns across 14 methods

#### 🔎 Evidence Trail:
- **+50%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'loki_sink' mixes 2 disparate concerns (http_web (1 methods), serialization (2 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`)_
- **+40%** `[SINGLE_RESPONSIBILITY_SRP_HIGH_METHOD_COUNT]` High method count (14 methods) indicates bloated class responsibility _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/loki_sink.h:1:1`)_

---

### #99 SINGLE_RESPONSIBILITY on god_class_srp_violation `sid_t`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** SRP Violation (God Class): 'sid_t' mixes 3 concerns across 9 methods

#### 🔎 Evidence Trail:
- **+60%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'sid_t' mixes 3 disparate concerns (http_web (2 methods), auth_security (2 methods), business_logic (2 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

---

### #100 SINGLE_RESPONSIBILITY on god_class_srp_violation `process_token_t`
- **Confidence:** 76% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h)
- **Summary:** SRP Violation (God Class): 'process_token_t' mixes 3 concerns across 3 methods

#### 🔎 Evidence Trail:
- **+60%** `[SINGLE_RESPONSIBILITY_SRP_MIXED_CONCERNS]` Class 'process_token_t' mixes 3 disparate concerns (http_web (1 methods), auth_security (3 methods), business_logic (3 methods)), violating SRP _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/win_eventlog_sink.h:1:1`)_

---

### #101 SINGLETON on static_singleton_state `mongo_sink::instance`
- **Confidence:** 74% (🔵 `HIGH`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/mongo_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/mongo_sink.h)
- **Summary:** Singleton pattern: static single-instance management for 'mongo_sink::instance'

#### 🔎 Evidence Trail:
- **+60%** `[SINGLETON_STATIC_SINGLETON_INSTANCE]` Static singleton instance managed for 'mongo_sink::instance' _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/mongo_sink.h:1:1`)_

---

### #102 SINGLETON on cpp_singleton_class `mongo_sink`
- **Confidence:** 57% (🟡 `MEDIUM`)
- **Primary Location:** [`/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/mongo_sink.h:1:1`](/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/mongo_sink.h)
- **Summary:** Singleton pattern: class 'mongo_sink' guarantees a single global instance

#### 🔎 Evidence Trail:
- **+35%** `[SINGLETON_STATIC_INSTANCE_FIELD]` Class 'mongo_sink' maintains static instance field _(at `/Volumes/External/Code/DPX-Cpp/tmp_spdlog/include/spdlog/sinks/mongo_sink.h:1:1`)_

---
