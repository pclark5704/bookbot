def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of",book_path," ---")
    print("There were",num_words,"words found in the document\n\n")
    character_times(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_times(counter_dict):
    sorted_dict = dict(sorted(counter_dict.items(), reverse=True, key=lambda item:item[1]))
    for character in sorted_dict:
        if character.isalpha() == True:
            print("The character",character,"occurs",sorted_dict[character],"times.")

main()