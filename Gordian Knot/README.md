# Gordian Knot — Bonus Automation Script

A desktop automation tool that processes paired **Report A / Report B** Excel files, cleans their data, and injects bonus-calculation formulas — all driven by a single `config.json` file with no hardcoded business values.

---

## What it does

1. **Unmerges cells** across columns 1–15 and strips wrap-text formatting.
2. **Trims TLC names** (Three Letter Codes) in column 2 to remove whitespace.
3. **Detects file type** (Report A or Report B) automatically from cell content, falling back to the filename and — as a last resort — a dialog prompt.
4. **Extracts Special TLC data** from the Report B sheet (instruction-day rows in columns 9–13).
5. **Appends Special TLC rows** into the matching block inside Report A.
6. **Deletes excluded TLC blocks** (configured per report type in `config.json`).
7. **Removes duplicate day entries** within each TLC block, keeping the first occurrence.
8. **Writes a TLC modifier lookup table** into hidden helper columns X/Y.
9. **Injects Excel formulas** into calculation columns Q–W (rows 6–999):
   - Q: Instruction Day · R: TLC · S: Exception flag · T: Day threshold · U: Days count · V: Paid count days · W: Amount (EUR)
10. **Hides helper columns** X/Y and applies an auto-filter on Q5:W1000.
11. **Saves** each processed file as `Modified_<original_filename>` in the chosen output folder.
12. **Optionally emails** the output files as attachments via SMTP.

---

## Prerequisites

- Python 3.10+
- `openpyxl`
- `tkinter` (included in standard CPython distributions)

Install dependencies:

```bash
pip install openpyxl
```

---

## Setup

1. Edit `config.json` with your real values. The file has three top-level sections:

### `report_a` / `report_b`

| Key | Type | Description |
|---|---|---|
| `bonus_amount` | number | EUR bonus per paid day (e.g. `20`) |
| `day_over_count` | number | Minimum-day threshold used in formula column T (e.g. `4`) |
| `excluded_tlc` | list | TLC codes whose entire blocks are deleted before formula injection |
| `tlc_modifiers` | object | Maps a day-count string to a list of TLC codes written to the X/Y lookup table |
| `special_tlc_code` | string | The TLC whose rows are extracted from Report B and appended to Report A |

### `email`

| Key | Description |
|---|---|
| `enabled` | Set to `true` to activate email dispatch after processing |
| `smtp_server` / `smtp_port` | SMTP host and port (e.g. `smtp.gmail.com`, `587`) |
| `sender` / `password` | Sending account credentials |
| `recipients` | List of recipient addresses |
| `subject` / `body` | Email subject line and body text |

> **Note:** The `config.json` included in this repository contains dummy values.

---

## Usage

Run the script directly:

```bash
python gordian_knot.py
```

Two dialogs appear in sequence:

1. **Select Excel files** — pick one or more Report A / Report B `.xlsx` files. You may select both at once; the script processes Report B before Report A automatically so the Special TLC data is available when Report A needs it.
2. **Select output folder** — choose where the `Modified_` files are saved. If you dismiss this dialog, output defaults to the same folder as the first selected file.

Progress and any warnings are printed to the console. Each saved file is named `Modified_<original_filename>`.

---

## File type detection

The script identifies each file in order of priority:

1. **Content-based** — scans column 2 for TLC codes that appear in the `excluded_tlc` lists; each list is unique to one report type.
2. **Filename** — looks for `report_a` or `report_b` in the filename (case-insensitive).
3. **Dialog prompt** — asks the user when both heuristics fail.

---

## Processing order

Report B is always processed first. This ensures the Special TLC rows are captured in `data_dict` before Report A's `append_special_tlc_insti_days` step runs.

Each report type runs its own processing pipeline defined in `file_type_config`:

**Report B pipeline:**
`unmerge → trim → bonus_index → extract_special_tlc → tlc_data_input → headers → delete_excluded_tlc → remove_duplicate_days → fucntions_input → hide_filter`

**Report A pipeline:**
`unmerge → trim → bonus_index → append_special_tlc_insti_days → tlc_data_input → headers → delete_excluded_tlc → remove_duplicate_days → fucntions_input → hide_filter`

---

## Known issues / pending work

- **PENDING 8:** Activation / deactivation process (e.g. scheduled task or desktop shortcut).

---

## Project structure

```
gordian_knot.py              # Main script
config.json                  # Dummy config with placeholder values
demo_report_a.xlsx           # Dummy Report A input for testing
demo_report_b.xlsx           # Dummy Report B input for testing
Modified_demo_report_a.xlsx  # Expected output for demo_report_a.xlsx
Modified_demo_report_b.xlsx  # Expected output for demo_report_b.xlsx
```
