def num_words(book):
    word_count = len(book.split())
    print(f"Found {word_count} total words")
    return
def count_characters(book):
    char_count = {}
    book_lower = book.lower()
    i = 0
    while i < len(book_lower):
         if book_lower[i] in char_count:
             char_count[book_lower[i]] = char_count[book_lower[i]] + 1
             i += 1
         else:
             char_count[book_lower[i]] = 1
             i += 1
    return char_count
def sort_characters(char_count):
    def sort_on(items):
        return items["num"]
    char_list = []
    for key, value in char_count.items():
        if isinstance(key, str) and key.isalpha():
            char_list.append({"char": key, "num": value})
    char_list.sort(reverse=True, key=sort_on)
    return char_list