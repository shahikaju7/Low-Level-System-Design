# Vending Machine System Design

## Purpose
Design a vending machine that supports multiple product slots, cash and card payment, change handling, stock management, and admin updates.

## Core Requirements
- The vending machine should have multiple slots, each holding a specific product.
- A customer can select a product and insert money to purchase it.
- The machine should return change if the customer inserts more money than the product price.
- If a product is out of stock, the machine should notify the customer.
- The machine should support multiple payment methods: cash and card.
- Admin should be able to restock products and update prices.

## Constraints
- A slot can hold only one type of product but multiple quantities.
- The machine should not dispense a product if inserted money is less than the price.
- Change can only be returned if the machine has enough coins/notes.
- Only admin can restock or update prices.

## Business Rules
- Only one product type per slot, but quantities may be greater than one.
- The machine must refuse dispensing if inserted money is less than the product price.
- Change is returned only if the machine has sufficient coins/notes in `cash_inventory`.
- Admin-only actions include restocking and price updates.

## Possible Improvements
- Add support for discounts and promotions.
- Add product selection by name or category.
- Add remote monitoring for stock levels.
- Add support for multiple card networks and mobile wallet payments.
- Add transaction logging for audit and analytics.
