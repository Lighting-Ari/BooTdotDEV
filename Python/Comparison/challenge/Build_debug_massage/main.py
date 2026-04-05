def build_test_header(suite_name):
    return f"=== Running: {suite_name} ==="


def build_failure_message(test_name, expected, actual):
    return f"Test: {test_name}\nExpected: {expected}\nActual: {actual}"
