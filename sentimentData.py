from multiprocessing.pool import INIT
from string import whitespace
import pandas as pd
import snscrape.modules.twitter as sntwitter
import re
import flair
import progressbar


class sentimentData:
    def cleanText(self, text):
        whitespace = re.compile(r"\s+")
        web_address = re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
        user = re.compile(r"(?i)@[a-z0-9_]+")
        text = whitespace.sub(' ', text)
        text = web_address.sub('', text)
        text = user.sub('', text)
        text = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", text)
        return text
    def __init__(self):
        INIT = 4507
        dataFrame = pd.read_csv('sih-2022/data/daily.csv')
        dataFrame = dataFrame[INIT:]
        sentiment_model = flair.models.TextClassifier.load('en-sentiment')
        MAX_TWEETS = 50
        widgets = ['Loading: ', progressbar.AnimatedMarker()]
        bar = progressbar.ProgressBar(widgets=widgets).start()
        for n in range (1, len(dataFrame['Day'])):
            PREV = str(list(dataFrame.Day)[n-1])[:4]+'-'+str(list(dataFrame.Day)[n-1])[4:6]+'-'+str(list(dataFrame.Day)[n-1])[6:]
            PRES = str(list(dataFrame.Day)[n])[:4]+'-'+str(list(dataFrame.Day)[n])[4:6]+'-'+str(list(dataFrame.Day)[n])[6:]
            QUERY = f"natural gas (natural OR gas OR import OR export OR price) until:{PRES} since:{PREV} -filter:links -filter:replies"
            curr = 0.0
            nums = 0
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(QUERY).get_items()):
                nums += 1
                if i>MAX_TWEETS:
                    break
                sentence = flair.data.Sentence(self.cleanText(tweet.content))
                sentiment_model.predict(sentence)
                try:
                    if(sentence.labels[0].value == 'POSITIVE'):
                        curr += sentence.labels[0].score
                    elif(sentence.labels[0].value == 'NEGATIVE'):
                        curr -= sentence.labels[0].score
                except:
                    pass
            bar.update(n)
            dataFrame.loc[dataFrame.Price == list(dataFrame['Price'])[n], 'Sentiment'] = curr/nums
        dataFrame.to_csv('./data/dailySentiment.csv')

s = sentimentData()