import numpy as np
import pandas as pd
from funcs import MSE
import matplotlib.pyplot as plt


class exponentialSmoothing:

    def __init__(self):
        self.alpha = 0

    def SES(self, series, alpha):
        results = np.zeros_like(series)
        results[0] = series[0]
        results[1] = series[0]
        for t in range(2, series.shape[0]):
            results[t] = alpha * series[t-1] + (1 - alpha) * results[t - 1]
        return results

    def fit(self, series):
        errors = {}
        for alpha in np.arange(0.0, 1.0, 0.001):
            errors[MSE(self.SES(series, alpha), series)] = alpha
        self.alpha = errors[min(errors)]
        print("alpha:", self.alpha)

    def predict(self, series):
        alpha = self.alpha
        results = np.zeros_like(series)
        results[0] = series[0]
        results[1] = series[0]
        for t in range(2, series.shape[0]):
            results[t] = alpha * series[t-1] + (1 - alpha) * results[t - 1]
        predicted = self.alpha * series[-1] + (1 - self.alpha) * results[-1]
        return (results, predicted)



class predictSES():
    def get(self):
        data = pd.read_csv('sih-2022/data/daily.csv')
        y = np.array(data.Price)[-500:]
        m = exponentialSmoothing()
        m.fit(np.array(y))
        total, pred = m.predict(np.array(y))
        return pred