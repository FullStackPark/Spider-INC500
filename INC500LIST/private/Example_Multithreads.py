import scrapy
from scrapy_splash import SplashRequest
import json
import copy
import datetime
import time
import re
from bs4 import BeautifulSoup
import threading

from .. import YDHP_SiteInfo
from .. import YDHP_ScrapyRecorder
from .. import YDHP_ScrapySystem
from .. import YDHP_SplashRequests
from .. import YDHP_NextPages
from .. import UnitTests
from .. import is_debug
from . import query_string

"""
Output: (dict)
    query_string                    - string of the query                           (str)
    result_page                     - how many uris had been successfully crawled   (int)
    time_consumed                   - total time spend on the site                  (str)
    search_engine_name              - name of the spider(search engine name)        (str)
    results                         - the result of crawler                         (list)
        URI                         - HTML uri                                      (str)
        HTML                        - HTML content (js rendered)                    (str)
"""

final_output = {
     'query_string': str()
    ,'result_page': 0
    ,'time_consumed': str()
    ,'search_engine_name': None
    ,'results': list()
}


class Dogpile(scrapy.Spider):
    name = "Dogpile_ISEHTMLD"

    """
    Take a search try and analysis the result
    """
    def start_requests(self):
        yield self.m_splash_requester.splash_requests(self.m_site_info.start_url, self.response)

    def response(self, response):
        """
        1. Is this response okay?
        """
        bs_obj = BeautifulSoup(response.text, 'lxml')
        img_tags = bs_obj.findAll("img")
        if len(img_tags) > 0:
            """
            $ Find the next uri then start request
            $ Save the response data
            """
            self.m_final_output['results'].append({'URI': response.url, 'HTML': response.text})
            self.m_final_output['result_page'] += 1

            next_page = YDHP_NextPages.NextPage(response.text, self.m_site_info).next_page()
            for target in next_page:
                yield self.m_splash_requester.splash_requests(target, self.response)
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("Check your internet connection or this spider need to be updated %s " % self.name)

    def close(spider, reason):
        global final_output
        final_output['query_string'] = spider.m_query_string
        final_output['time_consumed'] = spider.m_recorder.time_consumed_string()
        final_output['search_engine_name'] = spider.name

        print(final_output)

        print('Job Done')

    def __init__(self):
        global final_output
        super(Dogpile, self).__init__()
        if is_debug: ut = UnitTests.UnitTests()

        self.m_example_query = {
             'query_string': 'stevejobs'
            ,'example_uri': 'http://www.dogpile.com/info.dogpl/search/images?qsi=1&fcoid=4&fcop=results-bottom&om_nextpage=True&fpid=2&q=stevejobs'
        }
        self.m_site_info = None

        self.m_query_string = None

        self.m_final_output = final_output

        self.m_recorder = None

        threads = list()
        threads += [threading.Thread(target=self.site_info), threading.Thread(target=self.parse_query), threading.Thread(target=self.start_recording)]
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

        self.parse_start_uri()
        self.m_splash_requester = YDHP_SplashRequests.SplashRequests(site_info=self.m_site_info)

    def site_info(self):
        self.m_site_info = YDHP_SiteInfo.SiteInfo(self.m_example_query)

    def parse_query(self):
        self.m_query_string = query_string.decode('utf-8')

    def start_recording(self):
        self.m_recorder = YDHP_ScrapyRecorder.ScrapperRecorder()

    def parse_start_uri(self):
        self.m_site_info.start_url = self.m_example_query['example_uri'].replace(self.m_example_query['query_string'], self.m_query_string)
