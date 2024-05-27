from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    count_characters(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    freq = {}
    text_lower = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
       freq[char] = text_lower.count(char)
    return(freq)

main()