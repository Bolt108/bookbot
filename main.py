import sys
from stats import get_num_words, get_char_count, sorted_list_of_dicts

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]
    total_words = get_num_words(get_book_text(book_file_path))
    char_count = get_char_count(get_book_text(book_file_path))
    sorted_char_count = sorted_list_of_dicts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()