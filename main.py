def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_chars = get_char_count(text)
    chars_dict = get_chars_dict(text)

    list_of_dicts = [{'char': key, 'num': value} for key, value in chars_dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)

    print("--- Begin report of", book_path, "---")
    print(num_words, "words found in", book_path)
    print(num_chars, "total characters found in", book_path, '\n')

    for d in list_of_dicts:
        if (d["char"].isalpha()):
            print("The",'\'' + d["char"] + '\'', "character was found", d["num"], "times")
        else:
            None

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    count = 0

    for t in text:
        count += 1
    return count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()