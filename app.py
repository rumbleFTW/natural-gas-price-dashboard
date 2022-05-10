from flask import Flask, request
from flask_cors import CORS
import tensorflow as tf
import json
import pandas as pd

from funcs import sMAPE
from scrape import scrape
from predictARIMA import *
from predictSES import *
from predictNN import *

scrp = scrape()
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def main():
    scrp.getDaily()
    scrp.getWeekly()
    scrp.getMonthly()
    dfDaily = pd.read_csv('./sih-2022/data/daily.csv')
    dfSen = pd.read_csv('./sih-2022/data/dailySentiment.csv')
    dfSen = dfSen.loc[:, ~dfSen.columns.str.contains('^Unnamed')]
    if list(dfDaily.Day)[-1] != list(dfSen.Day)[-1]:
        day = list(dfDaily.Day)[-1]
        prevDay = list(dfDaily.Day)[-1]
        price = list(dfDaily.Price)[-1]
        s = sentimentData()
        sen = s.getSentiment(str(prevDay))
        dfSen = dfSen.append([{'Day':day, 'Price': price, 'Sentiment': sen}], ignore_index=True)
        dfSen.to_csv('./sih-2022/data/dailySentiment.csv')
        return json.dumps({'SiH-2022': 'Natural-Gas Price Prediction', 'Message': 'Updated all values'})
    return json.dumps({'SiH-2022': 'Natural-Gas Price Prediction', 'Message': 'All data up-to-date'})


@app.route('/historical/daily', methods=['GET'])
def getDailyData():
    dataHist = pd.read_csv('./sih-2022/data/daily.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


@app.route('/historical/weekly', methods=['GET'])
def getWeeklyData():
    dataHist = pd.read_csv('./sih-2022/data/weekly.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


@app.route('/historical/monthly', methods=['GET'])
def getMonthlyData():
    dataHist = pd.read_csv('./sih-2022/data/monthly.csv')
    hist = {}
    for i in range(len(dataHist)):
        hist[int(dataHist['Day'][i])] = dataHist['Price'][i]
    return json.dumps(hist)


@app.route('/predict/ARIMA/SS', methods=['GET'])
def predictARIMASS():
    p = predictARIMA()
    return json.dumps(p.getSS())


@app.route('/predict/ARIMA/MS', methods=['GET'])
def predictARIMAMS():
    step = int(request.args.get('steps'))
    p = predictARIMA()
    j = {}
    res = p.getMS(steps=step)
    for i, item in enumerate(res):
        j[i] = item
    return json.dumps(j)


@app.route('/predict/SES/SS', methods=['GET'])
def predictSESSS():
    p = predictSES()
    return json.dumps(p.get())


@app.route('/predict/CNN/SS', methods=['GET'])
def predictCNNSS():
    CNNModel = tf.keras.models.load_model('sih-2022\models\singleStepDailyCNN.h5', custom_objects={'smape': sMAPE})
    p = predictNN(CNNModel)
    return json.dumps(p)


@app.route('/predict/CNN/MS', methods=['GET'])
def predictCNNMS():
    CNNModel = tf.keras.models.load_model('sih-2022\models\multiStepDailyCNN.h5', custom_objects={'smape': sMAPE})
    p = predictNNMS(CNNModel)
    j = {}
    for i, item in enumerate(p):
        j[i] = float(item)
    return json.dumps(j)


@app.route('/predict/LSTM/SS', methods=['GET'])
def predictLSTMSS():
    LSTMModel = tf.keras.models.load_model('sih-2022\models\singleStepDailyLSTM.h5', custom_objects={'smape': sMAPE})
    p = predictNN(LSTMModel)
    return json.dumps(p)


@app.route('/predict/LSTM/MS', methods=['GET'])
def predictLSTMMS():
    LSTMModel = tf.keras.models.load_model('sih-2022\models\multiStepDailyLSTM.h5', custom_objects={'smape': sMAPE})
    p = predictNNMS(LSTMModel)
    j = {}
    for i, item in enumerate(p):
        j[i] = float(item)
    return json.dumps(j)


@app.route('/predict/CNN-LSTM/SS', methods=['GET'])
def predictHybridSS():
    hybridModel = tf.keras.models.load_model('sih-2022\models\singleStepDailyHybrid.h5', custom_objects={'smape': sMAPE})
    p = predictNN(hybridModel)
    return json.dumps(p)


@app.route('/predict/CNN-LSTM/MS', methods=['GET'])
def predictHybridMS():
    hybridModel = tf.keras.models.load_model('sih-2022\models\multiStepDailyHybrid.h5', custom_objects={'smape': sMAPE})
    p = predictNNMS(hybridModel)
    j = {}
    for i, item in enumerate(p):
        j[i] = float(item)
    return json.dumps(j)


app.run(host="localhost", port=5000, debug=True)
