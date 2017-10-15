"""Created by xetra f han"""
"""Download the json string from INC 500 Website"""

from ..Extension import YDHP_SplashRequester, YDHP_ScrapySystem
import scrapy
import json
from bs4 import BeautifulSoup

json_response = str()


class INC500_1(scrapy.Spider):
    name = "INC500_1"
    target_url = "https://www.inc.com/inc5000list/json/inc5000_2017.json"

    def start_requests(self):
        yield self.splash_requester.splash_requests(self.target_url, self.callback_parse)

    def callback_parse(self, response):
        global json_response
        try:
            bs_obj = BeautifulSoup(response.text, 'lxml')
            for json_level in bs_obj.findAll('pre'):
                json_text = json_level.get_text()
                json_response = json.loads(json_text)
        except:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("This response is not a json anymore, update the INC500_1 spider")

        with open("temp/INC500_1.json", mode='wb') as f:
            # f.write(json.dumps(json_response).encode("utf-8"))
            f.write(response.body)
        YDHP_ScrapySystem.ScrapySystem.spider_work_finished(self.name)

    def __init__(self):
        super(INC500_1, self).__init__()
        self.splash_requester = YDHP_SplashRequester.SplashRequester()
