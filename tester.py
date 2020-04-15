import sys
import urllib
from urllib.request import urlopen
import configargparse
import datetime, time
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import parse


if __name__ == "__main__":
    url = 'https://openreview.net/group?id=ICLR.cc/2020/Conference'

    path = 'D:/gitlab/openreview_crawling/sel_driver/chromedriver.exe'
    driver = webdriver.Chrome(path)

    # exe script 'body > script:nth-child(15)'
    driver.get(url)

    poster_button = driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[2]/a')
    time.sleep(10)
    driver.execute_script("arguments[0].click()", poster_button)

    poster = bs4.BeautifulSoup(driver.page_source, "html.parser")
    papers = poster.select("#accept-poster > ul > li")
    # "#accept-poster > ul > li:nth-child(1)"
    # print(paper1)
    #
    # paper1_item = paper1[0]
    # details = paper1_item.get_text()
    # detailsSpl = details.split("\n")
    # while "" in detailsSpl:
    #     detailsSpl.remove("")
    #
    # title = detailsSpl[0]
    # print(title)

    print(papers)



"""
# Example ID: Syx4wnEtvH

# XPath
//*[@id="accept-poster"]/ul/li[1]

# Full XPath
/html/body/div[3]/div/div/main/div/div[3]/div/div/div[2]/ul/li[1]
html > body > div[3] > div > div > main > div > div[3] > div > div > div[2] > ul
                                    notes/    tab-content
div.tab-content > div[2] > ul > li[1]


# Paper ID selector
#accept-poster > ul > li:nth-child(1) 

# Paper Title
#accept-poster > ul > li:nth-child(1) > h4 > a:nth-child(1)

# PDF URL
#accept-poster > ul > li:nth-child(1) > h4 > a.pdf-link

# Author
#accept-poster > ul > li:nth-child(1) > div.note-authors

# TL;DR
#Syx4wnEtvH-details-832 > div > ul > li:nth-child(1) > span

# Abstract
#Syx4wnEtvH-details-832 > div > ul > li:nth-child(2) > span

# Keyword
#Syx4wnEtvH-details-832 > div > ul > li:nth-child(3) > span

# Code (if available)
#Syx4wnEtvH-details-832 > div > ul > li:nth-child(4) > span > a




"""