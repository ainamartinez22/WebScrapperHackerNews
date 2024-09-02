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
where XXXX is the file you want to execute it's tests and you have to be located on the project folder (top level of WebScrapperHackerNews).



## Folder structure

The project structure is this one:

```
└── 📁WebScrapperHackerNews
    └── 📁.github
        └── 📁workflows
            └── pipeline_tests.yml
    └── 📁project
        └── 📁hacker_news_scrapper
            └── __init__.py
            └── hacker_news_scrapper.py
        └── 📁results
            └── final_result_20240901_130432.json
        └── 📁scrapper_web
            └── __init__.py
            └── scrapper_web.py
        └── 📁tests
            └── test_sentence_metrics.py
            └── test_transform_list_of_dicts.py
            └── test_word_metrics.py
        └── 📁utils
            └── __init__.py
            └── sentence_metrics.py
            └── transform_list_of_dicts.py
            └── word_metrics.py
    └── .gitignore
    └── ADR.md
    └── main.py
    └── params.py
    └── README.md
    └── requirements.txt
```

The functionality of every folder and file from the nearest root level is:

* .github: this folder contains the workflows to execute actions in Github. Particularly, it has a pipeline_tests.yml file, where there are the commands to execute the pipeline when the code is pushed or you do a pull_request at Github.

* project: this is the folder in which there is all the program that scraps the web and returns a file with clean data extracted. It can be called from the outside, calling the run_scrapper function.

* hacker_news_scrapper: this is a module in which there is a class of the custom web scrapper that returns data from the Hacker News URL. This is a custom module because the data we are obtaining depends totally on this URL. It inherits the structure of the class from the scrapper_web module class, the generalized scrapper.

* results: a folder to save the result files.

* scrapper_web: a module with a ScrapperWeb class, that is generalized for every existing web. It just have the general methods that are related to obtaning raw data from the page (call the get request) and saving it into a result file.

* tests: folder in which there are the pytest files.

* utils: module in which there are some helpful classes with static methods so as to compute certain values from sentences, words and lists of dicts.

* ADR.md: Architectural Decision Record or Decision Log from this project.

* .gitignore: file to tell git which files and folders are unnecessary to be tracked and pushed to Github.

* main.py: example file in which you can see how it would be called and runned the web scrapper from the Hacker News web.

* params.py: file with HackerNewsScrapper params

* requirements.txt: file with the python environment requirements. It contains the python libraries necessaries to run this project in your computer.



## Next steps

In order to improve the project, these would be the points to implement:

* Dockerize the project so as to make sure that everybody can execute it without any problem (with the same requirements instaled for anyone)

* Create a decorator to try/catch exceptions and return more information about which exact function returns an exception

* Create a log decorator (save it in a file of logs)

* Change example-based testing for properties-based testing with hypothesis and givens

* Create a pipeline for the coverage of tests

* Create an end to end testing, maybe with an html of the web saved (as a fake request of the website)

