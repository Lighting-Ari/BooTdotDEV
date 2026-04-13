def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    unique = set()
    count = 0

    for i in text:
        if i in vowels:
            unique.add(i)
            count += 1
    return count, unique
        
