def get_num_words(text):
    words = text.split()
    return len(words)

#from main import text

#words = text.split()

def count_characters(words):
    characters = {}
    for word in words :
        for char in word:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else :
                characters[char] = 1
    return characters


def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(characters):
    result = []

    for char in characters:
        result.append({
            "char": char,
            "num": characters[char]
        })

    result.sort(reverse=True, key=sort_on)
    return result