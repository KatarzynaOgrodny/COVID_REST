import requests
import bs4
import tkinter as tk


def get_html_data(url):
    data = requests.get(url)
    return data


def get_text_gp():
    url = "https://governanceportal-dev.roche.com/SiteRequest#!/request/collection/add/archiving"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", {"class": "ctcontainer"}).find_all("div", attrs={"class": "ttcol text"})
    all_data = " "
    for block in info_div:
        text = block.find("p").get_text()
        all_data = (all_data + text + " "+ "\n")
    print(all_data)
    return (all_data)


get_text_gp()