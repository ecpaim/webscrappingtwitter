import requests
from bs4 import BeautifulSoup

MAX = 10
URL = 'https://twitter.com/search'

if __name__ == '__main__':
    query = input('> ').replace(' ', '%20')
    URL = URL + '?q=' + query

    print('going to: %s' % URL)

    PAGE = requests.get(URL)
    SOUP = BeautifulSoup(PAGE.content, 'html.parser')

    print(SOUP.prettify())