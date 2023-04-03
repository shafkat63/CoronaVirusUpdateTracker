from flask import Flask, render_template,request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
@app.route('/')

def index():
    url = "https://www.worldometers.info/coronavirus/"
    req = requests.get(url)
# সব এইচটিএমএল ডাটা টেক্সট আকারে সোর্সের মধ্যে সেভ হয়ে আছে।

    bsObj = BeautifulSoup(req.text, 'html.parser')
#বিউটিফুলস্যুপে সোর্সের ডাটা সেভ করে রাখলাম।

    data = bsObj.find_all("div",class_ = "maincounter-number")
    print(data)
    data_for_active=bsObj.find_all("div",class_ ="number-table-main")
    totalCase = data[0].text.strip()
    death = data[1].text.strip()
    recovery = data[2].text.strip()
    activeCase = data_for_active[0].text.strip()
    closedCase = data_for_active[1].text.strip()


    #FOR BD Section
    url2="https://www.worldometers.info/coronavirus/country/bangladesh/"
    req_for_bd = requests.get(url2)
    bsObj_bd = BeautifulSoup(req_for_bd.text, "html.parser")
    data_for_bd=bsObj_bd.find_all("div",class_ ="maincounter-number")
    
    url3="https://virusncov.com/covid-statistics/bangladesh"
    req_for_bd_active=requests.get(url3)
    bsObj_bd_active = BeautifulSoup(req_for_bd_active.text, "html.parser")
    data_for_bdActive=bsObj_bd_active.find_all("div",class_="firt-div")


    bdActive = data_for_bdActive[0].text.strip()
    bdClosed = data_for_bdActive[1].text.strip()

    bdTotalCase = data_for_bd[0].text.strip()
    bdTotalDeath = data_for_bd[1].text.strip()
    bdTotalRecovered = data_for_bd[2].text.strip()


    return render_template('index.html', totalCase = totalCase, death = death, recovery =recovery, activeCase = activeCase,closedCase = closedCase, bdTotalCase = bdTotalCase, bdTotalDeath = bdTotalDeath, bdTotalRecovered = bdTotalRecovered,bdActive = bdActive,bdClosed = bdClosed)


# app.run(host='0.0.0.0', port=6363)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8082)