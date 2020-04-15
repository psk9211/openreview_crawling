from urllib.request import urlopen
import datetime
import time
import bs4
from selenium import webdriver


class Crawler(object):
    def __init__(self, args):
        self.base_url = args.base_url
        self.url = args.url
        self.html = urlopen(args.url)
        self.timestamp = str(datetime.datetime.now())

        self.path = 'D:/gitlab/openreview_crawling/sel_driver/chromedriver.exe'
        self.driver = webdriver.Chrome(self.path)
        self.driver.get(self.url)

    def get_poster(self):
        poster_button = self.driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[2]/a')
        time.sleep(10)
        self.driver.execute_script("arguments[0].click()", poster_button)
        poster_list = bs4.BeautifulSoup(self.driver.page_source, "html.parser").select("#accept-poster > ul > li")

        return poster_list

    def get_spotlights(self):
        spot_button = self.driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[3]/a')
        time.sleep(10)
        self.driver.execute_script("arguments[0].click()", spot_button)
        spot_list = bs4.BeautifulSoup(self.driver.page_source, "html.parser")

    def get_talk(self):
        talk_button = self.driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[4]/a')
        time.sleep(10)
        self.driver.execute_script("arguments[0].click()", talk_button)
        talk_list = bs4.BeautifulSoup(self.driver.page_source, "html.parser").select("#accept-talk > ul > li")

    def save_data(self, paper_list):
        title = []
        authors = []
        emails = []
        abstract = []
        keywords = []
        tldr = []
        github = []
        forum_link = []
        pdf_link = []

        for paper in range(len(paper_list)):
            title.append(paper_list[paper].find('h4').get_text())
            authors.append(paper_list[paper].find('div', {"class": "note-authors"}).get_text())
            emails.append(paper_list[paper].find_all('a', {"class": "profile-link"}).get_text())

            contents = paper_list[paper].find_all('span', {"class": "note-content-value"})
            abstract.append(contents[0].get_text())
            keywords.append(contents[1].get_text())
            tldr.append(contents[2].get_text())
            if len(contents) == 5:
                github.append(contents[3].a['href'])
            else:
                github.append('None')

            forum_link.append(self.base_url + paper_list[paper].h4.a['href'])
            pdf_link.append(self.base_url + paper_list[paper].find('a', {"class": "pdf-link"})['href'])




def crawl_main(args):
    print('crawler')
    crawl = Crawler()
    crawl.get_poster()


"""
<li class="note" data-id="rkgpv2VFvr" data-number="22">
<h4>
    <a href="/forum?id=rkgpv2VFvr">
        Sharing Knowledge in Multi-Task Deep Reinforcement Learning
    </a>
    <a class="pdf-link" href="/pdf?id=rkgpv2VFvr" target="_blank" title="Download PDF"><img src="/static/images/pdf_icon_blue.svg"/></a>
</h4>

<div class="note-authors">
    <a class="profile-link" data-placement="top" data-toggle="tooltip" href="/profile?email=carlo%40robot-learning.de" title="carlo@robot-learning.de">Carlo D'Eramo</a>, <a class="profile-link" data-placement="top" data-toggle="tooltip" href="/profile?email=davide%40robot-learning.de" title="davide@robot-learning.de">Davide Tateo</a>, <a class="profile-link" data-placement="top" data-toggle="tooltip" href="/profile?email=andrea.bonarini%40polimi.it" title="andrea.bonarini@polimi.it">Andrea Bonarini</a>, <a class="profile-link" data-placement="top" data-toggle="tooltip" href="/profile?email=marcello.restelli%40polimi.it" title="marcello.restelli@polimi.it">Marcello Restelli</a>, <a class="profile-link" data-placement="top" data-toggle="tooltip" href="/profile?email=peters%40ias.tu-darmstadt.de" title="peters@ias.tu-darmstadt.de">Jan Peters</a>
</div>

<div class="note-meta-info">
    <span class="date">26 Sep 2019 (modified: 11 Mar 2020)</span>
    <span class="item">ICLR 2020 Conference Blind Submission</span>
    <span class="readers">Readers: <span class="readers-icon glyphicon glyphicon-globe"></span> Everyone</span>
    <span>7 Replies</span>
</div>

<a aria-expanded="false" class="note-contents-toggle" data-toggle="collapse" href="#rkgpv2VFvr-details-278" role="button">Show details</a><div class="collapse" id="rkgpv2VFvr-details-278"><div class="note-contents-collapse"><ul class="list-unstyled note-content">
<li>
    <strong class="note-content-field">Abstract:</strong>
    <span class="note-content-value">We study the benefit of sharing representations among tasks to enable the effective use of deep neural networks in Multi-Task Reinforcement Learning. We leverage the assumption that learning from different tasks, sharing common properties, is helpful to generalize the knowledge of them resulting in a more effective feature extraction compared to learning a single task. Intuitively, the resulting set of features offers performance benefits when used by Reinforcement Learning algorithms. We prove this by providing theoretical guarantees that highlight the conditions for which is convenient to share representations among tasks, extending the well-known finite-time bounds of Approximate Value-Iteration to the multi-task setting. In addition, we complement our analysis by proposing multi-task extensions of three Reinforcement Learning algorithms that we empirically evaluate on widely used Reinforcement Learning benchmarks showing significant improvements over the single-task counterparts in terms of sample efficiency and performance.</span>
</li>
<li>
    <strong class="note-content-field">Keywords:</strong>
    <span class="note-content-value">Deep Reinforcement Learning, Multi-Task</span>
</li>
<li>
    <strong class="note-content-field">TL;DR:</strong>
    <span class="note-content-value">A study on the benefit of sharing representation in Multi-Task Reinforcement Learning.</span>
</li>
<li>
    <strong class="note-content-field">Code:</strong>
    <span class="note-content-value"><a href="https://github.com/carloderamo/shared/tree/master" rel="nofollow" target="_blank">https://github.com/carloderamo/shared/tree/master</a></span>
</li>
<li>
    <strong class="note-content-field">Original Pdf:</strong>
    <span class="note-content-value"><a class="attachment-download-link" href="/attachment?id=rkgpv2VFvr&amp;name=original_pdf" target="_blank" title="Download Original Pdf"><span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span>  pdf</a></span>
</li>
</ul>
</div></div>
</li>

"""