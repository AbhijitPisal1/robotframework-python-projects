```markdown
# Robot Framework Command Cheatsheet

A quick reference guide for executing Robot Framework test suites, using tags, variables, parallel execution, and generating reports/logs.

---

## 📘 About Robot Framework

Robot Framework is an **open-source, keyword-driven test automation framework** designed for acceptance testing and RPA (Robotic Process Automation).

- Simple **tabular syntax**
- Accessible to testers with **minimal programming knowledge**
- Supports a wide range of **libraries** (Selenium, API, Database, etc.)
- Generates **detailed reports and logs**
- Works with **command-line execution**

---

## ▶️ Basic Test Execution

Run a specific test file:

```bash
robot -d results parallelTest/test1.robot
```

- `-d results`: Sets the output directory to store reports and logs.

---

## 🔍 Filtering Tests by Tags

### Include tests with a specific tag:
```bash
robot -d results --include smoke parallelTest/test1.robot
```

### Exclude tests with a specific tag:
```bash
robot -d results --exclude smoke parallelTest/test1.robot
```

### Include tests with **both** `smoke` and `regression`:
```bash
robot -d results --include smokeANDregression parallelTest/test1.robot
```

### Include tests with **either** `smoke` or `regression`:
```bash
robot -d results --include smokeORregression parallelTest/test1.robot
```

### Run all `smoke` tests in a folder:
```bash
robot -d results --include smoke parallelTest
```

---

## 🎯 Run Specific Test Case by Name

```bash
robot --test <testcase_name> parallelTest/test1.robot
```

---

## 🔁 Rerun Failed Tests

```bash
robot --rerunfailed output.xml parallelTest
```

---

## 🔧 Using Variables

### Set a variable from command line:
```bash
robot -d results --variable BROWSER:chrome parallelTest/test5.robot
```

### Load variables from external Python file:
```bash
robot -d results --variablefile data.py parallelTest/test5.robot
```

---

## 🧪 Dry Run (Syntax Check Only)

```bash
robot -d results --dryrun parallelTest/test5.robot
```

---

## 📄 Custom Output, Report, and Log Files

```bash
robot --output output/custom_output.xml \
      --report output/custom_report.html \
      --log output/custom_log.html \
      parallelTest/test1.robot
```

---

## 🗂️ Argument File for Configurations

Use `args.txt` to define multiple options:

```bash
robot --argumentfile args.txt tests/
```

**Contents of `args.txt`:**

```text
--variable BROWSER:chrome
--variable ENV:staging
--outputdir results/
--include smoke
```

---

## ⚡ Parallel Execution with Pabot

Pabot enables parallel test execution with Robot Framework.

### Run with 4 parallel processes:

```bash
pabot --processes 4 parallelTest
```

### Split tests at test level with 2 processes:

```bash
pabot --testlevelsplit --processes 2 parallelTest/test3.robot
```

### Run with 3 processes, skip teardown on exit:

```bash
pabot --processes 3 --skipteardownonexit --outputdir results/ parallelTest
```

### Artifacts in subfolders, skip teardown:

```bash
pabot --processes 3 --artifactsinsubfolders --skipteardownonexit --outputdir results/ parallelTest
```

---

## 📊 Report Merging with Rebot

Rebot processes and merges output logs from test executions.

### Merge multiple output files:

```bash
rebot --merge --output merge_output.xml \
      --log merged_log.html \
      results/pabot_results/*/output.xml
```

### Merge single output into log:

```bash
rebot --log test2_log.html results/pabot_results/2/output.xml
```

### Include only `smoke` tag and generate custom log:

```bash
rebot --include smoke --log output/smoke_log.html output/my_output.xml
```

---

## ✅ Summary

| Tool   | Purpose                                  |
|--------|------------------------------------------|
| `robot` | Run test cases                          |
| `pabot` | Run tests in parallel                   |
| `rebot` | Merge and generate reports              |

---

> ✨ **Pro Tip:** Combine `pabot`, `--variablefile`, and `--include` options to create powerful and flexible CI pipelines for test execution!
```
