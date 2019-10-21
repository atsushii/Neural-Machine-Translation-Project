import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions

main_url = "https://librivox.org/search?primary_key=35&search_category=language&search_page=1&search_form=get_results"

# Firefox headless
options = FirefoxOptions()
options.add_argument('_headless')

# open Firefox
browser = Firefox(options=options)
# open url
browser.get(main_url)

ui = browser.find_element_by_css_selector("body > div > div.browse.browse-title > ul")
