import sys

sys.stdout.reconfigure(encoding="utf-8")


def demonstrate_loops():
    """Demonstrate different loop types using a school attendance scenario."""

    # This list stores all students in one class and is used by multiple attendance tasks.
    student_names = [
        "Aarav",
        "Diya",
        "Kabir",
        "Meera",
        "Rohan",
        "Anaya",
        "Vivaan",
        "Ishita",
        "Arjun",
        "Saanvi",
    ]

    # This list stores today's attendance as 1 (Present) and 0 (Absent) for each student.
    daily_attendance_flags = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

    # This list maps each weekday to support weekly attendance reporting.
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # This 5x10 grid stores weekly attendance (P/A) for 5 days and 10 students.
    weekly_attendance_grid = [
        ["P", "P", "A", "P", "A", "P", "P", "P", "A", "P"],
        ["P", "A", "P", "P", "P", "P", "A", "P", "P", "P"],
        ["A", "P", "P", "P", "A", "P", "P", "P", "P", "P"],
        ["P", "P", "P", "A", "P", "P", "P", "A", "P", "P"],
        ["P", "P", "A", "P", "P", "A", "P", "P", "P", "P"],
    ]

    # This heading separates the first loop output from others for better readability.
    print(f"{'=' * 70}")
    print(f"FOR LOOP: PRINT EACH STUDENT NAME")
    print(f"{'=' * 70}")

    # FOR LOOP: We use a for loop to visit each student name one by one from a known list.
    for student_name in student_names:
        print(f"Student Name: {student_name}")

    # This heading separates the second loop output from others for better readability.
    print(f"\n{'=' * 70}")
    print(f"WHILE LOOP: COUNT ABSENT STUDENTS UNTIL ALERT LIMIT")
    print(f"{'=' * 70}")

    # This list collects names of students who are absent today.
    absent_student_names = [
        student_names[index]
        for index, attendance_count in enumerate(daily_attendance_flags)
        if attendance_count == 0
    ]

    # These variables track absent counting and stop when a threshold is reached.
    absent_limit = 2
    absent_count = 0

    # WHILE LOOP: We use while because counting should continue only until a condition is met.
    while absent_count < len(absent_student_names) and absent_count < absent_limit:
        print(
            f"Absent Student {absent_count + 1}: {absent_student_names[absent_count]}"
        )
        absent_count += 1

    print(f"Absent counting stopped at limit: {absent_limit}")

    # This heading separates the third loop output from others for better readability.
    print(f"\n{'=' * 70}")
    print(f"FOR LOOP WITH RANGE(): PRINT ROLL NUMBERS 1 TO 10")
    print(f"{'=' * 70}")

    # FOR WITH RANGE: We use range when roll numbers are sequential numeric values.
    for roll_number in range(1, 11):
        print(f"Roll Number: {roll_number}")

    # This heading separates the fourth loop output from others for better readability.
    print(f"\n{'=' * 70}")
    print(f"NESTED LOOP: WEEKLY ATTENDANCE GRID (5 DAYS x 10 STUDENTS)")
    print(f"{'=' * 70}")

    # This prints the table title and border using '=' as requested.
    print(f"{'=' * 46}")
    print(f"WEEKLY ATTENDANCE REPORT")
    print(f"{'=' * 46}")

    # This builds the header row with roll numbers for all 10 students.
    header_row = "Day       "
    for roll_number in range(1, 11):
        header_row += f"S{roll_number:02d} "
    print(f"{header_row}")

    # This prints a separator line using '-' as requested.
    print(f"{'-' * 46}")

    # NESTED LOOP: Outer loop moves day by day, inner loop prints each student's attendance.
    for day_index, week_day in enumerate(week_days):
        day_row = f"{week_day:<9} "
        for student_index in range(len(student_names)):
            attendance_count = weekly_attendance_grid[day_index][student_index]
            day_row += f"{attendance_count:^3}"
        print(f"{day_row}")

    # This prints the closing border of the table.
    print(f"{'=' * 46}")

    # These values are used for final summary based on today's attendance.
    total_students = len(student_names)
    total_present = sum(daily_attendance_flags)
    total_absent = total_students - total_present
    attendance_rate = (total_present / total_students) * 100

    # This heading presents the final attendance summary clearly.
    print(f"\n{'=' * 70}")
    print(f"FINAL ATTENDANCE SUMMARY")
    print(f"{'=' * 70}")
    print(f"Total Students  : {total_students}")
    print(f"Total Present   : {total_present}")
    print(f"Total Absent    : {total_absent}")
    print(f"Attendance Rate : {attendance_rate:.2f}%")


if __name__ == "__main__":
    # Main block ensures this demo runs only when this file is executed directly.
    demonstrate_loops()



Role:
Senior Python Developer, 20+ years experience, beginner-friendly code.

Task:
Generate 100% compilable Python program named "GHC13 - loop_demo.py"
with function "demonstrate_loops".

Scenario:
A school attendance system that uses different types of loops
to mark attendance, count present students, print roll numbers,
and generate a weekly attendance report.

Conditions / Requirements:
1. Demonstrate all 4 loop types with real school data:
     for loop          → Print each student name from a list
     while loop        → Count absent students until limit reached
     for with range()  → Print roll numbers 1 to 10
     nested loop       → Print weekly attendance grid
                         (5 days x 10 students)
2. Each loop must solve a real attendance related problem.
3. Every loop must have a comment explaining what it is
   doing and why this loop type is used here.
4. Print output of every loop with a clear heading.
5. Use real school variable names like student_name,
   roll_number, attendance_count, week_day and so on.
6. Use f-strings for all print statements.
7. Final summary must show:
     Total Students    → count
     Total Present     → count
     Total Absent      → count
     Attendance Rate   → percentage with 2 decimal places

Rules:
1. Must compile and run in Python 3 without errors.
2. Add at top: import sys / sys.stdout.reconfigure(encoding='utf-8')
3. No external libraries, built-in only.
4. Clean indentation and comments on every block.
5. Main block inside if __name__ == "__main__".
6. Use = and - for table borders.
