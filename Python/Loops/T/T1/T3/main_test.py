from main import *

run_cases = [
    ("goAAAstopZZ", 3),
    ("abcDEFghI", 3),
    ("no caps here", 0),
]

submit_cases = run_cases + [
    ("A", 1),
    ("XYZabcQRSTUvw", 5),
    ("mix12ABCD!!EF", 4),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print("")
    result = longest_uppercase_streak(input1)
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
