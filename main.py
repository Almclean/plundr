#!/usr/bin/env python

import tweepy
import ConfigParser
from StockClassifier import StockClassifier
from PriceService import PriceService
from StreamWatchHandler import StreamHandler

stocks = ['AAPL', 'GOOG', 'MSFT']


def main():
    # Load in the twitter connection properties
    config = ConfigParser.RawConfigParser()
    config.read('twitterLogin.ini')
    classifier = StockClassifier(stocks)
    price_service = PriceService()
    authentication = establish_stream(config)

    print "Establishing stream...",
    stream = tweepy.Stream(authentication, StreamHandler(classifier, price_service), timeout=None)
    print "Done"
    stream.filter(track=stocks)


def establish_stream(config):
    consumer_key = config.get('twitter_config', 'oauth.consumerKey')
    consumer_secret = config.get('twitter_config', 'oauth.consumerSecret')
    auth1 = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)

    access_token = config.get('twitter_config', 'oauth.accessToken')
    access_token_secret = config.get('twitter_config', 'oauth.accessTokenSecret')
    auth1.set_access_token(access_token, access_token_secret)
    return auth1

if __name__ == '__main__':
    main()
