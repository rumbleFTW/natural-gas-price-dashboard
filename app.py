from flask import Flask
import json
import pandas as pd


from scrape import scrape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return json.dumps({'name': 'rajdeep', 'desc': 'API is working'})

@app.route('/historical/daily', methods=['GET'])
def getDailyData():
    scr = scrape()
    scr.getDaily()
    dataHist = pd.read_csv('./sih-2022/data/daily.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)

@app.route('/historical/weekly', methods=['GET'])
def getWeeklyData():
    scr = scrape()
    scr.getWeekly()
    dataHist = pd.read_csv('./sih-2022/data/weekly.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)

@app.route('/historical/monthly', methods=['GET'])
def getMonthlyData():
    scr = scrape()
    scr.getMonthly()
    dataHist = pd.read_csv('./sih-2022/data/monthly.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


app.run()