from main import build_seat_map


run_cases = [
    (
        ["A", "B"],
        4,
        ["A2", "B4"],
        "A1 X A3 A4\nB1 B2 B3 X",
    ),
    (
        ["VIP"],
        3,
        [],
        "VIP1 VIP2 VIP3",
    ),
]

submit_cases = run_cases + [
    (
        [],
        5,
        ["A1"],
        "",
    ),
    (
        ["C"],
        2,
        ["C3", "Z9"],
        "C1 C2",
    ),
    (
        ["A", "B", "C"],
        3,
        ["A1", "B2", "C3"],
        "X A2 A3\nB1 X B3\nC1 C2 X",
    ),
]


def format_input(row_labels, seats_per_row, blocked_seats):
    lines = []
    lines.append(f"Rows: {row_labels}")
    lines.append(f"Seats per row: {seats_per_row}")
    lines.append(f"Blocked seats: {blocked_seats}")
    return "\n".join(lines)


def test(row_labels, seats_per_row, blocked_seats, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_input(row_labels, seats_per_row, blocked_seats))
    print("")
    result = build_seat_map(row_labels, seats_per_row, blocked_seats)
    print("Expected:")
    print(expected_output)
    print("Actual:")
    print(result)
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
