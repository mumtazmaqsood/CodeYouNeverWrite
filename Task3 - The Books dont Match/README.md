## Task 3: The Books Don't Match (Ledger Audit & Discrepancy Reconciliation)

### 1. Project Title and the Problem It Solves
* **Project Title:** The Books Don't Match — Ledger Audit & Discrepancy Reconciliation
* **Problem Solved:** Treasurers and event organizers frequently deal with messy payment lists containing nicknames, abbreviations, transaction duplicates, and incorrect amounts. When physical cash counts do not align with digital receipts, manual matching is error-prone. This project automates the reconciliation process by parsing digital transaction records, mapping fuzzy names back to an official student roster, identifying invalid or duplicate payments, and uncovering the exact cause of cash-to-digital discrepancies.

---

### 2. AI Tool(s) Used
* **Gemini:** Used to construct the data-matching logic, generate the classification engine rules, resolve fuzzy name mappings, and design the clean HTML/CSS reporting dashboard containing the visual metrics and financial tables.

---

### 3. The Initial Prompt and Improved Prompts

#### Initial Prompt
> "I have some students and a payment history. Reconcile them and make an HTML report showing who paid and who didn't."
* *Why it needed improvement:* This prompt did not capture the complexity of the ledger. It ignored the distinct transaction classifications (like "Cash Deposit" or "Non-Trip Transactions") and did not provide guidance on how to mathematically reconcile the physical cash against the digital total to highlight the actual discrepancy.

#### Improved/Refined Prompt
> "Act as a forensic accountant. Reconcile the provided datasets: `students.csv`, `payment_history.csv`, and the rules in `ground_truth.json`. 
> 1. Apply name-mapping rules to resolve abbreviations (e.g., 'Alice J.' to 'Alice Johnson').
> 2. Classify every transaction into categories: Valid Payment, Duplicate, Unknown Sender, Non-Trip Transaction, or Cash Deposit.
> 3. Account for the physical cash count of $75.00 and identify if the $75.00 cash deposit (TXN016) represents double-counting.
> 4. Build a comprehensive HTML report dashboard. Include an Executive Summary, a Student Reconciliation Table, Transaction Analysis, and a Financial Summary showing the final reconciled total versus the expected total. Emphasize why the books do not match."

---

### 4. Verification of Results
The ledger was verified by cross-referencing the processed values against the mathematical constraints in `ground_truth.json`:

* **Expected Digital Total:** $225.00 (9 students @ $25.00)
* **Expected Cash Collected:** $75.00 (3 students @ $25.00)
* **Expected Total Trip Cost:** $300.00 (12 students @ $25.00)

#### Verification Calculations:
1. **Valid Digital Check:** All 12 students listed on the roster were matched to exactly one valid $25.00 digital payment (TXN001 to TXN012). This represents a digital total of **$300.00**.
2. **Physical Cash Check:** The hand-counted cash total is confirmed to be **$75.00**.
3. **Total Valid Funds in Hand:** 
   $$\text{Valid Digital Payments } (\$300.00) + \text{Physical Cash } (\$75.00) = \$375.00\text{ in hand.}$$
4. **Discrepancy Check:** 
   $$\$375.00\text{ (Actual funds)} - \$300.00\text{ (Expected funds)} = \$75.00\text{ surplus.}$$

The physical cash deposit of $75.00 (TXN016) in the bank ledger represents the deposit of the physical cash counted in hand. This confirmed that no funds went missing, but rather that some students paid twice.

---

### 5. What Worked, What Did Not, and Problems Faced

#### What Worked
* **Fuzzy Name Resolution:** The mapping of nicknames and initials (e.g., "Chloe D" to "Chloe Davis", "K. White" to "Kevin White") worked reliably by using the defined dictionary rules.
* **Filtering Logic:** Transactions with incorrect amounts (such as Emma Wilson's $10.00 snack payment) and unknown senders were successfully isolated and ignored in the final student ledger.

#### What Did Not / Problems Faced
* **Double-Counting the Cash Deposit:** During early logic testing, the cash deposit of $75.00 (TXN016) was initially flagged as a standard "digital transaction." If left unchecked, this would have double-counted the $75.00 (registering $75.00 as physical cash AND $75.00 as a digital bank payment, erroneously showing $450.00 total). 
* **The Solution:** The algorithm was adjusted to treat "Cash Deposit" as a reconciliation-only event, classifying it as a bank logging record rather than a new source of individual student dues.

---

### 6. Final Result, Actionable Insights, and Learnings

#### Final Deliverables Created
1. **Reconciliation Report Dashboard (HTML):** A visual single-page report showing a "Reconciliation FAIL" status due to an overcollection.
2. **Deterministic Ledger Mappings:** A resolved payment sheet showing that every single student paid digitally, meaning the outstanding missing balance is $0.00.

#### Actionable Insights
* **Identify Double-Payers:** Because all 12 students have fully settled their dues digitally ($300.00), the $75.00 collected in cash is a redundant overpayment. This indicates three students paid both in cash and digitally.
* **Treasurer Actions:** The treasurer should refer to physical paper receipts to find the three students who paid cash, cross-reference them with the digital roster, and process a $25.00 refund to each of them to return the trip funds to the expected $300.00.

#### Key Learnings
Reconciliation failures do not always mean money is missing; they can also indicate overpayment due to communication gaps. When multiple payment channels (cash and digital apps) are available to a group, users may accidentally use both. Establishing a central ledger with validation checks is essential to catching redundant payments.

---

### 7. Project Screenshots / Visual Demo Placeholders
<img width="585" height="893" alt="image" src="https://github.com/user-attachments/assets/e109e306-b3c0-4777-b261-276ab171a07f" />
<img width="614" height="882" alt="image" src="https://github.com/user-attachments/assets/70fa22dd-efed-44be-b3db-22b66781f773" />
