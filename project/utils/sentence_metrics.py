from project.utils.word_metrics import WordMetrics

class SentenceMetrics():
    """Class that contains some methods that return some metrics from a sentence
    """
    @staticmethod
    def get_count_words(sentence:str):
        """Returns the number of words in a sentence (with minimum one alpha letter to be a word)

        Args:
            sentence (str): any sentence

        Returns:
            number (int): the count of words
        """
        return len([word for word in sentence.split(' ') if WordMetrics.check_alphaletter_in_word(word)])

    @staticmethod
    def get_number_from_sentence(sentence:str):
        """Returns the number from a sentence

        Args:
            sentence (str): any sentence

        Returns:
            number(int): the number that it's inside the sentence
        """
        return '0' if (''.join(map(str,[int(i) for i in sentence.split() if i.isdigit()]))).strip()=='' else (''.join(map(str,[int(i) for i in sentence.split() if i.isdigit()]))).strip()
