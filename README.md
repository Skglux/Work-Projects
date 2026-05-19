# 🛠️ Business Workflow Automations

A collection of Python tools built to eliminate manual work in a **Financial Officer** role — from invoice filing to monthly bonus reporting. Each tool is self-contained, config-driven, and built around real operational problems.

---

## 📂 Projects

### 1. 🚚 The Sentry — PDF Distributer ✅ Complete

**The problem:** Incoming PDF and Excel invoices arrive in a single landing folder and must be manually cross-filed in two separate archive locations — once by supplier and once by fleet and training type — using metadata buried in the filename.

**The solution:** A continuous monitoring script that parses each filename, validates its keys, builds the required directory structure on the fly, and distributes copies to every correct destination — then deletes the original from the landing zone.

| What it handles | Detail |
|---|---|
| 📄 File types | `.pdf` and `.xlsx` |
| 🏢 Supplier archive | Filed by Supplier ID → Billing Period |
| 🎓 Training archive | Filed by Fleet Code → Training Type → Period |
| ✂️ Split filenames | Multi-fleet codes like `b7q4` are split and filed under each fleet independently |
| 🛡️ Safety net | `try/except` loop — a bad file prints an error and the script keeps running |

**Tech:** `os` · `shutil` · `time`

📖 [Full documentation →](pdf_distributer/README.md)

---

### 2. ⚔️ Gordian Knot — Bonus Automation &nbsp;✅ Complete

**The problem:** Monthly raw reports are exported in print-only Excel formats with merged cells and messy layouts, requiring hours of manual data preparation and bonus calculation.

**The solution:** A desktop GUI script that accepts paired Report A / Report B files, cleans their structure, transfers cross-report data, and injects a full set of Excel formulas to compute paid days and EUR amounts — all without touching a cell manually.

| What it handles | Detail |
|---|---|
| 🔓 Cell cleanup | Unmerges cells, strips whitespace, fixes alignment |
| 🔍 Auto-detection | Identifies report type from content, filename, or dialog |
| 🔄 Cross-report data | Extracts Special TLC rows from Report B and injects them into Report A |
| 🧮 Formula injection | Populates columns Q–W with dynamic bonus calculation logic |
| ⚙️ Config-driven | All TLC codes, bonus amounts, and thresholds live in `config.json` — nothing hardcoded |
| 📧 Optional email | Can send output files automatically via SMTP when enabled |

**Tech:** `openpyxl` · `tkinter` · `json`

📖 [Full documentation →](gordian_knot/README.md)

---

## ⚙️ Tech Stack

| | |
|---|---|
| **Language** | Python 3.10+ 🐍 |
| **Excel manipulation** | `openpyxl` |
| **File system** | `os` · `shutil` |
| **GUI / dialogs** | `tkinter` |
| **Email dispatch** | `smtplib` · `email` |
| **Config management** | `json` |

---

## 🗂️ Repository Structure

```
📁 business-workflow-automations/
├── 📁 pdf_distributer/
│   ├── pdf_distributer.py
│   └── README.md
├── 📁 gordian_knot/
│   ├── gordian_knot.py
│   ├── config.json
│   ├── demo_report_a.xlsx
│   ├── demo_report_b.xlsx
│   ├── Modified_demo_report_a.xlsx
│   ├── Modified_demo_report_b.xlsx
│   └── README.md
└── README.md
```
