#!/usr/bin/env python

import urllib2


class PriceService(object):
    def getPriceFor(self, stock=None):
        if stock is None:
            return None
        else:
            base_url = """http://download.finance.yahoo.com/d/quotes.csv?"""
            format_url = """&f=nsl1op&e.csv"""
            stock_url = "s=" + str(stock)
            final_url = base_url + stock_url + format_url
            f = urllib2.urlopen(final_url)
            return f.read()

if __name__ == '__main__':
    p = PriceService()
    print p.getPriceFor('GOOG')
    print p.getPriceFor('MSFT')
    print p.getPriceFor('AAPL')
