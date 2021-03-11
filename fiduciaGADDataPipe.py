import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

titles = []
dates = []
texts = []


def get_amount_of_pages():
    data = requests.get("https://fiduciagad-karriereportal.mein-check-in.de/list?").content
    soup = BeautifulSoup(data, features="html.parser")
    pagination_div = soup.find("div", {"class": "pagination-wrapper"})
    links_raw = pagination_div.find_all('a', href=True)
    cleaned_links = []
    # cleaning up the HTML Tags
    for link in links_raw:
        cleaned_links.append(link['href'])

    # getting the Sring containing the last page
    pageination_string = str(cleaned_links[2])
    # finding the int in the string through regex. Since regex converts it to a list containing a string convertion is
    # necessary
    return int(re.findall(r'\d+', pageination_string)[0])


def get_dataframe_from_link(urlcontent):
    tmpsoup = BeautifulSoup(urlcontent, features='html.parser')
    div_root = tmpsoup.find_all("div", {"class": "result"})
    linklist = []

    for div in div_root:
        linklist.append(div.find('a', href=True)['href'])
    for link in linklist:
        title, date = get_information_from_detailed_page(link)
        titles.append(title)
        dates.append(date[0:7])


def get_text_from_link(urlcontent):
    tmpsoup = BeautifulSoup(urlcontent, features='html.parser')
    div_root = tmpsoup.find_all("div", {"class": "result"})
    linklist = []

    for div in div_root:
        linklist.append(div.find('a', href=True)['href'])
    for link in linklist:
        texts.append(get_text_from_detailed_page(link))


def get_information_from_detailed_page(url):
    concated_url = "https://fiduciagad-karriereportal.mein-check-in.de" + url
    detailed_soup = BeautifulSoup(requests.get(concated_url).content, features="html.parser")
    title = detailed_soup.find("h1", {"class": "title"}).text
    date = detailed_soup.find("span", {"itemprop": "datePosted"}).text
    return title, date


def get_text_from_detailed_page(url):
    concated_url = "https://fiduciagad-karriereportal.mein-check-in.de" + url
    text = requests.get(concated_url).text
    return text


def main_wrapper():
    pages = get_amount_of_pages()
    for page in range(pages):
        get_dataframe_from_link(
            requests.get("https://fiduciagad-karriereportal.mein-check-in.de/list?page=" + str(page + 1)).content)
    df = pd.DataFrame(zip(titles, dates), columns=["job_title", "date"])
    return df


def get_text():
    pages = get_amount_of_pages()
    for page in range(pages):
        get_text_from_link(
            requests.get("https://fiduciagad-karriereportal.mein-check-in.de/list?page=" + str(page + 1)).content)
    return texts
