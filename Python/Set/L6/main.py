def find_missing_ids(first_ids, second_ids):
    missing_ids = set(first_ids) - set(second_ids)
    return missing_ids
