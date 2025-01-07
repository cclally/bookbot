def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_chars = get_char_count(text)
    chars_dict = get_chars_dict(text)

    print(num_words)
    print(num_chars)
    print(chars_dict)

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