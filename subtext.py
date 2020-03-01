from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import string
analyzer = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    print(text)
    print(score)
