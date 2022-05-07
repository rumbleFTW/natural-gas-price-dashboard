import numpy as np


def MAE(series1, series2):
    absError = 0
    for n in range(len(series1)):
        absError += abs(series1[n]-series2[n])
    return absError/len(series1)


def RMSE(series1, series2):
    return np.sqrt(((series1 - series2) ** 2).mean())


def MSE(series1, series2):
    return ((series1 - series2) ** 2).mean()


def sMAPE(series1, series2):
    return 100/len(series1) * np.sum(2 * np.abs(series2 - series1) / (np.abs(series1) + np.abs(series2)))
