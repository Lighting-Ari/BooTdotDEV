from main import *

run_cases = [
    (1, "1"),
    (4, "1\n12\n123\n1234"),
]

submit_cases = [
    (0, ""),
    (1, "1"),
    (4, "1\n12\n123\n1234"),
    (2, "1\n12"),
    (5, "1\n12\n123\n1234\n12345"),
]


def test(height, expected_output):
    print("---------------------------------")
    print(f"Input height: {height}")
    print("")
    result = build_number_ladder(height)
    print("Expected:")
    print(repr(expected_output))
    print("Actual:")
    print(repr(result))
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
