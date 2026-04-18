from main import *

run_cases = [
    (
        {"apples": 3, "bread": 2},
        "apples",
        1,
        "Inventory Report\n- apples: 4\n- bread: 2\nTotal items: 6",
    ),
    (
        {"carrots": 5},
        "milk",
        2,
        "Inventory Report\n- carrots: 5\n- milk: 2\nTotal items: 7",
    ),
    (
        {"tea": 1, "rice": 4, "beans": 2},
        "rice",
        3,
        "Inventory Report\n- tea: 1\n- rice: 7\n- beans: 2\nTotal items: 10",
    ),
]

submit_cases = run_cases + [
    (
        {},
        "soap",
        4,
        "Inventory Report\n- soap: 4\nTotal items: 4",
    ),
    (
        {"eggs": 0, "jam": 2},
        "eggs",
        0,
        "Inventory Report\n- eggs: 0\n- jam: 2\nTotal items: 2",
    ),
    (
        {"pens": 6, "paper": 10, "folders": 3},
        "markers",
        5,
        "Inventory Report\n- pens: 6\n- paper: 10\n- folders: 3\n- markers: 5\nTotal items: 24",
    ),
]


def test(inventory, delivered_item, delivered_amount, expected_output):
    print("---------------------------------")
    print("Input inventory:")
    if len(inventory) == 0:
        print("  {}")
    else:
        for item_name in inventory:
            print(f"  - {item_name}: {inventory[item_name]}")
    print(f"Delivered item:   {delivered_item}")
    print(f"Delivered amount: {delivered_amount}")
    print("")
    result = build_inventory_report(inventory, delivered_item, delivered_amount)
    print("Expected:")
    print(expected_output)
    print("")
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
