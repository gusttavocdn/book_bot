from readers.file_reader import FileReader


class TextFileReader(FileReader):
    def read_file(self):
        with open(self.file_path, "r") as f:
            file_content = f.read()
        return file_content
