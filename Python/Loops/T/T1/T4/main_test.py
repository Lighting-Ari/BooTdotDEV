from main import *

run_cases = [
    ("member_card", "Lena", 40, "Night Owls | Lena | Bronze"),
    ("trial_card", "Pax", 650, "Trial Guild | Pax | Gold"),
]

submit_cases = run_cases + [
    ("badge_only", "", 99, "Bronze"),
    ("badge_only", "", 100, "Silver"),
    (
        "scope_check",
        "Mira",
        500,
        "Trial Guild | Mira | Gold\nNight Owls | Mira | Gold",
    ),
]


def test(case_type, name, points, expected_output):
    print("---------------------------------")
    print(f"Case type: {case_type}")
    print(f"Input name: {name}")
    print(f"Input points: {points}")
    print("")

    if case_type == "member_card":
        result = build_member_card(name, points)
    elif case_type == "trial_card":
        result = build_trial_card(name, points)
    elif case_type == "badge_only":
        result = get_badge_level(points)
    else:
        first = build_trial_card(name, points)
        second = build_member_card(name, points)
        result = first + "\n" + second

    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
