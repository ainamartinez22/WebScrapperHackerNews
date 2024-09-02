from  project.utils.transform_list_of_dicts import FilterListOfDicts, SortListOfDicts

class TestFilterListOfDicts():
    """Class to test the static methods of the class FilterListOfDicts"""

    def test_filter_lte_number_words(this):
        """This method tests the static method filter_lte_number_words"""

        list_of_dicts = [
        {
            "id": "41410684",
            "title": "Why You Should Learn Linux (As a Developer)",
            "score": "4",
            "comments": "0",
            "filter": "1"
        },
        {
            "id": "41409891",
            "title": "My life",
            "score": "21",
            "comments": "6",
            "filter": "1"
        },
        {
            "id": "41367658",
            "title": "BaseX – a highly W3C compliant XQuery processor",
            "score": "72",
            "comments": "1",
            "filter": "1"
        }]

        expected_result = [
        {
            "id": "41409891",
            "title": "My life",
            "score": "21",
            "comments": "6",
            "filter": "1"
        }]

        assert FilterListOfDicts.filter_lte_number_words(list_of_dicts,3,"title") == expected_result


    def test_filter_gt_number_words(this):
        """This method tests the static method filter_gt_number_words"""

        list_of_dicts = [
        {
            "id": "41410684",
            "title": "Why You Should Learn Linux (As a Developer)",
            "score": "4",
            "comments": "0",
            "filter": "1"
        },
        {
            "id": "41409891",
            "title": "My life",
            "score": "21",
            "comments": "6",
            "filter": "1"
        },
        {
            "id": "41367658",
            "title": "BaseX – a highly W3C compliant XQuery processor",
            "score": "72",
            "comments": "1",
            "filter": "1"
        }]

        expected_result = [
        {
            "id": "41410684",
            "title": "Why You Should Learn Linux (As a Developer)",
            "score": "4",
            "comments": "0",
            "filter": "1"
        },
        {
            "id": "41367658",
            "title": "BaseX – a highly W3C compliant XQuery processor",
            "score": "72",
            "comments": "1",
            "filter": "1"
        }
        ]

        assert FilterListOfDicts.filter_gt_number_words(list_of_dicts,3,"title") == expected_result



class TestSortListOfDicts():
    """Class to test the static methods of the class SortListOfDicts"""

    def test_sort_list_of_dicts(this):
        """This method tests the sort_list_of_dicts static method """

        list_of_dicts = [
        {
            "id": "41410684",
            "title": "Why You Should Learn Linux (As a Developer)",
            "score": "4",
            "comments": "0",
            "filter": "1"
        },
        {
            "id": "41409891",
            "title": "My fake job in Y2K preparedness",
            "score": "21",
            "comments": "6",
            "filter": "1"
        },
        {
            "id": "41367658",
            "title": "BaseX – a highly W3C compliant XQuery processor",
            "score": "72",
            "comments": "1",
            "filter": "1"
        }]

        expected_result = [
        {
            "id": "41410684",
            "title": "Why You Should Learn Linux (As a Developer)",
            "score": "4",
            "comments": "0",
            "filter": "1"
        },
        {
            "id": "41367658",
            "title": "BaseX – a highly W3C compliant XQuery processor",
            "score": "72",
            "comments": "1",
            "filter": "1"
        },
        {
            "id": "41409891",
            "title": "My fake job in Y2K preparedness",
            "score": "21",
            "comments": "6",
            "filter": "1"
        }]


        assert SortListOfDicts.sort_list_of_dicts(list_of_dicts,"comments",False) == expected_result