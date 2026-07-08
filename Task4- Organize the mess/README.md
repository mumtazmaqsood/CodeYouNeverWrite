
# Safe AI-Assisted Folder Analysis and Cleanup Planning

## Project Overview
This project demonstrates how Artificial Intelligence (AI) can assist in safely analyzing and understanding a cluttered folder without risking the loss of important data. 

Over time, directories such as Downloads, Documents, and project folders accumulate redundant files—including duplicate files, forgotten documents, screenshots, installers, old downloads, and unnecessary copies. The purpose of this project was to establish a safe, systematic process to discover existing files, identify cleanup opportunities, and generate detailed reports before making any actual changes.

To prevent accidental data loss, the project followed a strict **safety-first approach**:
*   **Backup Priority:** A complete backup was created before initiating any analysis.
*   **Isolated Execution:** Scripts were executed solely on the backup directory.
*   **Read-Only Operations:** No files were deleted, moved, or renamed during the process.
*   **Dry-Run Verification:** A detailed dry-run report was generated prior to proposing any organization tasks.
*   **Human-in-the-Loop:** All potential file modifications require manual review and approval.

The outcome of this process is a structured understanding of folder contents, documented through automated text, CSV reports, and an interactive HTML dashboard.

---

## 1. Problem Statement
Digital storage folders naturally accumulate clutter as files are downloaded, copied, renamed, and stored across different locations. 

The target Downloads folder in this project presented several common challenges:
*   Redundant files that may no longer be required.
*   Duplicate files occupying unnecessary storage.
*   Files with highly similar or identical names.
*   Large individual files consuming drive capacity.
*   Various file types mixed together without organization.
*   Forgotten documents and legacy software installers.

Manually reviewing thousands of files is time-consuming and introduces the risk of human error. The primary challenge addressed was: **How can a user analyze and organize files safely and efficiently without risking accidental data loss?**

---

## 2. Project Goal
The objective was to design a secure, AI-assisted workflow to:
1.  Scan and analyze folder contents.
2.  Detect duplicate files using content hashing.
3.  Identify large and aging files.
4.  Group files by category and extension.
5.  Generate clear, actionable reports.
6.  Provide data-driven recommendations before any file operations occur.

The focus remains strictly on understanding existing data first rather than immediate, automated deletion.

---

## 3. Safety Architecture
To ensure zero accidental data loss, the project strictly enforced three safety rules:

### Rule 1: Mandatory Backup
Before running any scripts, the original folder was copied to create an isolated environment.
*   **Original Folder:** `Downloads`
*   **Working Backup:** `Downloads_Backup`
*   *Note: All analysis scripts were configured to run only against the backup directory, ensuring the original files remained completely untouched.*

### Rule 2: Define "Clean" Before Acting
In this workflow, a "clean" folder is defined by visibility and structure rather than deletion:
*   Identified duplicates and large files.
*   Highlighted aging or obsolete files.
*   Categorized files by extension.
*   Suggested organization pathways.
*   Preserved essential and sensitive data.

### Rule 3: Dry-Run Enforcement
The AI and automation scripts were restricted from performing destructive actions. The core directive was:
> *"Analyze the contents and present a complete plan—identifying every file that could be moved, renamed, or deleted—and wait for manual approval before executing any file operations."*

The scripts were restricted from:
*   Deleting or overwriting files.
*   Renaming or moving files.
*   Modifying file metadata.

---

## 4. Tools & Technologies Used

### AI Assistant (ChatGPT)
Used to assist with:
*   Designing safe, read-only workflows.
*   Generating and debugging Python scripts.
*   Refining analysis prompts.
*   Designing the HTML reporting layout.

### Automation Tool (Python)
Used as the execution engine for:
*   Scanning directory structures.
*   Calculating SHA-256 hashes for precise duplicate identification.
*   Filtering files by size and modification age.
*   Generating structured outputs (TXT, CSV, and HTML formats).

---

## 5. Prompting Strategy

### Initial Safety Prompt
To set boundaries with the AI assistant, the following initial prompt was used:
```text
Show me your full plan first—every file you would move, delete, or rename—and wait for my approval before touching anything.
```

### Script and Analysis Refinement Prompts

#### Prompt 1: Read-Only Folder Analysis
```text
Analyze this folder but do not modify anything.

Create a report showing:
- Duplicate files
- Large files
- Old files
- File types
- Organization opportunities

Do not move, rename, or delete anything.
```

#### Prompt 2: Safe Python Script Generation
```text
Create a Python script that only analyzes my backup folder.

The script must:
- Never delete files.
- Never rename files.
- Never move files.
- Create reports only.
- Work only on the backup folder.
```

#### Prompt 3: HTML Report Formatting
```text
Create an HTML report from the generated CSV files so the results are easier to review.
```

---

## 6. Implementation Process

### Step 1: Directory Setup
A backup copy of the target folder was created as the isolated working directory.
*   **Original Path:** `C:\Users\mmaq\OneDrive - Stibo\Documents\Downloads`
*   **Backup Path:** `C:\Users\mmaq\OneDrive - Stibo\Documents\Downloads_Backup`

### Step 2: Analysis Script Development
The script `analyze_folder.py` was developed to handle the core scanning and analysis. This script:
*   Traversed the backup directory.
*   Identified files and recorded file sizes.
*   Calculated SHA-256 hashes of file contents to verify duplicates, ignoring filename differences.
*   Flagged files matching specific age threshold criteria.

### Step 3: Running the Analysis
The script was executed via the command line:
```bash
python analyze_folder.py
```
This script generated the following raw data reports in the working directory:
*   `summary.txt`
*   `duplicates.csv`
*   `same_names.csv`
*   `large_files.csv`
*   `old_files.csv`

### Step 4: HTML Dashboard Generation
A secondary script, `create_html_report.py`, was run to aggregate the raw TXT and CSV data into an interactive, readable format:
*   **Output File:** `folder_cleanup_report.html`
*   This dashboard compiles the summary metrics, duplicate groups, large files, and potential cleanup recommendations into an easy-to-navigate browser interface.

---

## 7. Verification Process

To ensure accuracy and safety, the outputs were verified through the following checks:

1.  **Original Folder Integrity:** Confirmed that the source `Downloads` folder remained entirely unmodified. No files were deleted, moved, or altered.
2.  **Report Accuracy:** Cross-referenced random entries in the generated CSV files with actual file properties in the backup folder to confirm sizes, paths, and dates.
3.  **Hash-Based Duplicate Verification:** Confirmed that duplicate flagging was based on identical SHA-256 file hashes rather than just matching file names, preventing false positives.
4.  **Manual UI Review:** Opened `folder_cleanup_report.html` locally to manually review storage distribution, ensuring the layout correctly presented data trends and potential cleanup actions.

---

## 8. Challenges & Resolutions

### Challenge 1: Environment Path Issues
*   **Error:** `Python was not found`
*   **Cause:** Python was either not installed or not configured in the system's Environment Variables (`PATH`).
*   **Resolution:** Installed Python and ensured the "Add Python to PATH" option was selected. Verified installation using `python --version`.

### Challenge 2: Directory Execution Errors
*   **Error:** `can't open file 'analyze_folder.py': [Errno 2] No such file or directory`
*   **Cause:** The terminal session was not pointed to the directory where the script was saved.
*   **Resolution:** Used the `cd` command in the terminal to navigate to the correct folder before executing the script.

### Challenge 3: HTML Report Output Visibility
*   **Issue:** The generated HTML report was not immediately visible in the target directory.
*   **Resolution:** Modified the Python output script to explicitly print the absolute path of the generated HTML file upon successful completion, ensuring easy location.

---

## 9. Key Deliverables and Reports

The workflow successfully generated the following assets without altering user data:

| File Name | Description |
| :--- | :--- |
| `summary.txt` | General overview of total files, directory size, and overall category distribution. |
| `duplicates.csv` | List of duplicate files grouped by matching SHA-256 content hashes. |
| `same_names.csv` | Files sharing identical names but possessing different file contents. |
| `large_files.csv` | Files exceeding size thresholds, highlighting potential storage-saving targets. |
| `old_files.csv` | Files that have not been modified or accessed for an extended period. |
| `folder_cleanup_report.html` | A unified dashboard summarizing all findings in an interactive format. |

---

## 10. Potential Cleanup Insights
By reviewing the compiled reports, users can identify:
*   Duplicate images, videos, or documents taking up unnecessary storage.
*   Outdated installers (e.g., `.msi` or `.exe` files) that can safely be deleted or archived.
*   Large temporary zip archives that are no longer active.
*   Unorganized files that are candidates for structured subdirectories.

*Note: Any actual file cleanup must be executed manually based on these insights.*

---

## 11. Lessons Learned & Observations

### What Worked Well
*   The **backup-first** principle effectively mitigated the risk of accidental data deletion during the development and testing phases.
*   Using **file content hashing** (SHA-256) prevented false duplicate flags on files that shared generic names but held different data.
*   Converting raw CSV files into an **HTML dashboard** significantly improved data readability and simplified manual decision-making.
*   The approach established a **repeatable workflow** that can be applied to other messy directories in the future.

### Challenges Encountered
*   Initial Python configuration and shell path navigation required adjustments.
*   Generating text-only logs proved difficult to parse initially, which highlighted the value of structured CSV and HTML interfaces.

---

## 12. Future Scope
Potential enhancements to this project include:
*   **Automatic Category Sorting:** Implementing extension-based rules to suggest specific target folder paths (e.g., moving `.pdf` to a "Documents" subfolder).
*   **Graphical User Interface (GUI):** Developing a lightweight local interface for non-technical users.
*   **Safe Execution Script:** Adding a script that securely executes approved actions (moves/deletions) based on a manually verified checklist, with an built-in "undo" log.
*   **Preview Integration:** Including file thumbnail or path previews directly within the HTML dashboard.
