from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True
driver = webdriver.Chrome(options=opt)
query = input('enter query> ').replace(' ', '%20')
driver.get('https:/twitter.com/search?q=' + query + '&f=live')

try:
    # basically get's all the span.text inside the tweet's div. (Autor, body, everything...)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@data-testid="tweet"]')
        )
    )

    tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

    print('Printing the contents of the first 10 tweets.')

    # iterate over the first 10 or less possible tweets.
    for i in range(10):
        try:
            print('TWEET(%i) ==================' % (i + 1))
            spans = tweets[i].find_elements_by_tag_name('span')
            for word in spans:
                print(word.text, end=' ')
            print('============================')
        except IndexError:
            break
finally:
    driver.quit()