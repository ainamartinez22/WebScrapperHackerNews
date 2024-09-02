from project.scrapper_web.scrapper_web import ScrapperWeb
import project.hacker_news_scrapper.params as params

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
     
    """

    def __init__(this, URL = params.URL, current_time = None):

        ScrapperWeb.__init__(this, URL, current_time)

    def run_scrapper(this):
        """Function to execute the scrapper and get the information we need, saving it into a file at results folder

        Args:
            url (str): url of the web we want to create the scrapper
        """

        page_info = this.get_request()

        return page_info
