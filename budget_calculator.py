# Budget Calculator
# Author: Carrington Davis
# Description: Monthly Budget Calculator with custom categories + input validation

# helper: calculate percentages
def calc_percent(amount, income):
    """Return the percent of income spent on a category."""
    return (amount / income) * 100 if income > 0 else 0.0

# helper: safe numeric input (non-negative)
def get_number(prompt):
    """Keep asking until user enters a valid non-negative number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# === Inputs ===
income = get_number("Enter your monthly income: ")

# how many categories
while True:
    try:
        num_categories = int(input("How many expense categories do you want to enter? "))
        if num_categories < 0:
            print("Please enter 0 or a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number (e.g., 4).")

# collect categories
categories = {}  # preserves insertion order
for i in range(1, num_categories + 1):
    name = input(f"Enter name for category #{i}: ").strip()
    if not name:
        name = f"Category {i}"
    amount = get_number(f"Enter monthly amount for '{name}': ")
    categories[name] = amount

# === Calculations ===
total_expenses = sum(categories.values())
savings = abs(income - total_expenses)  # keep abs() to satisfy the assignment
total_percent = calc_percent(total_expenses, income)
percents = {k: calc_percent(v, income) for k, v in categories.items()}

# === Output ===
print("\n== Monthly Budget Report ==")
print(f"{'Total Monthly Income':<25}: ${income:,.2f}")
print(f"{'Total Monthly Expenses':<25}: ${total_expenses:,.2f}")
print(f"{'Total Monthly Savings':<25}: ${savings:,.2f}")

# dynamic label width so columns line up nicely
label_width = max(15, *(len(k) for k in categories.keys())) if categories else 15

print("\n-- Percentage Breakdown of Income --")
if not categories:
    print("(No categories entered.)")
else:
    for name, pct in percents.items():
        print(f"{name:<{label_width}}: {pct:.2f}% of income")
    print(f"{'Total Expenses':<{label_width}}: {total_percent:.2f}% of income")
