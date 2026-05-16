import sys
sys.stdout.reconfigure(encoding='utf-8')

# ============================================================
# GHC12 - condition_checker.py
# Hospital Patient Admission System — Condition Checker
# ============================================================


def check_conditions(patient_name, age, systolic_bp, sugar_level, spo2_level, is_insurance_valid):
    """
    Checks all 5 admission conditions for a hospital patient.
    Returns True if all conditions pass, False otherwise.
    """

    print("=" * 60)
    print(f"  HOSPITAL PATIENT ADMISSION SYSTEM")
    print(f"  Patient : {patient_name}")
    print("=" * 60)

    # Dictionary to store results of each condition check
    results = {}

    # ----------------------------------------------------------
    # Condition 1: Age Check (valid range: 1 to 120)
    # ----------------------------------------------------------
    print("\n[Checking Condition 1] Age Verification")
    if 1 <= age <= 120:
        age_status = "PASS"
        age_reason = f"Age {age} is within the valid range (1–120)."
        print(f"  PASS — {age_reason}")
    else:
        age_status = "FAIL"
        age_reason = f"Age {age} is outside the valid range (1–120)."
        print(f"  FAIL — {age_reason}")
    results["Age Check"] = age_status

    # ----------------------------------------------------------
    # Condition 2: Blood Pressure Check (normal: 80 to 120 mmHg)
    # ----------------------------------------------------------
    print("\n[Checking Condition 2] Blood Pressure (Systolic)")
    if 80 <= systolic_bp <= 120:
        bp_status = "PASS"
        bp_reason = f"Systolic BP {systolic_bp} mmHg is normal (80–120 mmHg)."
        print(f"  PASS — {bp_reason}")
    elif systolic_bp < 80:
        bp_status = "FAIL"
        bp_reason = f"Systolic BP {systolic_bp} mmHg is too low (below 80 mmHg). Risk of hypotension."
        print(f"  FAIL — {bp_reason}")
    else:
        bp_status = "FAIL"
        bp_reason = f"Systolic BP {systolic_bp} mmHg is too high (above 120 mmHg). Risk of hypertension."
        print(f"  FAIL — {bp_reason}")
    results["Blood Pressure"] = bp_status

    # ----------------------------------------------------------
    # Condition 3: Sugar Level Check (normal: 70 to 140 mg/dL)
    # ----------------------------------------------------------
    print("\n[Checking Condition 3] Blood Sugar Level")
    if 70 <= sugar_level <= 140:
        sugar_status = "PASS"
        sugar_reason = f"Sugar level {sugar_level} mg/dL is normal (70–140 mg/dL)."
        print(f"  PASS — {sugar_reason}")
    elif sugar_level < 70:
        sugar_status = "FAIL"
        sugar_reason = f"Sugar level {sugar_level} mg/dL is too low (below 70 mg/dL). Risk of hypoglycemia."
        print(f"  FAIL — {sugar_reason}")
    else:
        sugar_status = "FAIL"
        sugar_reason = f"Sugar level {sugar_level} mg/dL is too high (above 140 mg/dL). Risk of hyperglycemia."
        print(f"  FAIL — {sugar_reason}")
    results["Sugar Level"] = sugar_status

    # ----------------------------------------------------------
    # Condition 4: Oxygen (SpO2) Level Check (safe: 95% or above)
    # ----------------------------------------------------------
    print("\n[Checking Condition 4] Oxygen Saturation (SpO2)")
    if spo2_level >= 95:
        spo2_status = "PASS"
        spo2_reason = f"SpO2 level {spo2_level}% is safe (>= 95%)."
        print(f"  PASS — {spo2_reason}")
    elif 90 <= spo2_level < 95:
        spo2_status = "FAIL"
        spo2_reason = f"SpO2 level {spo2_level}% is low (90–94%). Mild hypoxia detected."
        print(f"  FAIL — {spo2_reason}")
    else:
        spo2_status = "FAIL"
        spo2_reason = f"SpO2 level {spo2_level}% is critically low (below 90%). Severe hypoxia."
        print(f"  FAIL — {spo2_reason}")
    results["Oxygen (SpO2)"] = spo2_status

    # ----------------------------------------------------------
    # Condition 5: Insurance Validity Check (must be True)
    # ----------------------------------------------------------
    print("\n[Checking Condition 5] Insurance Validity")
    if is_insurance_valid:
        insurance_status = "PASS"
        insurance_reason = "Insurance is valid. Cashless admission available."
        print(f"  PASS — {insurance_reason}")
    else:
        insurance_status = "FAIL"
        insurance_reason = "Insurance is not valid. Cashless admission unavailable."
        print(f"  FAIL — {insurance_reason}")
    results["Insurance Valid"] = insurance_status

    # ----------------------------------------------------------
    # Final Report Table
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print(f"  FINAL ADMISSION REPORT — {patient_name}")
    print("=" * 60)
    print(f"  {'Condition':<22} {'Status':>6}")
    print("-" * 60)

    for condition, status in results.items():
        # Align status column for a clean table layout
        print(f"  {condition:<22} {status:>6}")

    print("-" * 60)

    # ----------------------------------------------------------
    # Overall Admission Decision
    # ----------------------------------------------------------
    all_passed = all(status == "PASS" for status in results.values())

    if all_passed:
        print(f"\n  OVERALL STATUS : ALL PASS")
        print(f"  >>> Patient Admitted Successfully <<<")
    else:
        failed = [cond for cond, status in results.items() if status == "FAIL"]
        print(f"\n  OVERALL STATUS : FAIL ({len(failed)} condition(s) not met)")
        print(f"  >>> Admission On Hold — Check Report <<<")

    print("=" * 60)

    return all_passed


# ==============================================================
# Main block — Test cases with different patient scenarios
# ==============================================================
if __name__ == "__main__":

    # ----------------------------------------------------------
    # Test Case 1: Healthy patient with valid insurance — ALL PASS
    # ----------------------------------------------------------
    print("\n" + "#" * 60)
    print("  TEST CASE 1 — Healthy Patient, Valid Insurance")
    print("#" * 60)
    check_conditions(
        patient_name       = "Amit Sharma",
        age                = 35,
        systolic_bp        = 110,   # mmHg — normal
        sugar_level        = 95,    # mg/dL — normal
        spo2_level         = 98,    # % — safe
        is_insurance_valid = True
    )

    # ----------------------------------------------------------
    # Test Case 2: High BP and low oxygen — SOME FAIL
    # ----------------------------------------------------------
    print("\n" + "#" * 60)
    print("  TEST CASE 2 — High BP and Low Oxygen")
    print("#" * 60)
    check_conditions(
        patient_name       = "Sunita Rao",
        age                = 62,
        systolic_bp        = 145,   # mmHg — hypertension
        sugar_level        = 110,   # mg/dL — normal
        spo2_level         = 91,    # % — mild hypoxia
        is_insurance_valid = True
    )

    # ----------------------------------------------------------
    # Test Case 3: Invalid age and no insurance — MULTIPLE FAIL
    # ----------------------------------------------------------
    print("\n" + "#" * 60)
    print("  TEST CASE 3 — Invalid Age, No Insurance")
    print("#" * 60)
    check_conditions(
        patient_name       = "Unknown Patient",
        age                = 0,     # invalid age
        systolic_bp        = 100,   # mmHg — normal
        sugar_level        = 50,    # mg/dL — hypoglycemia
        spo2_level         = 97,    # % — safe
        is_insurance_valid = False  # no insurance
    )

Role:
Senior Python Developer, 20+ years experience, beginner-friendly code.

Task:
Generate 100% compilable Python program named "GHC12 - condition_checker.py"
with function "check_conditions".

Scenario:
A hospital patient admission system that checks multiple conditions
before admitting a patient — age, blood pressure, sugar level,
oxygen level, and insurance validity.

Conditions / Requirements:
1. Check all 5 conditions using if, elif, else:
     Age Check         → Patient must be between 1 and 120
     Blood Pressure    → Normal if between 80 and 120
     Sugar Level       → Normal if between 70 and 140
     Oxygen Level      → Safe if 95% or above
     Insurance Valid   → Must be True to get cashless admission
2. Each condition must print PASS or FAIL with reason.
3. At the end print overall admission status:
     ALL PASS  → "Patient Admitted Successfully"
     ANY FAIL  → "Admission On Hold — Check Report"
4. Use real medical variable names like systolic_bp,
   sugar_level, spo2_level and so on.
5. Use f-strings for all print statements.
6. Show a final report table with all condition results.
7. Test with 2 patients — one ALL PASS and one with FAIL.

Rules:
1. Must compile and run in Python 3 without errors.
2. Add at top: import sys / sys.stdout.reconfigure(encoding='utf-8')
3. No external libraries, built-in only.
4. Clean indentation and comments on every block.
5. Main block inside if __name__ == "__main__".
6. Use = and - for table borders.


