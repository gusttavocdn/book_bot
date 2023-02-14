import os
from readers.pdf_file_reader import PdfFileReader
from readers.text_file_reader import TextFileReader


class FileContentReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        _, file_extension = os.path.splitext(self.file_path)
        reader = self._get_reader_for_extension(file_extension)
        return reader.read_file()

    def _get_reader_for_extension(self, file_extension):
        if file_extension == ".txt":
            return TextFileReader(self.file_path)
        elif file_extension == ".pdf":
            return PdfFileReader(self.file_path)
        else:
            raise ValueError("Unsupported file type")
