#!/usr/bin/env python
import tweepy


class StreamHandler(tweepy.StreamListener):
    def __init__(self, statusListener):
        super(StreamHandler, self).__init__()
        self.statusListener = statusListener

    def on_status(self, status):
        try:
            usr = status.author.screen_name.strip()
            txt = status.text.strip()
            print 'Tweet consists of %s' % str(self.statusListener.classify(txt))
            # print '%s => %s' % (usr, txt)
        except Exception as e:
            print e

    def on_error(self, status_code):
        print 'Oops, an error occurred %s' % status_code
        return True
