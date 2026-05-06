import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words
#path = "books/frankenstein.txt"
#text = get_book_text(path)
        
from stats import count_characters, sort_on, chars_dict_to_sorted_list

def main ():
    #path = "books/frankenstein.txt"
    
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book> ")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    test = get_num_words(text)
    words = text.split()
    new_variable = count_characters(words)
    sorted_chars = chars_dict_to_sorted_list(new_variable)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {test} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()