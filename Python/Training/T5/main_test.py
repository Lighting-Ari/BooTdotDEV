from main import *

run_cases = [
    (["10", "5", "8"], 23),
    ([1, "2", None, "7"], 10),
    (["4", "bad", "6"], 10),
]

submit_cases = run_cases + [
    (["nope", None, "-", "3"], 3),
    (["12", 3, "4", "0"], 19),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print("")
    result = total_valid_numbers(input1)
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
