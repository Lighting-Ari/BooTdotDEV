from main import *

run_cases = [
    ("Ari", 12, 3, (15, "Ari scored 15 points")),
    ("Mina", 9, 0, (9, "Mina scored 9 points")),
]

submit_cases = run_cases + [
    ("Bo", 0, 0, (0, "Bo scored 0 points")),
    ("Luna", 7, 8, (15, "Luna scored 15 points")),
    ("Zed", 21, 4, (25, "Zed scored 25 points")),
]


def test(player_name, base_score, bonus_score, expected_output):
    print("---------------------------------")
    print(f"Input player_name: {player_name}")
    print(f"Input base_score:  {base_score}")
    print(f"Input bonus_score: {bonus_score}")
    print("")
    result = get_final_score(player_name, base_score, bonus_score)
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
