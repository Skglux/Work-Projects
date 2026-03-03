# 📊  Gordian Knot (WIP)

## 🎯 The Business Problem
Monthly reports are currently downloaded in spreadsheet that their formats were designed for printing rather than data analysis. This creates a significant "manual control" burden due to:
* **Structural Obstacles:** Merged cells and irregular column layouts that prevent standard calculations.
* **Volume & Risk:** Hours of manual data entry and verification, which increases the probability of errors.
* **Complex Logic:** The need to apply different business rules based on specific codes and dates.

## 🛠️ Current Automation Progress
I am developing a Python solution using `openpyxl` to transform this manual process into a structured, "one-click" workflow.

### ✅ Completed Features:
* **Automated Sanitization:** The script identifies and unmerges cells in the core data range (Columns 1-15) and resets alignment for a clean tabular view. 🧱
* **Exception Handling Logic:** Hardcoded validation for specific `tlc_exceptions` and `days_count_exceptions` to ensure accurate indexing.
* **Dynamic Formula Injection:** Instead of manual typing, the script writes complex Excel formulas (INDEX, MATCH, COUNTIF) directly into the spreadsheet to calculate:
  * **Paid Count Days:** Logic to determine billable time.
  * **Financial Totals:** Automatic calculation of Amounts in EUR.
* **Clean Output:** Auto-filters are applied to the final results, and helper columns are hidden to keep the final report professional. 🔍

---

## 🏗️ Roadmap & Work in Progress
This project is currently under active development. Future updates will include:
1. **Smart Format Detection:** Differentiating between "A" and "B" package structures automatically.
2. **Data Cleanup:** Removing duplicate entries and handling specific tlc exceptions.
3. **Distribution:** Integrating an automated email dispatch system.
4. **Execution Control:** Creating a user-friendly process to activate/deactivate the program.