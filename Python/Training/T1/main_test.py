from main import *

run_cases = [
    (50, 10, 1, 80),
    (120, 24, 0, 40),
    (75, 15, 2, 120),
]

submit_cases = run_cases + [
    (1, 8, 0, 1),
    (200, 40, 3, 160),
    (500, 100, 1, 80),
]


def test(file_size_mb, upload_speed_mbps, retry_count, expected_output):
    print("---------------------------------")
    print(f"Input file size (MB):    {file_size_mb}")
    print(f"Input speed (Mbps):      {upload_speed_mbps}")
    print(f"Input retry count:       {retry_count}")
    print("")
    result = estimate_upload_time(file_size_mb, upload_speed_mbps, retry_count)
    print(f"Expected seconds: {expected_output}")
    print(f"Actual seconds:   {result}")
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
