from  project.utils.sentence_metrics import SentenceMetrics
import pytest


class TestSentenceMetrics():
    """Class to test SentenceMetrics static methods
    """

    @pytest.mark.parametrize("sentences, expected_counted_words", [
        ("", 0),
        ("a", 1),
        ("Bob ddas 3231 ewew", 3),
        (" This is - a self-explained example ", 5),
        ("Changes in Need for Uniqueness From 2000 Until 2020", 7),
        (" ·$'·$$ hola", 1)
    ])
    def test_count_words(this,sentences:str,expected_counted_words:int):
        """Method to test count_words static method

        Args:
            sentences (str): possible sentences
            expected_counted_words (int): expected count of words in the sentence
        """
        assert SentenceMetrics.get_count_words(sentences) == expected_counted_words



    @pytest.mark.parametrize("possible_sentences, expected_number", [
        ("", "0"),
        ("324 dsadasdas", "324"),
        ("a ew 21 asdad", "21"),
        (" 23 comments ", "23"),
        (" 43432432", "43432432"),
        ("231 23 ", "23123")
    ])
    def test_get_number_from_sentence(this,possible_sentences:str,expected_number:int):
        """Method to test static method get_number_from_sentence

        Args:
            possible_sentences (str): possible sentences
            expected_number (int): expected number detected in the sentence
        """
        assert SentenceMetrics.get_number_from_sentence(possible_sentences) == expected_number