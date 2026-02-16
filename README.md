# 🚚 PDF Distributer

## 📝 Overview
The **PDF Distributer** is an automated file management script that acts as a "Sentry" for your workflow. It monitors a specific landing folder and automatically sorts incoming PDF invoices into organized directories based on specific **keys** extracted from the filename.

It manages two primary distribution channels:
1.  **Supplier Archive:** Organized by Supplier ID and Consumption Period.
2.  **Internal Fleet (INFPC):** Organized by Fleet, Training Type, and Consumption Period.

## 🏷️ File Naming Convention
For the script to parse information correctly, files must follow this underscore-separated pattern:
`SupplierID_InvoiceNr_Fleet_TrainingType_Period_PONumber.pdf`

| Key Position | Data Type | Used for Sorting? |

| 1 |          Supplier ID | ✅ Yes           |<br>
| 2 |       Invoice Number | ❌ No            |<br>
| 3 |                Fleet | ✅ Yes           |<br>
| 4 |        Training Type | ✅ Yes           |<br>
| 5 |               Period | ✅ Yes           |<br>
| 6 |            PO Number | ❌ No            |<br>

*Example:* `2990103_120003506_q4_conv_0126_33000012145.pdf`

## ⚙️ How it Works
* **Active Monitoring:** The script polls the `source_dir` every 10 seconds.
* **Safety Buffer:** Implements a 1-second delay upon detection to ensure files are fully written to the disk before processing.
* **Dynamic Folder Matching:** It performs a "starts with" search. If a folder begins with the Supplier ID (e.g., "2990103_Airways"), it uses that folder. If no match is found, it creates a new one using the ID.
* **Automated Allocation:**
    * Copies the file to the **Supplier** path.
    * Moves (cuts) the file to the **Internal Fleet** path.
* **Overwrite Policy:** Existing files in the destination with the same name are automatically 
replaced with the latest version.

## 🎯 Goal
The primary objective of this project is to eliminate the manual overhead of sorting and filing PDF invoices. By automating the distribution process, the script aims to:
* **Increase Efficiency:** Reduce the time spent manually navigating complex directory structures.
* **Ensure Accuracy:** Eliminate human error in file placement by using standardized naming conventions as "keys."

## 🚀 Setup & Execution
1.  **Prerequisites:** Ensure [Python 3.x](https://www.python.org/) is installed on the system.
2.  **Configuration:** Update the directory paths at the top of the script:
    * `source_dir`: Your "Drop" folder.
    * `supplier_dir`: The root directory for supplier folders.
    * `infpc_dir`: The root directory for internal fleet folders.
3.  **Run:** Double-click the provided `.bat` shortcut or run `python your_script_name.py` in the terminal.
4.  **Stop:** Close the terminal window or press `Ctrl + C`.

## 🛡️ Safety Net

The script is wrapped in a `try/except` block. If a file is locked or a path is unreachable, the script will print an error message and continue monitoring without crashing.

## Status
🚧 Work in Progress

Currently improving:
- Error handling
- Validation
