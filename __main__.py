import requests
from bs4 import BeautifulSoup

URL  = 'https://twitter.com/?lang=en'
PAGE = requests.get(URL)
SOUP = BeautifulSoup(PAGE.content, 'html.parser')

if __name__ == '__main__':
    print(SOUP.prettify())