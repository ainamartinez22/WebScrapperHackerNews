from project.scrapper_web.scrapper_web import ScrapperWeb
import project.hacker_news_scrapper.params as params
from project.utils.sentence_metrics import SentenceMetrics
from project.utils.transform_list_of_dicts import FilterListOfDicts,SortListOfDicts
import unicodedata

class HackerNewsScrapper(ScrapperWeb):
    """A class used to represent the HackerNewsScrapper that inherits from ScrapperWeb
    ...

    Attributes
    ----------
    Inherit from ScrapperWeb

    Methods
    -------
    run_scrapper(this)
        Function to run the Hackers News Web Scrapper.
    get_clean_data(page_info: str)
        Returns an list of dicts (custom) from the information of page_info, that it's the html parsed from the web.
    get_clean_filter_sort_data(info:list)
        Returns an array of dicts filtering and sorting the original info (a list of dicts passed by argument) with custom criteria
    
     
    """

    def __init__(this, URL = params.URL, current_time = None):

        ScrapperWeb.__init__(this, URL, current_time)

    def run_scrapper(this):
        """Function to execute the scrapper and get the information we need, saving it into a file at results folder

        Args:
            url (str): url of the web we want to create the scrapper
        """

        page_info = this.get_request()
        clean_list = this.get_clean_data(page_info) 
        filter_info = this.get_clean_filter_sort_data(clean_list)

        return filter_info

    def get_clean_data(this, page_info: str):

        elements = page_info.select('tr.athing')

        info = []

        for item in elements:
            id = item.get('id')
            title = item.select_one('span.titleline > a').text
            score_element = page_info.select_one('.subline > #score_'+str(item.get('id')))
            comments_element = page_info.select_one('span.subline > a[href="item?id='+str(item.get('id'))+'"]:last-child')

            info.append({
                "id": id,
                "title": title,
                "score":'0' if score_element is None else SentenceMetrics.get_number_from_sentence(unicodedata.normalize('NFKC',score_element.text)),
                "comments": '0' if comments_element  is None else SentenceMetrics.get_number_from_sentence(unicodedata.normalize('NFKC',comments_element.text))
            })

        return info
    

    def get_clean_filter_sort_data(this,info:list):

        filter_info1 = FilterListOfDicts.filter_gt_number_words(info,5,"title")
        result1 = SortListOfDicts.sort_list_of_dicts(filter_info1,"comments")

        filter_info2 = FilterListOfDicts.filter_lte_number_words(info,5,"title")
        result2 = SortListOfDicts.sort_list_of_dicts(filter_info2,"score")

        join_result = [dict(item, filter='1') for item in result1]+[dict(item, filter='2') for item in result2]

        return join_result
        