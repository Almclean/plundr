#!/usr/bin/env python
import re


class StockClassifier(object):
    def __init__(self, stocks):
        self.stocks = stocks
        pattern_string = '|'.join(map(str, self.stocks))
        self.pattern = re.compile(pattern_string, re.I)

    def classify(self, tweet=None):
        if tweet is None:
            return set()
        else:
            return set(re.findall(self.pattern, tweet))
