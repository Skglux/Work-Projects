# 🚚 PDF Distributer

A Python script that monitors a folder for PDF and Excel files and moves them into organized subfolders based on their filenames.

---

## ⚙️ How It Works

The script runs on a continuous loop (every 10 seconds) and performs the following steps:

1. **Monitor**: Scans the `source_dir` for `.pdf` or `.xlsx` files.
2. **Parse**: Breaks down the filename using underscores (`_`) as separators.
3. **Validate**: Checks the filename against predefined lists of fleet codes and training types.
4. **Sort**: 
   * Moves a copy to the **Supplier** folder (organized by period).
   * Moves copies to the **Training** folders (organized by fleet, then type, then period).
5. **Clean**: Deletes the file from the source folder after it has been successfully copied.

---

## 📋 Filename Requirements

The script expects filenames to follow this specific format to sort them correctly:

`SupplierID_Invoice#_FleetCode_TrainingType_Period_Other.pdf`

* **Supplier ID**: Must be between 8 and 11 characters.
* **Fleet Codes**: Validated against a list (e.g., `b7`, `q4`, `e2`).
* **Training Codes**: Validated against a list (e.g., `re`, `co`, `reco`).

---

## 🎯 Goal
The primary objective of this project is to eliminate the manual overhead of sorting and filing PDF invoices. By automating the distribution process, the script aims to:
* **Increase Efficiency:** Reduce the time spent manually navigating complex directory structures.
* **Ensure Accuracy:** Eliminate human error in file placement by using standardized naming conventions as "keys."

---

## 🚀 Setup
1. **Set Paths**: Open the script and update the directory paths to match your computer:
   ```python
   source_dir = "C:/path/to/input"
   supplier_dir = "C:/path/to/supplier_archive"
   infpc_dir = "C:/path/to/training_archive"

## 🛡️ Safety Net
The script is wrapped in a `try/except` block. If a file is locked or a path is unreachable, the script will print an error message and continue monitoring without crashing.