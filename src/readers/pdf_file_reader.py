from pypdf import PdfReader
from readers.file_reader import FileReader


class PdfFileReader(FileReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_file(self):
        reader = PdfReader(self.file_path)
        file_content = ""

        for page in reader.pages:
            page_content = page.extract_text()
            file_content += page_content

        return file_content
