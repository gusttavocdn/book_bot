from analyzer import Analyzer

with open("./books/frankenstein.txt") as file:
    book_content = file.read()

analyzer = Analyzer(book_content)

print(analyzer)
