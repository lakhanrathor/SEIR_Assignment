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




# project2: (scraper.py)


## Description

This project is a Python program that compares how simialr two documents are.
It processes the content, generates hashes for words, and applies a similarity hashing technique to create compact representations of documents.
We compare fingerprints for each document to save time complexity and check near duplicate documents

## Technologies Used

* Python 3
* Standard Python libraries
* Hashing and text processing techniques

## How to Run

1. input two urls as command line inputs

2. Run the program:
   python scraper.py

3. The program will output similarity-related results based on the processed documents.

## Features

* Converts text into tokens and frequency counts
* Generates hashes for words
* Uses simhash to create fingerprint of documents

## Learning Outcomes

* Understanding near duplicate documents comparison
* Working with hashing concepts in Python
* Applying algorithms for efficient comparison of data
