
def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words
path = "books/frankenstein.txt"
text = get_book_text(path)
        
from stats import count_characters

def main ():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    test = get_num_words(text)
    words = text.split()
    new_variable = count_characters(words)
    print(f"Found {test} total words")
    print(new_variable)

main()