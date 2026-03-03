# Assignment
This repository has two python programming projects as part of my SEIR course learning.

# Scrap WebPage (project1):
## Description 
This python project takes command line url and downloads the webpage, then parse the html and return the clean title and body text. Adding to that, it returns the set of all the links attached to the web page. 
It uses BeautifulSoup for extracting data efficiently.

## Technologies Used

* Python 3
* requests
* BeautifulSoup (bs4)

## How to Run

1. Install required libraries:
   pip install requests beautifulsoup4

2. Execute the script with a URL:
   python project1.py https://example.com

## Features

* Accepts webpage URL as a command line argument
* Removes script and style elements from the page
* Cleans extra whitespace for readable text output
* Converts relative links into full URLs
* Filters duplicate links automatically

## Learning Outcomes

* Understanding how web scraping works
* Working with HTTP requests in Python
* Parsing and cleaning HTML data
* Using command line inputs in Python programs


* Applying algorithms for efficient comparison of data
