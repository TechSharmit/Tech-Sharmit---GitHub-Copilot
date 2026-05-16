import sys
sys.stdout.reconfigure(encoding='utf-8')


def perform_math_operations():
    """Perform basic grocery-related math operations and print the results."""

    # Sample grocery values used across operations
    item_prices = [120.50, 85.75, 40.25, 210.00]
    paid_amount = 500.00
    quantity_of_rice_bags = 3
    unit_price_of_rice_bag = 62.00
    number_of_items = len(item_prices)
    number_of_friends = 4
    base_amount = 1000
    interest_periods = 2

    print("\n==================== GROCERY MATH CALCULATOR ====================")

    # 1) Addition: Add all item prices to find the total grocery bill
    total_bill = sum(item_prices)
    print(f"Addition (Total bill of all items): ₹{total_bill:.2f}")

    # 2) Subtraction: Subtract total bill from paid amount to find amount left after payment
    amount_left_after_payment = paid_amount - total_bill
    print(f"Subtraction (Amount left after payment): ₹{amount_left_after_payment:.2f}")

    # 3) Multiplication: Multiply quantity and unit price to get total price for rice bags
    total_rice_price = quantity_of_rice_bags * unit_price_of_rice_bag
    print(f"Multiplication (Total price = quantity x unit price): ₹{total_rice_price:.2f}")

    # 4) Division: Divide total bill by number of items to find average spend per item
    average_spend_per_item = total_bill / number_of_items
    print(f"Division (Average spend per item): ₹{average_spend_per_item:.2f}")

    # 5) Floor Division: Split total bill equally among friends using floor division for whole rupees
    equal_split_whole_rupees = int(total_bill) // number_of_friends
    print(f"Floor Division (Equal split among friends): ₹{equal_split_whole_rupees:.2f}")

    # 6) Modulus: Find the remaining rupees after equal split among friends
    remaining_after_split = int(total_bill) % number_of_friends
    print(f"Modulus (Remaining amount after equal split): ₹{remaining_after_split:.2f}")

    # 7) Power: Raise base amount to interest periods as a simple power calculation example
    compound_power_value = base_amount ** interest_periods
    print(f"Power (Base amount raised to interest periods): ₹{compound_power_value:.2f}")

    # 8) Absolute: Get positive difference amount so difference is always shown as positive
    positive_difference_amount = abs(total_bill - paid_amount)
    print(f"Absolute (Always positive difference amount): ₹{positive_difference_amount:.2f}")

    print("\n========================= SUMMARY TABLE =========================")
    print("================================================================")
    print(f"{'Operation':<18} | {'Real-World Meaning':<45} | {'Result':>12}")
    print("----------------------------------------------------------------")
    print(f"{'Addition':<18} | {'Total bill of all items':<45} | ₹{total_bill:>11.2f}")
    print(f"{'Subtraction':<18} | {'Amount left after payment':<45} | ₹{amount_left_after_payment:>11.2f}")
    print(f"{'Multiplication':<18} | {'Total price = quantity x unit price':<45} | ₹{total_rice_price:>11.2f}")
    print(f"{'Division':<18} | {'Average spend per item':<45} | ₹{average_spend_per_item:>11.2f}")
    print(f"{'Floor Division':<18} | {'Equal split of bill among friends':<45} | ₹{equal_split_whole_rupees:>11.2f}")
    print(f"{'Modulus':<18} | {'Remaining amount after equal split':<45} | ₹{remaining_after_split:>11.2f}")
    print(f"{'Power':<18} | {'Base amount raised to periods':<45} | ₹{compound_power_value:>11.2f}")
    print(f"{'Absolute':<18} | {'Always positive difference amount':<45} | ₹{positive_difference_amount:>11.2f}")
    print("================================================================")


if __name__ == "__main__":
    perform_math_operations()


Role:
You are a Senior Python Developer with 20+ years of experience
in writing clean, simple, and beginner-friendly Python programs.
Task:
Generate a 100% compilable Python program named "GHC11 - basic_math_calculator.py"
with a function called "perform_math_operations".
This program should demonstrate how to ask Copilot to perform
basic math operations in a real-world scenario.
Program Name  : basic_math_calculator.py
Function Name : perform_math_operations
Scenario:
A grocery shop owner wants a simple calculator to perform
daily math operations like calculating total bill, finding
average spending, calculating discount amount, finding
remainder after splitting bill, and calculating power
for compound interest base.
Conditions / Requirements:
1.  Function must perform all 8 basic math operations:
      Addition       → Total bill of all items
      Subtraction    → Amount left after payment
      Multiplication → Total price = quantity x unit price
      Division       → Average spend per item
      Floor Division → Equal split of bill among friends
      Modulus        → Remaining amount after equal split
      Power          → Base amount raised to interest periods
      Absolute       → Always show positive difference amount
2.  Each operation must use real grocery related variable names
    like item_prices, total_bill, paid_amount and so on.
3.  Each operation must have a comment explaining what
    math operation is being performed and why.
4.  Print result of every operation with a clear label
    showing what the result represents in real world.
5.  All currency values must display with ₹ symbol.
6.  Use f-strings for all print statements.
7.  Add a final summary section that prints all results
    together in a formatted table.
Rules:
1.  Program must be 100% compilable and runnable in Python 3.
2.  Add this at the top of the program:
      import sys
      sys.stdout.reconfigure(encoding='utf-8')
3.  Use simple real-world variable names only.
4.  Every operation must be on a separate clearly commented block.
5.  No external libraries allowed, use only Python built-in math.
6.  Code must be clean, properly indented, and well commented.
7.  Main program must be inside if __name__ == "__main__" block.
8.  Do not use any complex logic, keep every operation simple
    and easy to understand for a beginner.
Output Format:
- Print each operation result as it is calculated.
- Print a final summary table at the end with all results.
- Use ₹ symbol for all currency values.
- Use = signs and - signs for table borders.
