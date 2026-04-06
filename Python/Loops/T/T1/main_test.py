from main import *

run_cases = [
    (30, 20, 5, 3, False, True),
    (10, 20, 5, 3, False, False),
    (50, 10, 7, 7, False, True),
]

submit_cases = run_cases + [
    (20, 20, 5, 5, True, False),
    (20, 20, 4, 5, False, False),
    (100, 25, 10, 2, False, True),
]


def test(mana, spell_cost, level, required_level, is_silenced, expected_output):
    print("---------------------------------")
    print(f"Input mana:           {mana}")
    print(f"Input spell_cost:     {spell_cost}")
    print(f"Input level:          {level}")
    print(f"Input required_level: {required_level}")
    print(f"Input is_silenced:    {is_silenced}")
    print("")
    result = can_cast_spell(mana, spell_cost, level, required_level, is_silenced)
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
