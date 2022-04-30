import requests
import pandas as pd

key = "LLlFxfWWzAsqU8YRvLvoKQoGwqWOUAfmrITv8TFE"
class scrape:

    def getMonthly(self):
        dataMonthly = requests.get(f"https://api.eia.gov/series/?series_id=NG.RNGWHHD.M&api_key={key}")
        rawResponseMonthly = dataMonthly.json()['series']
        rawDataMonthly = rawResponseMonthly[0]['data'][::-1]

        dataframeMonthly = pd.DataFrame(rawDataMonthly, columns = ['Day', 'Price'])
        nan_value = float("NaN")
        dataframeMonthly.replace("", nan_value, inplace=True)
        dataframeMonthly.dropna(subset = ["Price"], inplace=True)
        dataframeMonthly.to_csv('./sih-2022/data/monthly.csv', index = False)
        print('Monthly Data saved!')

    def getWeekly(self):
        dataWeekly = requests.get(f"https://api.eia.gov/series/?series_id=NG.RNGWHHD.W&api_key={key}")
        rawResponseWeekly = dataWeekly.json()['series']
        rawDataWeekly = rawResponseWeekly[0]['data'][::-1]

        dataframeWeekly = pd.DataFrame(rawDataWeekly, columns = ['Day', 'Price'])
        nan_value = float("NaN")
        dataframeWeekly.replace("", nan_value, inplace=True)
        dataframeWeekly.dropna(subset = ["Price"], inplace=True)
        dataframeWeekly.to_csv('./sih-2022/data/weekly.csv', index = False)
        print('Weekly Data saved!')
    
    def getDaily(self):
        dataDaily = requests.get(f"https://api.eia.gov/series/?series_id=NG.RNGWHHD.D&api_key={key}")
        rawResponseDaily = dataDaily.json()['series']
        rawDataDaily = rawResponseDaily[0]['data'][::-1]

        dataframeDaily = pd.DataFrame(rawDataDaily, columns = ['Day', 'Price'])
        nan_value = float("NaN")
        dataframeDaily.replace("", nan_value, inplace=True)
        dataframeDaily.dropna(subset = ["Price"], inplace=True)
        dataframeDaily.to_csv('./sih-2022/data/daily.csv', index = False)
        print('Daily Data saved!')
