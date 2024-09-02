from  project.utils.word_metrics import WordMetrics
import pytest



class TestWordMetrics():
    """Class that tests WordMetrics methods
    """
    
    @pytest.mark.parametrize("maybe_with_alphaletter, expected_result", [
        ("", False),
        ("a", True),
        ("Bob", True),
        (" 43432432a ", True),
        (" 43432432", False),
        (" ·$'·$$ ", False),
        (" ·$'·$$ a", True)
    ])
    def test_check_alphaletter_in_word(this,maybe_with_alphaletter:str,expected_result:bool):
        """Test of the check_alphaletter_in_word static method

        Args:
            this (_type_): instance of the TestWordMetrics class
            maybe_with_alphaletter (str): possible words
            expected_result (bool): boolean with the expected result (if it has or not an alphaletter in the word)
        """
        assert WordMetrics.check_alphaletter_in_word(maybe_with_alphaletter) == expected_result

