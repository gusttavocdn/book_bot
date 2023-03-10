from collections import defaultdict
from unidecode import unidecode


class Analyzer:
    def __init__(self, content: str):
        self._content = content

    def generate_letters_log(self):
        letters_log = defaultdict(int)

        for letter in self._content:
            if letter.isalpha():
                normalized_letter = unidecode(letter.lower())
                letters_log[normalized_letter] += 1

        letters_log = self.__alphatize_letters_log(letters_log)
        return letters_log

    def __alphatize_letters_log(self, letters_log: dict):
        return {key: letters_log[key] for key in sorted(letters_log)}

    def count_words(self):
        words_count = len(self._content.split())
        return words_count

    def __str__(self) -> str:
        report = (
            "---- Begin report ----\n"
            f"{self.count_words()} words found in the text\n\n"
        )

        for key in self.generate_letters_log():
            report += (
                f"The character {key} was found "
                f"{self.generate_letters_log()[key]} times in the text\n"
            )

        return report
