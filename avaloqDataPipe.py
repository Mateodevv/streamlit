import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium import webdriver

#  Under construction. PROBLEM: JAVASCRIPT content is not being loaded. This File will may be deleted.


browser = webdriver.Chrome()
browser.get('https://careers.smartrecruiters.com/Avaloq1/')

time.sleep(4)
soup = BeautifulSoup(browser.page_source, features="html.parser")
# DataFrame which will hold all the Data. This is a global variable which will be modified from Methods.
df = pd.DataFrame()


# gets the div containing the single divs holding the country specific listings
def get_root_div():
    div = soup.find("div", {"class": "js-openings-load"})
    offers = div.find_all("a", {"class": "link--block details"})

    for x in offers:
        print(x)
    print(offers.__len__())


get_root_div()
