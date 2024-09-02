class WordMetrics():

    @staticmethod
    def check_alphaletter_in_word(word:str):
        """Function that checks if there is any alpha letter in a word

        Args:
            word (str): any word

        Returns:
            boolean: True or False
        """
        for letter in word:
            if letter.isalpha():
                return True
        return False