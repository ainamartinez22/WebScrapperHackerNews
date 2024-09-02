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


class SortListOfDicts():
    """Class that contains some methods that sort a list of dictionaries

    Returns:
        list of dicts
    """

    @staticmethod
    def sort_list_of_dicts(info:list, field: str, desc = False):
        """Function that sorts a list of dicts by a value field

        Args:
            info (list): list of dicts you want to sort
            field (str): field by the value of which you want to sort
            desc (bool, optional): sorting descending. Defaults to False (so descending).

        Returns:
            list of dicts: sorted
        """
        return sorted(info, key=lambda x: int(x[field]), reverse=desc)
    
    



    







