#!/usr/bin/env python
import tweepy
from PriceService import PriceService


class StreamHandler(tweepy.StreamListener):
    def __init__(self, statusListener):
        super(StreamHandler, self).__init__()
        self.statusListener = statusListener
        self.price_service = PriceService()

    def on_status(self, status):
        try:
            usr = status.author.screen_name.strip()
            txt = status.text.strip()
            result_set = self.statusListener.classify(txt)
            print 'Tweet consists of %s' % str(result_set)
            for stock in result_set:
                print self.price_service.getPriceFor(stock)
        except Exception as e:
            print e

    def on_error(self, status_code):
        print 'Oops, an error occurred %s' % status_code
        return True
