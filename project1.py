# project to scrape a webpage using command line url: 
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def input_url():
    if len(sys.argv) < 2:
        print("Error: Enter URL")
        sys.exit()
    return sys.argv[1]


def get_page(url):
    data = requests.get(url)
    return data.text

def make_soup(html):
    return BeautifulSoup(html, "html.parser")

def print_title(soup):   
    if soup.title !=None:
        print(soup.title.text.strip())
    else:
        print("This page does not have title.")

def print_body(soup):
# remove script and style tags

    for tag in soup(["script", "style"]):
        tag.extract()

    body_text = " ".join(soup.get_text().split())
    print(body_text)

def print_links(soup, url):
    anchor_tags = soup.find_all("a", href=True)
    link_set= set()
    for tag in anchor_tags:
        link = tag.get("href").strip()
        if link.lower().startswith("javascript"):
            continue

        full_link = urljoin(url, link)
        if full_link not in link_set:
            link_set.add(full_link)
            print(full_link)

def main():
    url = input_url()
    html = get_page(url)
    soup = make_soup(html)

    print_title(soup)
    print_body(soup)
    print_links(soup, url)


main()