import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# Program Name : inventory_slicer.py
# Scenario     : A supermarket inventory system that uses
#                list slicing with steps to extract specific
#                product records for restocking, auditing,
#                quality checks, and weekly reports.
# ============================================================


def analyze_inventory() -> None:
    """
    Analyzes supermarket inventory using multiple list
    slicing operations with start, stop, and step values
    to extract specific product subsets for different reports.
    """

    # ----------------------------------------------------------
    # Raw inventory data — 12 products with details
    # Index positions: 0 to 11
    # ----------------------------------------------------------
    products = [
        {"id":  1, "name": "Rice 5kg",          "stock": 120, "price": 350},
        {"id":  2, "name": "Wheat Flour 10kg",   "stock":  85, "price": 420},
        {"id":  3, "name": "Sugar 2kg",          "stock": 200, "price": 110},
        {"id":  4, "name": "Cooking Oil 1L",     "stock":  60, "price": 180},
        {"id":  5, "name": "Dal Chana 1kg",      "stock": 150, "price":  95},
        {"id":  6, "name": "Salt 1kg",           "stock": 300, "price":  25},
        {"id":  7, "name": "Tea Powder 500g",    "stock":  75, "price": 220},
        {"id":  8, "name": "Coffee 200g",        "stock":  40, "price": 380},
        {"id":  9, "name": "Biscuits 400g",      "stock": 180, "price":  60},
        {"id": 10, "name": "Noodles 200g",       "stock":  95, "price":  45},
        {"id": 11, "name": "Tomato Ketchup 1kg", "stock":  55, "price": 160},
        {"id": 12, "name": "Cheese 200g",        "stock":  30, "price": 280},
    ]

    # ----------------------------------------------------------
    # Slice 1: list[::2]
    # Every alternate product starting from index 0
    # Used for: Odd-position product audit (index 0,2,4,6,8,10)
    # ----------------------------------------------------------
    alternate_products = products[::2]

    print("=" * 60)
    print("  📋  SLICE 1 — Every Alternate Product [::2]")
    print("       (Picks index: 0, 2, 4, 6, 8, 10)")
    print("=" * 60)
    for p in alternate_products:
        print(f"  [{p['id']:>2}] {p['name']:<25} Stock: {p['stock']}")

    # ----------------------------------------------------------
    # Slice 2: list[1::2]
    # Every alternate product starting from index 1
    # Used for: Even-position product audit (index 1,3,5,7,9,11)
    # ----------------------------------------------------------
    alternate_products2 = products[1::2]

    print("\n" + "=" * 60)
    print("  📋  SLICE 2 — Alternate Product From Index 1 [1::2]")
    print("       (Picks index: 1, 3, 5, 7, 9, 11)")
    print("=" * 60)
    for p in alternate_products2:
        print(f"  [{p['id']:>2}] {p['name']:<25} Stock: {p['stock']}")

    # ----------------------------------------------------------
    # Slice 3: list[0:6]
    # First 6 products only (index 0 to 5)
    # Used for: First half shelf restocking report
    # ----------------------------------------------------------
    first_half = products[0:6]

    print("\n" + "=" * 60)
    print("  🛒  SLICE 3 — First 6 Products Only [0:6]")
    print("       (Picks index: 0, 1, 2, 3, 4, 5)")
    print("=" * 60)
    for p in first_half:
        print(f"  [{p['id']:>2}] {p['name']:<25} Price: ₹ {p['price']}")

    # ----------------------------------------------------------
    # Slice 4: list[6:]
    # All products from index 6 to end
    # Used for: Second half shelf restocking report
    # ----------------------------------------------------------
    second_half = products[6:]

    print("\n" + "=" * 60)
    print("  🛒  SLICE 4 — Last 6 Products Only [6:]")
    print("       (Picks index: 6, 7, 8, 9, 10, 11)")
    print("=" * 60)
    for p in second_half:
        print(f"  [{p['id']:>2}] {p['name']:<25} Price: ₹ {p['price']}")

    # ----------------------------------------------------------
    # Slice 5: list[-3:]
    # Last 3 products using negative index
    # Used for: Recently added products quick check
    # ----------------------------------------------------------
    last_three = products[-3:]

    print("\n" + "=" * 60)
    print("  🆕  SLICE 5 — Last 3 Products (Negative Index) [-3:]")
    print("       (Picks index: 9, 10, 11 = last 3)")
    print("=" * 60)
    for p in last_three:
        print(f"  [{p['id']:>2}] {p['name']:<25} Stock: {p['stock']}")

    # ----------------------------------------------------------
    # Slice 6: list[::-1]
    # Full list reversed using negative step
    # Used for: Reverse order stock display from last to first
    # ----------------------------------------------------------
    reversed_products = products[::-1]

    print("\n" + "=" * 60)
    print("  🔄  SLICE 6 — Full List Reversed [::-1]")
    print("       (Picks index: 11,10,9,8,7,6,5,4,3,2,1,0)")
    print("=" * 60)
    for p in reversed_products:
        print(f"  [{p['id']:>2}] {p['name']:<25} Stock: {p['stock']}")

    # ----------------------------------------------------------
    # Slice 7: list[10:2:-2]
    # From index 10, go backward to index 3, step -2
    # Used for: Reverse alternate product quality check
    # ----------------------------------------------------------
    reverse_alternate = products[10:2:-2]

    print("\n" + "=" * 60)
    print("  🔍  SLICE 7 — Reverse Alternate From Index 10 [10:2:-2]")
    print("       (Picks index: 10, 8, 6, 4)")
    print("=" * 60)
    for p in reverse_alternate:
        print(f"  [{p['id']:>2}] {p['name']:<25} Stock: {p['stock']}")

    # ----------------------------------------------------------
    # Slice 8: list[1:10:3]
    # From index 1 to 9, pick every 3rd product
    # Used for: Weekly sample check — every 3rd product
    # ----------------------------------------------------------
    every_third = products[1:10:3]

    print("\n" + "=" * 60)
    print("  📅  SLICE 8 — Every 3rd Product From Index 1 [1:10:3]")
    print("       (Picks index: 1, 4, 7)")
    print("=" * 60)
    for p in every_third:
        print(f"  [{p['id']:>2}] {p['name']:<25} Price: ₹ {p['price']}")

    print("=" * 60)


# -------------------------------------------------------
# Main Program
# -------------------------------------------------------
if __name__ == "__main__":
    analyze_inventory()


Role:
You are a Senior Python Developer and Technical Educator with 20+ years of
experience in explaining Python sequence operations, list slicing, step
arguments, index-based access, and memory-efficient iteration techniques
to beginners, junior developers, and non-technical audiences.

Task:
I have a Python program named "inventory_slicer.py".
In this program there is a function called "analyze_inventory".
This function uses multiple list slicing operations with start,
stop, and step arguments on a real-world inventory dataset to
extract specific subsets of product records.
Your task is to read every slicing operation carefully and explain
exactly how each slice works step by step in simple plain English.
Do not explain the full file, focus only on the slicing operations
inside the function "analyze_inventory".

Rules to Follow:
1. Use plain English only, avoid heavy technical jargon.
2. Do not skip any slicing operation, cover every single one
   in the same order as it appears in the code top to bottom.
3. For each slicing operation explain the start, stop, and step
   values one by one and what each value means.
4. Show the exact index positions that are picked by each slice
   using the actual data from the program.
5. Show the data BEFORE slicing and AFTER slicing using
   actual product names and values from the program.
6. Clearly explain what a negative step means and how it
   reverses the direction of slicing.
7. Clearly explain what a negative index means in slicing.
8. Do not modify or rewrite the function, only explain it as it is.
9. Keep your language simple enough for a 1st year programming student.
10. Do not assume anything that is not written in the function.

Output Requirements:
1. Purpose of This Function
   - Write 2 to 3 lines explaining what this function does
     overall in plain English.

2. How List Slicing Works — Quick Explanation
   - Explain in 3 to 4 lines what list[start:stop:step] means
     in simple plain English.
   - Explain what happens when start, stop, or step is omitted.

3. Slicing Operation Breakdown — For Every Slice
   - For each slicing operation write the following:
     a. Slice Number (Slice 1, Slice 2, Slice 3 ...)
     b. The exact slice syntax used
     c. Start value — what it means and where it begins
     d. Stop value  — what it means and where it ends
     e. Step value  — what it means and how it jumps
     f. Exact index positions picked from the list
     g. Data BEFORE slice (full list with index numbers)
     h. Data AFTER slice (only selected items)

4. Negative Slicing Explanation
   - Identify every slice that uses a negative index or
     negative step in this function.
   - Explain exactly how negative values work in each case.
   - Show the direction of traversal for negative step slices.

5. Real World Analogy
   - Give one real world analogy that explains how list slicing
     with steps works.
   - The analogy should be relatable to everyday life.

6. Important Logic and Special Handling
   - Mention any special decisions made in the slicing operations.
   - Example: why step 2 skips alternate items, why negative step
     reverses the list, why omitting start or stop uses the full
     range, why slice does not modify the original list.

Output Format:
- Use clear section headings for each of the 6 points above.
- Use bullet points inside each section.
- Keep the total explanation under 500 words.
- Do not write any code in the output, only plain English explanation.
