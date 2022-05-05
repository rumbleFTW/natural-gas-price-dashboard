import tensorflow as tf
import pandas as pd

from scrape import scrape

class singleStepSentimentNN:
    sc = scrape()
    sc.getDaily()
    data = pd.read_csv('../data/dailySentiment.csv')
    model = tf.keras.models.tf.keras.models.load_model('../models/singleStepSentimentHybrid.h5')