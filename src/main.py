from analyzer import Analyzer
from readers.file_content_reader import FileContentReader


content = FileContentReader("./books/Profile.pdf").read_file()

analyzer = Analyzer(content)

print(analyzer)
