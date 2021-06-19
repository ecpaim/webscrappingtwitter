import requests
from bs4 import BeautifulSoup

MAX = 10
URL = 'https://twitter.com/search'

if __name__ == '__main__':
    # only works with simple words like 'Banana' or 
    # 'hot dogs'.
    query = input('> ').replace(' ', '%20')
    URL = URL + '?q=' + query

    print('going to: %s' % URL)

    PAGE = requests.get(URL)
    SOUP = BeautifulSoup(PAGE.content, 'html.parser')

    i = 0
    for d in SOUP.find_all('div'):
        if d.get('data-testid') == 'tweet':
            print('TWEET #%s ================' % i)
            print(d.prettify())
            print('==========================')
            i += 1

            if d == MAX:
                exit(0)
    else:
        print('nothing')