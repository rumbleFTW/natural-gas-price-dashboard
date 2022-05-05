from flask import Flask
import json
import pandas as pd
from requests import request


from scrape import scrape
from predictARIMA import *

scrp = scrape()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return json.dumps({'name': 'rajdeep', 'desc': 'API is working'})


@app.route('/historical/daily', methods=['GET'])
def getDailyData():
    scrp.getDaily()
    dataHist = pd.read_csv('./sih-2022/data/daily.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


@app.route('/historical/weekly', methods=['GET'])
def getWeeklyData():
    scrp.getWeekly()
    dataHist = pd.read_csv('./sih-2022/data/weekly.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


@app.route('/historical/monthly', methods=['GET'])
def getMonthlyData():
    scrp.getMonthly()
    dataHist = pd.read_csv('./sih-2022/data/monthly.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


@app.route('/predict/ARIMA/SS', methods=['GET'])
def predictARIMASS():
    scrp.getDaily()
    p = predictARIMA()
    return json.dumps(p.getSS())


@app.route('/predict/ARIMA/MS/<int:step>', methods=['GET'])
def predictARIMAMS(step):
    scrp.getDaily()
    p = predictARIMA()
    j = {}
    res = p.getMS(steps=step)
    for i, item in enumerate(res):
        j[i] = item
    return json.dumps(j)


app.run()