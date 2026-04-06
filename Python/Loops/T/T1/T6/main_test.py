from main import *

run_cases = [
    (45, False, "fighting"),
    (12, True, "safe to attack"),
    (10, False, "enraged"),
]

submit_cases = run_cases + [
    (0, False, "defeated"),
    (20, False, "fighting"),
    (75, True, "safe to attack"),
]


def test(health, is_stunned, expected_output):
    print("---------------------------------")
    print(f"Input health:     {health}")
    print(f"Input is_stunned: {is_stunned}")
    print("")
    result = get_boss_state(health, is_stunned)
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
