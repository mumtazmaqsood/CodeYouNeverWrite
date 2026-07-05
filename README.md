
# Task 1 Report: Personal Finance Auditing

## Task 1: Money Detective (Financial Leak & Subscription Analysis)

### 1. Project Title and the Problem It Solves
* **Project Title:** Money Detective
* **Problem Solved:** Personal bank statements are often long, cluttered, and difficult to audit manually. Over time, individuals accumulate "financial leaks"—such as duplicate charges, forgotten or overlapping subscriptions, and high-frequency micro-payments—that go unnoticed. This project solves that problem by using AI and programmatically running a rules-based analysis script over historical PDF transaction data to automatically surface these leaks and group spending categories for actionable decision-making.

---

### 2. AI Tool(s) Used
* **Gemini:** Used for high-accuracy text extraction (OCR) of the Danish bank statement, pattern recognition across the transaction history, and generation of both the automated Python analysis script and the interactive HTML reporting dashboard.

---

### 3. The Initial Prompt and Improved Prompts

#### Initial Prompt
> "Analyze my bank statement PDF and find any subscriptions or duplicate charges."
* *Why it needed improvement:* This prompt was too generic. It did not instruct the AI on how to handle the specific layout of Danish bank statements, multi-currency transactions, or how to programmatically structure the final script for future reuse.

#### Improved/Refined Prompt
> "Act as a financial data analyst. Extract all transactions from the attached 6-page Danske Bank PDF statement covering 01.04.2026 to 30.06.2026. 
> 1. Identify recurring monthly subscriptions, overlapping service providers (specifically in telecom), and duplicate payments occurring on the same day.
> 2. Reconcile the mathematics: ensure the sum of starting balance, total inflows, and total outflows matches the printed ending balance.
> 3. Write a modular Python script that utilizes standardized merchant name-matching (ignoring minor suffix variations) to flag these exact anomalies in future CSV exports.
> 4. Generate an interactive HTML/CSS report dashboard summarizing these findings."

---

### 4. Verification of Results
The results were verified using a three-factor mathematical reconciliation against known figures directly printed on the Danske Bank statement:

1. **Known Starting Balance (31.03.2026):** `100.715,39 DKK`
2. **Known Ending Balance (30.06.2026):** `128.949,57 DKK`
3. **Reconciliation Formula:** 
   $$\text{Ending Balance} = \text{Starting Balance} + \text{Total Inflows} - \text{Total Outflows}$$

* **Calculated Inflows (Income/Refunds):** `+127.579,61 DKK` (including the major salary payment on June 30th of `69.403,56 DKK`).
* **Calculated Outflows (Expenses/Fees):** `-99.345,43 DKK` (including the quarterly bank package fee of `117,00 DKK`).
* **Verification Math:** 
   $$100.715,39 + 127.579,61 - 99.345,43 = 128.949,57\text{ DKK}$$

Because the calculated net change of `+28.234,18 DKK` matched the statement balances down to the øre (cents), the dataset extracted by the AI was verified as complete and accurate.

---

### 5. What Worked, What Did Not, and Problems Faced

#### What Worked
* **Keyword Mapping:** The AI excelled at recognizing Danish banking terms (e.g., *Lønoverførsel* for salary, *Gebyrer* for fees, and *Udl. kortbetaling* for foreign transaction card fees).
* **Cross-Provider Identification:** The system successfully flagged that the user was paying four separate mobile networks (Telenor, Telmore, Callme, and Lebara) during the same billing cycles.
* **Duplicate Detection:** It successfully flagged a double charge of `19,00 DKK` from Lebara Denmark ApS occurring on the exact same posting date (`11.06`).

#### What Did Not & Problems Faced
* **Multi-Currency Tracking:** Transactions made in foreign currencies (such as Pakistani Rupees / PKR for Cyber Internet, or Qatar Riyals / QAR for Qatar Airways) were initially difficult to parse because the statement displays both the foreign amount and the converted DKK amount. The prompt had to be adjusted to ensure only the final DKK values were calculated to prevent double-counting.
* **Sign Notation:** Danske Bank represents inflows with a trailing `+` and outflows with a trailing `-` (e.g., `500,00 -`). Standard regex parser logic often expects leading signs (e.g., `-500.00`). The parsing rules had to be explicitly updated to handle trailing signs and European decimal comma notation (`100.715,39`).

---

### 6. Final Result, Actionable Insights, and Learnings

#### Final Deliverables Created
1. **Interactive HTML Dashboard:** A clean, card-based local web report visualising leaks, duplicate charges, recurring expenses, and mathematical validation.
2. **Modular Python Audit Script:** A script that can be run on future transaction exports to automate duplicate checks and flag multi-carrier billing anomalies.

#### Actionable Insights
* **Telecom Consolidation:** Paying Telenor, Telmore, Callme, and Lebara simultaneously is a major structural leak. Consolidating into a single family plan or single carrier can save an estimated **`~6.000 DKK` annually**.
* **Billing Dispute:** The double charge of `19,00 DKK` on `11.06` from Lebara represents a candidate for a refund claim or check on multiple active SIM profiles.
* **Debt Optimization:** Over the three-month period, a total of `75.583,00 DKK` was paid to Bank Norwegian As. Investigating refinancing or consolidation of this debt could reduce high interest-rate leaks.

#### Key Learnings
This project demonstrated that minor, recurring subscriptions (like multiple `19,00 DKK` charges) are easily overlooked individually but aggregate into substantial annual leaks. Programmatic auditing using simple string-matching and date-matching rules is vastly faster and more reliable than manual line-by-line review.

---

### 7. Project Screenshots / Visual Demo Placeholders

* *[Insert Screenshot of the interactive HTML Dashboard here]*
* *[Insert Screenshot of Python script execution output showing the flagged duplicates and telecom overlap warnings here]*
