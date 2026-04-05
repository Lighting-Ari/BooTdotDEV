from main import *

run_cases = [
    (13, 145, False, True),
    (11, 145, False, False),
    (15, 150, True, False),
]

submit_cases = run_cases + [
    (12, 140, False, True),
    (12, 139, False, False),
    (16, 170, False, True),
]


def test(age, height_cm, is_vip_skip, expected_output):
    print("---------------------------------")
    print(f"Input age:        {age}")
    print(f"Input height_cm:  {height_cm}")
    print(f"Input is_vip_skip:{is_vip_skip}")
    print("")
    result = can_ride(age, height_cm, is_vip_skip)
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
