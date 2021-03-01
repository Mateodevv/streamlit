import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = requests.get("https://www.f-i.de/Karriere/Offene-Stellen").content
soup = BeautifulSoup(data, features="html.parser")
# DataFrame which will hold all the Data. This is a global variable which will be modified from Methods.
df = pd.DataFrame()



def find_job_offers():
    offers = soup.find("div", {"class": re.compile('content-view-children line count-*')})
    links = []
    job_titles = []
    dates = []

    a = [2, 5, 6]
    for offer in offers.find_all(href=True):
        # Returning found links.
        links.append(offer['href'])
    for offer in offers.find_all("h3"):
        # replacing the html Tags and adding to list. Returns Job Title of the Inquiry
        job_titles.append(str(offer).replace("<h3>", "").replace("</h3>", ""))
    for offer in offers.find_all("div", {"class": "attribute-publish_date"}):
        # removing junk from the string. Return Date in format "month.year". [3:] cuts day off from the date.
        dates.append(
            str(offer).replace('<div class="attribute-publish_date">', "").replace("</div>", "").replace(" ",
                                                                                                         "").replace(
                "\n", "")[3:])

        # Modifies global variable df
        global df
        df = pd.DataFrame(zip(job_titles, dates), columns=["job_title", "date"])

    return links, df
