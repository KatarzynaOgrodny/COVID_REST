from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def getCountryInfo(cname):
    totalresult = []
    country = cname
    url = "https://www.worldometers.info/coronavirus/country/{countryname}/".format(countryname=country)
    response = requests.get(url)
    print("response: " + str(response.text))
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find_all("div", attrs={"class": "maincounter-number"})
        print(result)
        for i in result:
            totalresult.append(i.find("span").text)
    else:
        totalresult.append("No Result")
    return totalresult


@app.route("/info/", methods=["GET"])
def find_info():
    country = request.args.get("country")
    try:
        country_response = getCountryInfo(country)
        response_object = {
            "Total Cases": country_response[0],
            "Total Deaths": country_response[1],
            "Total Recovered": country_response[2],
        }
        jsonified_object = jsonify(response_object)
        return jsonified_object
    except Exception as err:
        print("Exception occurred: " + str(err))
        return {"No country found": country}


if __name__ == "__main__":
    app.run()


#//zwracanie listy wszystkich krajow
