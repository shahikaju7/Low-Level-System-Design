# Bank and ATM System Design

## Purpose
Design a banking system that supports customer accounts, transactions, and ATM operations with secure PIN verification.

## Core Requirements
- A customer can create a bank account and check their balance.
- A customer can deposit and withdraw money from their account.
- A customer can transfer money to another account.
- An ATM should allow a customer to log in with card number and PIN.
- The ATM should support withdraw, deposit, check balance, and transfer operations.
- Each transaction should be recorded with amount, type, and timestamp.
- An account should not allow withdrawal if balance is insufficient.

## Constraints
- A customer can have multiple accounts (savings, current).
- PIN must be verified before any ATM operation.
- Withdrawal cannot exceed available balance.
- Every operation (deposit, withdraw, transfer) creates a transaction record.


## Business Rules
- ATM operations require successful PIN verification.
- Withdrawals fail if the account balance is insufficient.
- Transfers move funds from one account to another only when sufficient balance exists.
- All account-changing actions create transaction history entries.

## Possible Improvements
- Add account statement generation.
- Add support for account closing and reopening.
- Add multi-factor authentication for ATM login.
- Add overdraft protection or daily withdrawal limits.
- Add transaction rollback for failed transfers.
