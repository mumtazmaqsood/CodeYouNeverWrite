
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

* *<img width="778" height="868" alt="image" src="https://github.com/user-attachments/assets/50d119b5-5970-4f69-bb3a-e50e7b666575" />
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Task 2

**Task 2 – What's My Grade, Really?**

---

## Problem the Project Solves

Many online grade calculators and school learning management systems cannot accurately calculate a student's course grade because they do not support instructor-specific grading policies. These policies may include weighted grading categories, dropping the lowest assignment or quiz, replacing a low midterm score with a higher final exam score, or awarding bonus points.

This project solves that problem by creating a Python grade calculator that follows the instructor's grading rules exactly. It also predicts the score needed on the final exam to achieve a desired overall course grade.

---

## AI Tool(s) Used

- **ChatGPT (OpenAI)**

ChatGPT was used to:
- Generate realistic sample grading data.
- Design the grading policy.
- Write the Python grade calculator.
- Calculate the current course grade.
- Determine the required final exam score for a target grade.
- Produce documentation for the project.

---

## Initial Prompt

> Write a Python script that calculates my current course grade using my assignments, quizzes, midterms, and grading policy. The grading policy includes weighted categories, dropping the lowest quiz, conditionally dropping the lowest assignment, replacing the lowest midterm with the final exam if it is higher, and adding bonus points.

---

## Improved Prompt

> Write a reusable Python program that:
>
> - Calculates the current course grade using the provided sample scores.
> - Drops the lowest quiz automatically.
> - Drops the lowest assignment if the assignment average remains at least 85%.
> - Replaces the lowest midterm score with the final exam score if the final exam is higher.
> - Applies weighted grading categories.
> - Calculates the exact final exam score needed to achieve a target overall course grade.
> - Makes it easy to update scores throughout the semester.

The improved prompt produced a more complete and reusable solution.

---

## How I Verified the Result

The program's calculations were verified manually by checking the quiz category.

Quiz scores:

- 18
- 20
- 15
- 19
- 17

The grading policy states that the lowest quiz score should be dropped.

Dropped score:

15

Remaining scores:

18, 20, 19, 17

Average:

(18 + 20 + 19 + 17) ÷ 4 = 18.5

Percentage:

18.5 ÷ 20 × 100 = **92.5%**

The Python program produced the same quiz average (92.5%), confirming that the implementation was correct.

---

## What Worked

- The AI generated a complete Python program from a natural language description.
- The weighted grading calculations were accurate.
- The script correctly implemented score-dropping rules.
- The program automatically calculated the current course grade.
- It successfully determined the required final exam score for any target grade.
- The script was easy to modify with new grades.

---

## What Did Not Work Initially

Initially, the generated solution only calculated the current grade and did not determine the required final exam score.

The first version also did not clearly separate the grading rules into reusable sections, making future updates more difficult.

These issues were resolved by improving the prompt and requesting a reusable script with additional functionality.

---

## Problems Faced

Since actual course grades and grading policies were unavailable, realistic sample data had to be created for testing.

Another challenge was ensuring that all grading rules interacted correctly, particularly:

- Dropping the lowest assignment only when the average remained above the required threshold.
- Ignoring the final exam weight until the exam had been completed.
- Correctly replacing the lowest midterm score only when the final exam score was higher.

These rules required careful implementation and testing.

---

## Final Result

The final project produced a reusable Python grade calculator that:

- Calculates the current course grade.
- Applies instructor-specific grading rules.
- Drops the lowest quiz score.
- Conditionally drops the lowest assignment.
- Replaces the lowest midterm with the final exam when appropriate.
- Supports bonus points.
- Calculates the exact final exam score required for any target course grade.
- Can be updated throughout the semester by changing only the score lists.

Using the sample data, the calculator reported a current course grade of approximately **90.11%** and determined that approximately **89.8%** on the final exam would be needed to finish the course with a **90% overall grade**.

---

## What I Learned
This project demonstrated how AI can automate complex calculations while following customized grading rules. I learned how to convert grading policies into program logic, verify AI-generated results through manual calculations, and improve AI prompts to obtain more accurate and reusable solutions.

The project also highlighted the importance of validating AI-generated code instead of accepting the output without checking its correctness.

This project demonstrated how AI can automate complex calculations while following customized grading rules. I learned how to convert grading policies into program logic, verify AI-generated results through manual calculations, and improve AI prompts to obtain more accurate and reusable solutions.

The project also highlighted the importance of validating AI-generated code instead of accepting the output without checking its correctness.
