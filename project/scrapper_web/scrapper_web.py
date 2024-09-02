import requests
from bs4 import BeautifulSoup
import datetime

class ScrapperWeb():
    """A class used to represent a general Web Scrapper
    ...

    Attributes
    ----------
    current_time : str
        a timestamp formatted the way you want as a string to save the time in which you get the request
    url : str
        the url of the web you want to create the scrapper

    Methods
    -------
    get_request(this)
        Makes a get request to an URL and returns de html parsed by BeautifulSoup. It saves the time of the request.

    """
    def __init__(this,url: str,current_time = None):
        this.url = url
        this.current_time = current_time
    

    def get_request(this):
        this.current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page = requests.get(this.url)
        # Parse the HTML content
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup
    
