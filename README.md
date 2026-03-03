# 🛠️ Business Workflow Automations

This repository contains programs developed in **Python** to automate and optimize tasks related to my role as a **Financial Officer**. These tools are designed to eliminate manual data entry, streamline complex file management, and ensure high accuracy in financial reporting.

---

## 📂 Project Overview

### 1. 🚚 PDF Distributer (The Sentry) — ✅ Complete (Polishing Phase)
**Problem:** Incoming PDF invoices require manual sorting and filing based on supplier, fleet, training type and period.
**Solution:** An automated script that monitors a "landing" directory and uses filename keys to:
* **Validate:** Check supplier IDs and training codes against predefined logic.
* **Organize:** Automatically create directory structures by period and flett/training type/period.
* **Distribute:** Move files to their final destinations and remove them from the landing zone.
* **Status:** Fully functional; currently in the **polishing phase** for future optimizations and code refactoring.

### 2. 📊 Report Transformer & Calculator — 🏗️ Work in Progress
**Problem:** Monthly raw reports are exported in "print-only" formats with merged cells and messy layouts, resulting in time consuming data calculation and control.
**Solution:** A script using `openpyxl` that:
* **Cleans:** Unmerges cells and fixes alignment issues across the dataset.
* **Automates Logic:** Injects dynamic Excel formulas to calculate "Paid Days" and "Amount (EUR)" while handling specific business exceptions.
* **Optimizes:** Reduces hours of manual data control to a single execution.
* **Status:** Under active development. Future updates will include smart format detection and automated email dispatching.

---

## ⚙️ Tech Stack
* **Language:** Python 3.x 🐍
* **Libraries:** * `os` & `shutil`: Robust file system operations and management.
  * `openpyxl`: Advanced Excel spreadsheet manipulation.
  * `time`: Script pacing and automation loops.

---

## 🚀 Getting Started
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Skglux/Work-Projects.git](https://github.com/Skglux/Work-Projects.git)