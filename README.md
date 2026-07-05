# Task 1 — Money Detective

**Estimated Time:** ~45 minutes

## Overview

Money Detective is a personal finance analysis project that helps identify hidden spending leaks in historical transaction data. Instead of creating a new budget, the project analyzes past transactions to uncover recurring subscriptions, duplicate charges, and unusual spending patterns.

The goal is to transform transaction history into actionable insights that can help reduce unnecessary expenses.

---

## Objective

Analyze a bank or digital wallet transaction statement to automatically detect:

- Recurring charges
- Possible forgotten subscriptions
- Duplicate or repeated payments
- Spending patterns by category

The project also verifies the analysis against known financial totals to ensure accuracy.

---

## Input

The program accepts a transaction statement exported from a bank or digital wallet.

**Supported format**

- PDF transaction statement (provided by the user)

The statement should contain at least:

- Transaction Date
- Description
- Amount

---

## Requirements

Before running the analysis, prepare:

- A PDF export of your transaction history
- At least one known financial figure for verification (e.g., monthly total spending or account balance)
- A rough idea of your spending categories

---

## Workflow

### Step 1 — Extract Transactions

Provide the PDF statement as input.

The transaction data is extracted into a structured format containing:

- Date
- Description
- Amount

---

### Step 2 — Analyze Transactions

The generated script examines the transaction history to detect:

- Recurring monthly or periodic payments
- Possible forgotten subscriptions
- Duplicate charges
- Repeated payments occurring within a short period
- Spending grouped by merchant or category

---

### Step 3 — Verify Results

Validate the analysis by comparing at least two computed totals with known values such as:

- Monthly spending total
- Known account balance
- Expected transaction sums

Matching values increase confidence in the remaining analysis.

---

### Step 4 — Understand the Logic

Review the AI-generated explanation of how the detection algorithm works in plain English.

This helps ensure the analysis process is transparent and understandable.

---

### Step 5 — Save for Future Use

Store the final script so it can be reused each month with new transaction statements.

---

## Expected Outcome

The project should produce:

- A working transaction analysis script
- A summary of recurring charges
- A list of possible forgotten subscriptions
- Detection of duplicate payments
- Spending insights by category

Example findings:

- "Found a streaming subscription that has not been used."
- "Detected a duplicate payment made on the same day."
- "Identified recurring monthly charges totaling $45."

---

## Verification

The analysis should be manually verified using at least two known financial figures before trusting the complete results.

---

## Future Improvements

Potential enhancements include:

- Automatic PDF parsing
- Interactive spending dashboard
- Category prediction using machine learning
- Visualization of monthly spending trends
- Export reports to Excel or CSV
- Email alerts for new recurring subscriptions

---

## Deliverables

- Transaction analysis script
- Verification results
- Plain-English explanation of the algorithm
- Monthly reusable workflow
