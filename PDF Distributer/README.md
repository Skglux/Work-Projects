# 🚚 PDF Distributer

An automated Python "Sentry" that monitors a landing folder, parses incoming invoices (PDF/Excel), and distributes them into a structured archive based on filename metadata.

---

## 🏢 The Business Problem
Manual filing of supplier invoices is time-consuming and prone to human error. 
Invoices must be cross-referenced and filed in two distinct locations:
1.  **Supplier Directory:** Organized by Supplier ID and Billing Period.
2.  **Fleet-Training Directory:** Organized by Aircraft Fleet, Training Type, and Period.

---

## 🎯 Project Goals
* **Zero Manual Entry:** Eliminate the need to manually move files into nested folders.
* **High Precision:** Use standardized naming conventions as "keys" for 100% accurate placement.
* **Scalability:** Support complex filenames that involve multiple fleets or training types.

---

## ⚙️ How It Works
The script runs in a continuous loop (polling every 10 seconds) through the following lifecycle:

1.  **Monitor:** Scans the `source_dir` for new `.pdf` or `.xlsx` files.
2.  **Parse:** Splits the filename by underscores (`_`) to extract metadata.
3.  **Validate:** Verifies the **Supplier ID** length (8-11 chars) and checks **Fleet/Training codes** against authorized lists.
4.  **Distribute:** * Creates a master record in the **Supplier Archive**.
    * Generates copies in the **Training Archive** (handling multi-fleet splits like `b7q4`).
5.  **Clean:** Deletes the original file from the source folder only after all copies are successfully verified.

---

## 📋 Filename Requirements
To ensure correct sorting, files **must** follow this naming convention:

`SupplierID_Invoice#_FleetCode_TrainingType_Period_Other.pdf`

### Key Definitions:
| Key | Requirement | Example |
| :--- | :--- | :--- |
| **Supplier ID** | 8 to 11 characters | `VEND000123` |
| **Fleet Code** | Validated against `fleet_codes` | `b7`, `q4`, `e2`, `b7q4` |
| **Training Type**| Validated against `trng_codes` | `re`, `co`, `reco` |
| **Period** | 4 digits (MMYY) used for subfolder | `0124` |

---

## 📂 Logic Map

The script automatically generates the following structure if it doesn't exist:
```text
Archive/
├── 🏢 Supplier_Archive/
│   └── [Supplier_ID]/
│       └── [MMYY]/
│           └── File_Name.pdf
└── 🎓 Training_Archive/
    └── [Fleet_Code]/
        └── [Training_Type]/
            └── [MMYY]/
                └── File_Name.pdf
```

---

## 🚀 Setup
**Set Paths**: Open the script and update the directory paths to match your computer:
   ```python
   source_dir = "C:/path/to/input"
   supplier_dir = "C:/path/to/supplier_archive"
   infpc_dir = "C:/path/to/training_archive"
   ```

---

## 🛡️ Safety Net

The script is wrapped in a `try/except` block. If a file is locked or a path is unreachable, the script will print an error message and continue monitoring without crashing.
