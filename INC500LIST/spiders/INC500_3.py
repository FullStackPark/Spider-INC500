"""Extracting and Appending other company information to the json file"""

import scrapy
import json
from scrapy.selector import Selector
import logging
import time
import copy
import threading

output_companies = list()
INC500_profiles = list()

class CompanySchema:
    company_schema = {
         "CompanyID": str()
        ,"Ranking": str()
        ,"CompanyName": str()
        ,"Industry": str()
        ,"Growth": str()
        ,"Revenue": str()
        ,"City": str()
        ,"StateAbbr": str()
        ,"StateName": str()
        ,"YearsOnINCList": str()
        ,"Partner": "None"

        ,"BriefDescription": str()
        ,"Description": str()
        ,"Leadership": str()
        ,"Founded": str()
        ,"ThreeYearGrowth": str()
        ,"Employees": str()
        ,"Website": str()
        ,"Location": str()

        ,"WikipediaPage": str()
        ,"WikipediaURL": str()
    }


class INC500_3:
    global output_companies, INC500_profiles

    """These xpath are used to extract data from the Company Profile Page"""
    xpath_article = '//*[@id="contentcontainer"]/section/div[2]/div/div/section/article'
    xpath_ranking = '//div[1]/div[1]/section[1]/section[1]/div[2]/dl[@class="rank"]/dd/text()'

    xpath_brief_description = '//div[1]/header/p/text()'
    xpath_description = '//section[2]/div/p/text()'
    xpath_leadership = '//section[1]/div[2]/dl[2]/dd/text()'
    xpath_founded = '//section[1]/div[3]/dl[5]/dd/text()'
    xpath_3_year_growth = '//section[1]/div[3]/dl[2]/dd/text()'
    xpath_employees = '//section[1]/div[3]/dl[6]/dd/text()'
    xpath_company_website = '//section[5]/dl/dd/a/@href'
    xpath_location = '//section[1]/div[3]/dl[4]/dd/text()'

    def __init__(self):
        f = open(file='temp/INC500_1.json', encoding='utf-8', mode='r')
        json_obj = json.loads(f.read())
        f.close()
        self.companies = json_obj

        f = open(file='temp/INC500_2.json', encoding='utf-8', mode='r')
        json_obj = json.loads(f.read())
        f.close()
        self.companies_info = json_obj

        for company_profile in self.companies_info['inc_500_company_details']:
            f = open(file=company_profile['file_path'], encoding='utf-8', mode='r')
            INC500_profiles.append(f.read())
            f.close()
            print("Loading company profile to memory `" + str(len(INC500_profiles)) + '`')

        logging.info("Output Companies Initialization Succeed")

    def extract_company(self, company):
        global output_companies, INC500_profiles

        cs = CompanySchema()
        if 'id' in company:
            cs.company_schema['CompanyID'] = company['id']
        if 'rank' in company:
            cs.company_schema['Ranking'] = company['rank']
        if 'company' in company:
            cs.company_schema['CompanyName'] = company['company']
        if 'industry' in company:
            cs.company_schema['Industry'] = company['industry']
        if 'growth' in company:
            cs.company_schema['Growth'] = company['growth']
        if 'revenue' in company:
            cs.company_schema['Revenue'] = company['revenue']
        if 'city' in company:
            cs.company_schema['City'] = company['city']
        if 'state_s' in company:
            cs.company_schema['StateAbbr'] = company['state_s']
        if 'state_l' in company:
            cs.company_schema['StateName'] = company['state_l']
        if 'yrs_on_list' in company:
            cs.company_schema['YearsOnINCList'] = company['yrs_on_list']
        for partner in company['partner_lists']:
            cs.company_schema['Partner'] += partner + " "

        for wikipedia_detail in self.companies_info['wikipedias']:
            if str(company['id']) == str(wikipedia_detail['company_id']):
                cs.company_schema['WikipediaPage'] = str(company['url']) + '.html'
                cs.company_schema['WikipediaURL'] = wikipedia_detail['wikipedia_url']

        for html in INC500_profiles:
            articles = Selector(text=html).xpath(self.xpath_article).extract()

            for article in articles:
                ranking = Selector(text=article).xpath(self.xpath_ranking).extract_first()
                if ranking is not None:
                    ranking = str(ranking).replace('#', '')

                    if str(ranking) == str(company['rank']):
                        print('mmp')
                        cs.company_schema['BriefDescription'] = Selector(text=article).xpath(
                            self.xpath_brief_description).extract_first()
                        cs.company_schema['Description'] = Selector(text=article).xpath(
                            self.xpath_description).extract_first()
                        cs.company_schema['Leadership'] = Selector(text=article).xpath(
                            self.xpath_leadership).extract_first()
                        cs.company_schema['Founded'] = Selector(text=article).xpath(
                            self.xpath_founded).extract_first()
                        cs.company_schema['ThreeYearGrowth'] = Selector(text=article).xpath(
                            self.xpath_3_year_growth).extract_first()
                        cs.company_schema['Employees'] = Selector(text=article).xpath(
                            self.xpath_employees).extract_first()
                        cs.company_schema['Website'] = Selector(text=article).xpath(
                            self.xpath_company_website).extract_first()
                        cs.company_schema['Location'] = Selector(text=article).xpath(
                            self.xpath_location).extract_first()

        output_companies.append(copy.deepcopy(cs.company_schema))

        # For Debug purpose
        print(str(cs.company_schema['Ranking']) + "` " + "Finished information collecting stage")

    def start_extraction(self):
        """Initialize output companies according to the result of spider 1"""
        threads = list()
        for company in self.companies:
            threads += [threading.Thread(target=self.extract_company, args=(company))]
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

        f = open(file='temp/INC500_3.json', encoding='utf-8', mode='w')
        f.write(json.dumps(output_companies))
        f.close()

if __name__ == '__main__':
    inc_500_3 = INC500_3()
    inc_500_3.start_extraction()
