import urllib.request
import urllib.error
from sys import argv

from bs4 import BeautifulSoup

def process_article_url(articlestring):
    #Titlize string
    articlestring = articlestring.title()
    #replace spaces with underscores articlestring = articlestring.replace(" ", "_")
    
    article_url = "http://starwars.wikia.com/wiki/" + articlestring
    return article_url

def get_article(article_url):
    try:
        sock = urllib.request.urlopen(article_url)
    except urllib.error.HTTPError:
        print("Oops! This is not an article")
        return get_article(process_article_string(input("Article Name: ")))
    htmlsource = sock.read()
    sock.close()
    soup = BeautifulSoup(htmlsource)
    return soup

def display_article(soup):
    p = soup.find_all("p") 
    for i in p:
        if i.b != None:
            summary = i
    return summary.get_text().encode("UTF-8")

if (__name__ == "__main__"):
    if (len(argv) == 1):
        inputarticle = input("Article Name: ")
    else:
        inputarticle = argv[1]

    url = process_article_url(inputarticle)
    article = get_article(url)
    print(display_article(article))
