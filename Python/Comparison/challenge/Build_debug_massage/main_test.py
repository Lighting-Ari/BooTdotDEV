from main import *

run_cases = [
    ("build_test_header", ("Login Tests",), "=== Running: Login Tests ==="),
    (
        "build_failure_message",
        ("test_total", "42", "41"),
        "Test: test_total\nExpected: 42\nActual: 41",
    ),
]

submit_cases = run_cases + [
    ("build_test_header", ("",), "=== Running:  ==="),
    (
        "build_failure_message",
        ("test_name", "dragon", "dragn"),
        "Test: test_name\nExpected: dragon\nActual: dragn",
    ),
    (
        "build_failure_message",
        ("test_status", "ready now", "ready later"),
        "Test: test_status\nExpected: ready now\nActual: ready later",
    ),
]


def test(function_name, args, expected_output):
    print("---------------------------------")
    print(f"Function: {function_name}")
    print(f"Input: {args}")
    print("")

    if function_name == "build_test_header":
        result = build_test_header(*args)
    else:
        result = build_failure_message(*args)

    print(f"Expected: {repr(expected_output)}")
    print(f"Actual:   {repr(result)}")
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
