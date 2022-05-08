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
	for j in range(0, 21):
		res.append([df.Price[i+j], df.Sentiment[i+j]])
	res.append([0, sen.getSentiment(str(df.Day[i+20]))])
	xRes.append(res)
	tf.convert_to_tensor(xRes)
	print(xRes)
	return model.predict(np.array(xRes))