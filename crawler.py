import time
import bs4
from urllib.request import urlopen
from selenium import webdriver


class Crawler(object):
    def __init__(self, args):
        self.base_url = args.base_url
        self.url = args.url
        self.html = urlopen(args.url)

        self.path = 'D:/gitlab/openreview_crawling/sel_driver/chromedriver.exe'
        self.driver = webdriver.Chrome(self.path)
        self.driver.get(self.url)

    def get_poster(self):
        self.driver.get(self.url)
        poster_button = self.driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[2]/a')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click()", poster_button)
        time.sleep(10)
        poster_list = bs4.BeautifulSoup(self.driver.page_source, "html.parser").select("#accept-poster > ul > li")

        return self.save_data(poster_list)

    def get_spotlights(self):
        self.driver.get(self.url)
        spot_button = self.driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[3]/a')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click()", spot_button)
        time.sleep(5)
        spot_list = bs4.BeautifulSoup(self.driver.page_source, "html.parser").select("#accept-spotlight > ul > li")

        return self.save_data(spot_list)

    def get_talk(self):
        self.driver.get(self.url)
        talk_button = self.driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[4]/a')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click()", talk_button)
        time.sleep(5)
        talk_list = bs4.BeautifulSoup(self.driver.page_source, "html.parser").select("#accept-talk > ul > li")

        return self.save_data(talk_list)

    def save_data(self, paper_list):
        # dict = {'title', 'authors', 'emails', 'abstract', 'keywords', 'tldr',
        #        'github', 'forum_link', 'pdf_link'}

        temp_dict = dict()
        dict_list = []
        email_string = ''

        for paper in range(len(paper_list)):
            temp_dict['title'] = paper_list[paper].find('h4').get_text(strip=True)
            temp_dict['authors'] = paper_list[paper].find('div', {"class": "note-authors"}).get_text(strip=True)

            email_list = paper_list[paper].find_all('a', {"class": "profile-link"})
            for email in range(len(email_list)):
                if email == 0:
                    email_string = email_list[email]['title']
                else:
                    email_string = email_string + ', ' + email_list[email]['title']
            temp_dict['emails'] = email_string

            contents = paper_list[paper].find_all('span', {"class": "note-content-value"})
            contents_title = paper_list[paper].find_all('strong', {"class": "note-content-field"})

            for k in range(len(contents_title)):
                name = contents_title[k].get_text(strip=True)
                temp_dict[name] = contents[k].get_text(strip=True)

            temp_dict['forum_link'] = self.base_url + paper_list[paper].h4.a['href']
            temp_dict['pdf_link'] = self.base_url + paper_list[paper].find('a', {"class": "pdf-link"})['href']

            dict_list.append(temp_dict.copy())

        return dict_list


def crawl_main(args):
    print('In Crawler')
    crawl = Crawler(args)

    print('Start crawling...')
    spotlights = crawl.get_spotlights()
    posters = crawl.get_poster()
    talks = crawl.get_talk()
    print('Finish')

    return posters, spotlights, talks
