import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

opts = Options()
opts.headless = True
assert opts.headless
browser = Firefox(options=opts)

browser.get('https://duckduckgo.com')
search = browser.find_element_by_id('search_form_input_homepage')
search.send_keys("testing")
search.submit()

# wait for URL to change with 15 seconds timeout
WebDriverWait(browser, 15).until(EC.url_changes(browser.current_url))
print(browser.current_url)

results = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.ID, "links"))
    )
time.sleep(5)
results = browser.find_elements_by_css_selector('.result.results_links_deep.highlight_d.result--url-above-snippet')
print(results[0].text)


browser.close()
quit()
