import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = requests.get("https://www.f-i.de/Karriere/Offene-Stellen").content
soup = BeautifulSoup(data, features="html.parser")
# DataFrame which will hold all the Data. This is a global variable which will be modified from Methods.
df = pd.DataFrame()


def find_job_offers():
    # Gives the div holind all job listings.
    offers = soup.find("div", {"class": re.compile('content-view-children line count-*')})
    # Will be used for further Data Mining.
    links = []
    job_titles = []
    dates = []

    for offer in offers.find_all(href=True):
        # Returning found links.
        links.append(offer['href'])
    for offer in offers.find_all("h3"):
        # Replacing the html Tags and adding to list. Returns Job Title of the Inquiry
        job_titles.append(str(offer).replace("<h3>", "").replace("</h3>", ""))
    for offer in offers.find_all("div", {"class": "attribute-publish_date"}):
        # Removing junk from the string. Return Date in format "month.year".
        fulldate = str(offer).replace('<div class="attribute-publish_date">', "").replace("</div>", "").replace(" ",
                                                                                                                "").replace(
            "\n", "")

        # Slicing of the day, reversing and concetanating the string so it fits better for plotting.
        month = fulldate[3:5]
        year = fulldate[6:10]
        dates.append(year + "-" + month)

        # Modifies global variable df
        global df
        df = pd.DataFrame(zip(job_titles, dates), columns=["job_title", "date"])

    return df
