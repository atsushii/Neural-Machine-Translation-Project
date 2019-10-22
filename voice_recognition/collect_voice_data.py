from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import os
import time

url_list = []
n = 1

# Firefox headless
options = FirefoxOptions()
options.add_argument('--headless')

# open Firefox
browser = Firefox(options=options)
while True:
    main_url = ("https://librivox.org/search?primary_key=35&search_category=language&search_page=%d&search_form=get_results" % n)

    # open url
    browser.get(main_url)
    # sleep time until show book detail
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
    if n == 4:
        break

text_url_list = []
download_url_list = []

for url in url_list:
    # access book detail page
    browser.get("https://librivox.org/%s/" % url)
    # sleep time until show dl button
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "play-btn")))

    # check Etext button
    etext_check = browser.find_elements_by_css_selector("body > div > div.page.book-page > table > tbody > tr > td:nth-child(4)")
    # check japanese lang
    lang_check = browser.find_elements_by_css_selector("body > div > div.page.book-page > table > tbody > tr > td:nth-child(7)")
    # check download button
    download_tags = browser.find_elements_by_css_selector("body > div > div.page.book-page > table > tbody > tr > td:nth-child(1)")

    for etext, lang, download_tag in zip(etext_check, lang_check, download_tags):
        # get only japanese lang and available text info
        if etext.text == "Etext" and lang.text == "jp":
            # text data url
            text_url = etext.find_element_by_css_selector("a").get_attribute("href")
            # audio data url
            download_url = download_tag.find_element_by_css_selector("a").get_attribute("href")
            # check duplicate data
            if text_url in text_url_list or download_url in download_url_list:
                continue
            text_url_list.append(text_url)
            download_url_list.append(download_url)

# define dir for save
audio_save_dir = "dataset/audio_dataset"
text_save_dir = "dataset/text_data"
for download_url, text_url in zip(download_url_list, text_url_list):
    try:
        print(download_url, text_url)
        # create file name
        audio_file_name = download_url.split("/")[-1]
        # save audio data
        urllib.request.urlretrieve(download_url, os.path.join(audio_save_dir, audio_file_name))
        time.sleep(1)
        # check file extension
        if not text_url.split(".")[-1] == "html":
            text_url = text_url.replace(text_url.split(".")[-1], "html")
        text_file_name = text_url.split("/")[-1]
        # save text data as html
        urllib.request.urlretrieve(text_url, os.path.join(text_save_dir, text_file_name))
        time.sleep(1)
    except Exception as e:
        print(e, "can't load: %s" % audio_file_name, text_file_name)
        os.remove(audio_save_dir + "/" + audio_file_name)
        continue

browser.close()