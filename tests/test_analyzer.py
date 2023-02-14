from src.analyzer import Analyzer


def test_analyzer_is_init_with_correct_attributes():
    """Test that Analyzer is initialized with correct attributes."""
    test_phrase = "Essa é uma frase de teste"
    sut = Analyzer(test_phrase)

    assert sut._content == test_phrase


def test_analyzer_generate_letters_log():
    """Test that Analyzer generate_letters_log method works correctly."""
    test_phrase = "Essa é uma frase de teste"
    sut = Analyzer(test_phrase)

    assert sut.generate_letters_log() == {
        "a": 3,
        "d": 1,
        "e": 6,
        "f": 1,
        "m": 1,
        "r": 1,
        "s": 4,
        "t": 2,
        "u": 1,
    }


def test_analyzer_generate_letters_log_excluding_special_chars():
    """Test that Analyzer generate_letters_log method works correctly with
    special characters."""
    test_phrase = "This is a test phrase with !@#$%^&*()_+ special characters"
    sut = Analyzer(test_phrase)

    assert sut.generate_letters_log() == {
        "a": 5,
        "c": 3,
        "e": 4,
        "h": 4,
        "i": 4,
        "l": 1,
        "p": 2,
        "r": 3,
        "s": 6,
        "t": 5,
        "w": 1,
    }


def test_analyzer_count_words():
    """Test that Analyzer count_words method works correctly."""
    test_phrase = "This is a test phrase with !@#$%^&*()_+ special characters"
    sut = Analyzer(test_phrase)

    assert sut.count_words() == 9
