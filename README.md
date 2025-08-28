# Python CSV File Combiner

A professional-grade Python script that automatically finds and combines multiple CSV files from a specified folder into a single, clean master report. This project demonstrates key data handling and file system automation skills using the Pandas and Glob libraries.

---

### The Problem

This script is designed to solve the common business problem of having data spread across multiple files (e.g., monthly sales reports, daily logs). Manually copying and pasting this data is slow, tedious, and prone to errors.

### The Solution

The `combiner.py` script fully automates this process:

1.  **File Discovery:** Uses the `glob` library to dynamically find all files ending with `.csv` inside the `input_files` directory.
2.  **Data Ingestion:** Reads each discovered CSV file into a separate Pandas DataFrame.
3.  **Data Consolidation:** Concatenates all the individual DataFrames into one master DataFrame, stacking them vertically.
4.  **Index Normalization:** Creates a new, clean, sequential index for the master report, discarding the old indexes from the source files.
5.  **Clean Export:** Saves the final, combined DataFrame to a new file named `master_report.csv`, ready for immediate use.

### How to Use

1.  Place all your source CSV files into the `input_files` folder.
2.  Ensure you have the required Python libraries installed: `pip install pandas`
3.  Run the script from your terminal: `python combiner.py`
4.  The clean, combined output file, `master_report.csv`, will be created in the root directory.

### Technologies Used

-   Python
-   Pandas
-   Glob