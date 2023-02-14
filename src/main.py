from collections import defaultdict

with open("./books/frankenstein.txt") as file:
    book_content = file.read()


book_words = book_content.split()


def generate_letter_appear_log(content: str):
    letter_log = defaultdict(int)

    for letter in content:
        if letter.isalpha():
            letter_log[letter.lower()] += 1

    return letter_log


book_log = generate_letter_appear_log(book_content)
book_log_sorted = {key: book_log[key] for key in sorted(book_log)}

print(
    "---- Begin report of the book ----\n"
    + f"{len(book_words)} words found in the book\n\n"
)

for key in book_log_sorted:
    print(f"The character {key} was found {book_log[key]} times in the book")
