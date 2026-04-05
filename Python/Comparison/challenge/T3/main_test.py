from main import *

run_cases = [
    ((1, 0, 1), (5, True)),
    ((1, 1, 1), (7, True)),
    ((0, 1, 0), (2, True)),
]

submit_cases = run_cases + [
    ((0, 0, 0), (0, False)),
    ((1, 0, 0), (4, True)),
    ((0, 0, 1), (1, True)),
]


def test(bits, expected_output):
    read_bit, write_bit, execute_bit = bits
    print("---------------------------------")
    print(f"Input bits: read={read_bit}, write={write_bit}, execute={execute_bit}")
    print("")
    result = decode_permission_bits(read_bit, write_bit, execute_bit)
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
