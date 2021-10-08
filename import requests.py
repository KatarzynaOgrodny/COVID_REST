import  requests
from  bs4 import BeautifulSoup
def findinfo(cname):
    totalresult = []
    country = cname
    url = "https://www.worldometers.info/coronavirus/country/{countryname}/".format(countryname = country)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find_all('div',class_="maincounter-number")
        for i in result:
            totalresult.append(i.find("span").text)
    else:
        totalresult.append("No Result")
    return totalresult