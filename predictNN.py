import tensorflow as tf
import pandas as pd
from sentimentData import sentimentData
import numpy as np

def predictNN(model):
	sen = sentimentData()
	df = pd.read_csv('sih-2022\data\dailySentiment.csv')
	i = len(df)-20-1
	xRes = []
	res = []
	for j in range(1, 21):
		res.append([df.Price[i+j], df.Sentiment[i+j]])
	res.append([0, sen.getSentiment(str(df.Day[i+20]))])
	nextDay = sen.nextDay(str(df.Day[i+20]))
	xRes.append(res)
	tf.convert_to_tensor(xRes)
	return {str(nextDay): float(model.predict(np.array(xRes))[0][0])}

def predictNNMS(model):
	df = pd.read_csv('sih-2022\data\daily.csv')
	xRes = [[item] for item in df.Price[-60:]]
	res = list(model.predict(np.array([xRes])))
	print(res[0])
	return res[0]

if __name__ == '__main__':
	from funcs import sMAPE
	model = tf.keras.models.load_model('sih-2022\models\singleStepDailyHybrid.h5', custom_objects={'smape': sMAPE})