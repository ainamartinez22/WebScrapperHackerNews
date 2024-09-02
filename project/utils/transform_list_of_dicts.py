from project.utils.sentence_metrics import SentenceMetrics

class FilterListOfDicts():
    """Class that contains some methods that filter a list of dictionaries

    Returns:
        list of dicts
    """

    @staticmethod
    def filter_lte_number_words(info:list,number:int,field:str):
        """Function that return a list of dicts filtered by a value of a field that has to have a count of words lower than or equal to a number

        Args:
            info (list): list of dicts you want to filter
            number (int): number with which you will compare the number of words
            field (str): field from the list of dicts

        Returns:
            list of dicts: the result filtered
        """
        return [item for item in info if SentenceMetrics.get_count_words(item[field]) <= number] 

    @staticmethod
    def filter_gt_number_words(info:list,number:int,field:str):
        """Function that return a list of dicts filtered by a value of a field that has to have a count of words greater than a number

        Args:
            info (list): list of dicts you want to filter
            number (int): number with which you will compare the number of words
            field (str): field from the list of dicts

        Returns:
            list of dicts: the result filtered
        """
        return [item for item in info if SentenceMetrics.get_count_words(item[field]) > number] 



    







