import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url_list = []
n = 1

# Firefox headless
options = FirefoxOptions()
# options.add_argument('--headless')

# open Firefox
browser = Firefox(options=options)
while True:
    main_url = ("https://librivox.org/search?primary_key=35&search_category=language&search_page=%d&search_form=get_results" % n)

    # open url
    browser.get(main_url)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "book-author")))
    # get li tag
    li = browser.find_elements_by_css_selector("body > div > div.browse.browse-title > ul > li")

    # add each url to list
    for i in li:
        url = i.find_elements_by_css_selector("h3 > a")[0].get_attribute("href")
        # check duplicate
        if url not in url_list:
            url_list.append(url)


    n += 1
    if n == 6:
        break

print(len(url_list))