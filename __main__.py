import requests
from bs4 import BeautifulSoup

URL  = 'https://twitter.com/?lang=en'
PAGE = requests.get(URL)

if __name__ == '__main__':
    print(PAGE.content)