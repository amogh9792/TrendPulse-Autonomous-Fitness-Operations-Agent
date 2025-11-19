import pandas as pd
from pytrends.request import TrendReq
import snscrape.modules.twitter as sntwitter
import datetime

def get_google_trends(keywords, timeframe="now 7-d", geo="IN"):
    pytrends = TrendReq()
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
    data = pytrends.interest_over_time()
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])
    return data

def scrape_twitter_trends(hashtag, max_tweets=100):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"{hashtag} lang:en").get_items()):
        if i >= max_tweets:
            break
        tweets.append({'date': tweet.date, 'content': tweet.content})
    return pd.DataFrame(tweets)

if __name__ == "__main__":
    # Example usage
    google_data = get_google_trends(['resistance band', 'kettlebell'])
    print(google_data.tail())

    twitter_data = scrape_twitter_trends('#fitness', 50)
    print(twitter_data.head())
