# ADR: Language to use and possible libraries

## Context and Problem Statement

Which language should I use to create a Web Scrapper, in order to be efficient but also easy to understand and develop in less than 72h?

## Decision Drivers

* Easy code developing
* Efficient code
* Not too many folders and dependencies (frameworks)
* Understandable program
* Not necessary relational data result

## Considered Options

1. Node.js with maybe Axios library
2. Python with BeautifulSoup
3. Python with Selenium

## Decision Outcome

I have decided to apply Python with BeautifulSoup and neglected other languages and frameworks because of the experience I had with some of them, and thinking about the easiest language to develop and understand. Maybe Python it's not the best option in terms of efficiency but it's better with data treatment than JS.
Selenium usually returns some errors and have some problems related to the browser, It could be dealed with a Docker image with Python and Selenium in it, but I should find the right one (or create it myself) and test it before starting developing. Node.js as a framework that it is, it has some dependencies that I would not use and folders.

### Consequences

* Good, because it has been easier to develop and structure the code, and also with data treatment.
* Bad, because there might be a performance penalty in terms of efficiency.


# ADR: Functional programming or object oriented programming

It has been a difficult decision, but using Python, a language that can use both ways of programming in an efficient and organized way, I have decided to use at every module the object oriented programming. However, the utils module could have been done all with functions, without any class but I decided to follow the consistency of the project and create classes but with static methods, as this functions just compute values and do not change the state of the object.


# ADR: Library to use for Python testing

I considered pytest and unittest as the libraries I could use for testing. I decided to use pytest because unittest has more verbose syntax.

