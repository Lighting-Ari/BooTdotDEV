from main import *

run_cases = [
    (
        3,
        4,
        7,
        "Win points: 15\nQuest points: 8\nBonus points: 7\nTotal points: 30",
    ),
    (
        1,
        2,
        0,
        "Win points: 5\nQuest points: 4\nBonus points: 0\nTotal points: 9",
    ),
    (
        5,
        0,
        10,
        "Win points: 25\nQuest points: 0\nBonus points: 10\nTotal points: 35",
    ),
]

submit_cases = run_cases + [
    (
        0,
        0,
        0,
        "Win points: 0\nQuest points: 0\nBonus points: 0\nTotal points: 0",
    ),
    (
        0,
        6,
        3,
        "Win points: 0\nQuest points: 12\nBonus points: 3\nTotal points: 15",
    ),
    (
        8,
        9,
        4,
        "Win points: 40\nQuest points: 18\nBonus points: 4\nTotal points: 62",
    ),
]


def test(wins, quests, bonus_points, expected_output):
    print("---------------------------------")
    print(f"Input wins:         {wins}")
    print(f"Input quests:       {quests}")
    print(f"Input bonus_points: {bonus_points}")
    print("")
    result = build_reward_summary(wins, quests, bonus_points)
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
