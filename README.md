# WebScrapperHackerNews

This project is a Web Scrapper developed using Python and the library BeaufitulSoup4.
It is focus on scrapping the web Hacker News and filtering and sorting the news returned by the web page. Eventually, it creates a JSON file with the results, filtered and sorted.

The Architectural Decision Record or Decision Log, can be find in the ADR.md file.


## Requirements

As a requirement needed for running the code and install the dependencies, the following versions of Python and pip are required:
```
Python 3.10.3
pip 22.0.4 
```


Once Python and pip are installed, the following command should be run for obtaining the needed environment:
```
pip install -r requirements.txt
```


## How to run

In order to run this project, you have to execute:

```
python main.py
```

Being at the root folder of the project (at the same level as main.py).


## How to test

In order to execute testing with py-test, you should execute on the command line:
```
python -m pytest tests/XXXX.py 
```
where XXXX is the file you want to execute it's tests and you have to be located on the project folder (top level of WebScrapperPython).
