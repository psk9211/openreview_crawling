import sys
from urllib.request import urlopen
import configargparse
import datetime
import requests
import bs4


class Crawler(object):
    def __init__(self, args):
        self.url = args.url
        self.html = urlopen(args.url)
        self.timestamp = str(datetime.datetime.now())

    def get_info(self):
        source = self.html.read()
        self.html.close()
        soup = bs4.BeautifulSoup(source, "html5lib")



def crawl_main(args):
    print('crawler')
