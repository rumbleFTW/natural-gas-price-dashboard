import pandas as pd
import snscrape.modules.twitter as sntwitter
import re
import flair
from datetime import datetime, timedelta


class sentimentData:
    def nextDay(self, prevDate):
        prev = prevDate[:4]+'-'+prevDate[4:6]+'-'+prevDate[6:]+' 00:00:00'
        return datetime.fromisoformat(prev)+timedelta(1)

    def cleanText(self, text):
        whitespace = re.compile(r"\s+")
        web_address = re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
        user = re.compile(r"(?i)@[a-z0-9_]+")
        text = whitespace.sub(' ', text)
        text = web_address.sub('', text)
        text = user.sub('', text)
        text = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", text)
        return text

    def getSentiment(self, currDay):
            MAX_TWEETS = 25
            PREV = currDay
            PRES =  self.nextDay(currDay)
            QUERY = f"natural gas (natural OR gas OR import OR export OR price) until:{PRES} since:{PREV} -filter:links -filter:replies"
            sentiment_model = flair.models.TextClassifier.load('en-sentiment')
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
            return curr/nums