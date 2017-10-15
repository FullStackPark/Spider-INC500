"""Create by xetra f han"""
"""Read the companies list from temp/INC500_1.json"""
"""Scrap the wikipedia and INC500 Company Profile Page"""
"""Save them to 'temp/html/wikipedia_list' and 'temp/html/INC500_company_details' respectively"""
"""Save json description file to temp/INC500_2.json"""

from ..Extension import YDHP_SplashRequester, YDHP_ScrapySystem
import scrapy
import json
import logging

json_output = {
     "wikipedias" : list()
    ,"inc_500_company_details": list()
}


class INC500_2(scrapy.Spider):
    global json_output

    name = "INC500_2"

    company_id = str()
    company_rank = str()
    company_url = str()
    company_name = str()

    def __init__(self):
        super(INC500_2, self).__init__()
        self.splash_requester = YDHP_SplashRequester.SplashRequester()

        """Read Json Company List from the last spider"""
        with open(file="temp/INC500_1.json", encoding="utf-8", mode="r") as f:
            self.json_obj = json.loads(f.read())

    def start_requests(self):
        for company in self.json_obj:
            """Get the company details from json"""
            self.company_id = str(company['id'])
            self.company_url = str(company['url'])
            self.company_name = str(company['company'])
            self.company_rank = str(company['rank'])

            """Request the company profile (detail page)"""
            target = "http://www.inc.com/profile/" + self.company_url
            yield self.splash_requester.splash_requests(target, self.callback_detail_page)

            """Request the wikipedia search page (search the company-name on wikipedia)"""
            wiki_query = {
                 "example_url": "https://en.wikipedia.org/wiki/Special:Search?search=theneedleand&go=Go"
                , "example_query": "theneedleand"
            }
            target = wiki_query["example_url"].replace(wiki_query["example_query"], self.company_name)
            yield self.splash_requester.splash_requests(target, self.callback_wiki_page)

            """We will go on to the next company"""
            logging.info("Company id: `" + self.company_rank + "` Finished Download")

    def callback_detail_page(self, response):
        """Write Company Profile page to file_path"""
        file_path = "temp/html/INC500_company_details/" + self.company_url + '.html'
        f = open(file=file_path, encoding="utf-8", mode="w")
        f.write(response.text)
        f.close()

        """Append the file info to json description file"""
        detail_page_info = {
             "file_path": file_path
            ,"company_url": self.company_url
            ,"company_id": self.company_id
        }
        json_output["inc_500_company_details"].append(detail_page_info)

        """Company Profile Page had finished download"""
        logging.info("Company: `" + self.company_name + "` profile had downloaded")

    def callback_wiki_page(self, response):
        """Write Wikipedia Search Result Page to file_path"""
        file_path = "temp/html/wikipedia_list/" + self.company_url + '.html'
        f = open(file=file_path, encoding="utf-8", mode="w")
        f.write(response.text)
        f.close()

        """Append the file info to json description file"""
        wiki_page_info = {
             "file_path": file_path
            ,"wikipedia_url" : response.url
            ,"company_id": self.company_id
        }
        json_output['wikipedias'].append(wiki_page_info)

        """Wikipedia Search Result Page had finished download"""
        logging.info(self.company_name + "had finished downloading wiki page")

    def __del__(self):
        """Dump Json Description File"""
        with open(file="temp/INC500_2.json", encoding="utf-8", mode="w") as f:
            f.write(json.dumps(json_output))

        YDHP_ScrapySystem.ScrapySystem.spider_work_finished(self.name)
