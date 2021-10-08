from flask import Flask, jsonify, request, Response
import requests

from bs4 import BeautifulSoup

app = Flask(__name__)

def get_html_data(url):
    data = requests.get(url)
    return data
@app.route("/countries/", methods=["GET"])
def get_all_countries():
    lnkList = []

    url = "https://www.worldometers.info/coronavirus/#countries"
    html_all_country_data = get_html_data(url)
    bs = BeautifulSoup(html_all_country_data.text, 'html.parser')
    find_all_a = bs.find_all("a", {"class":"mt_a"})
    for tag in find_all_a:
        country = tag.get_text()
        #country_list = country_list.lower()
        lnkList.append(country)
    final_list = sorted(list(set(lnkList)))
    jsonified_list = jsonify(final_list)
    return jsonified_list


if __name__ == "__main__":
    app.run()



