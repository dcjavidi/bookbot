import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def book():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    return text
from stats import num_words
from stats import count_characters
from stats import sort_characters
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
num_words(book())
print("--------- Character Count -------")
char_count = count_characters(book())
sorted_chars = sort_characters(char_count)
for char in sorted_chars:
    print(f"{char["char"]}: {char["num"]}")
print("============= END ===============")