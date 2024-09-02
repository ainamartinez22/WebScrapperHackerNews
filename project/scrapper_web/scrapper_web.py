import requests
from bs4 import BeautifulSoup
import datetime
import json

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
        Makes a get request to an URL and returns the html parsed by BeautifulSoup. It saves the time of the request.
    load_data_into_file(data:dict,file_path_name:str)
        Loads the data you pass as an argument into a file with the file name and path you enter
    
    """
    def __init__(this,url: str,current_time = None):
        this.url = url
        this.current_time = current_time
    

    def get_request(this):
        """Makes a get request to an URL and returns the html parsed by BeautifulSoup. 
            It saves the time of the request in this.current_time"""

        this.current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page = requests.get(this.url)
        # Parse the HTML content
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup
    
    def load_data_into_file(this,data:dict,file_path_name:str):
        """Load data into a file

        Args:
            data (dict): data to save
            file_path_name (str): file path you want to save the data (it creates the file)
        """
        
        with open(file_path_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

