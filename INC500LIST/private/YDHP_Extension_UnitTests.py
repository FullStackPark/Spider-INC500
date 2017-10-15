from ..Extension import YDHP_SplashRequester, YDHP_ScrapySystem, YDHP_SiteInfo, YDHP_ScrapyRecorder, YDHP_NextPages

import datetime


class YDHP_Extension_UnitTests:
    def __init__(self):
        YDHP_Extension_UnitTests.next_page()
        YDHP_ScrapySystem.ScrapySystem.module_passed('YDHP_NextPages')
        YDHP_Extension_UnitTests.splash_request()
        YDHP_ScrapySystem.ScrapySystem.module_passed('YDHP_SplashRequester')
        YDHP_Extension_UnitTests.scrapper_recorder()
        YDHP_ScrapySystem.ScrapySystem.module_passed('YDHP_ScrapyRecorder')
        YDHP_Extension_UnitTests.site_info()
        YDHP_ScrapySystem.ScrapySystem.module_passed('YDHP_ScrapyRecorder')

        YDHP_ScrapySystem.ScrapySystem.unit_test_finished()

    @staticmethod
    def site_info():
        module_name = "Site URI"
        example_query = {
            'example_uri': 'http://www.dogpile.com/info.dogpl/search/images?qsi=1&fcoid=4&fcop=results-bottom&om_nextpage=True&fpid=2&q=stevejobs'
        }
        if YDHP_SiteInfo.SiteInfo.extract_site_uri(example_query) is not None:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        module_name = "Start URI"
        site_info = YDHP_SiteInfo.SiteInfo(example_query)
        site_info.start_url = "https://www.yahoo.com/"
        site_info.fetched_urls = site_info.start_url
        if "https://www.yahoo.com/" == site_info.start_url:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        module_name = "Pending URI"
        site_info = YDHP_SiteInfo.SiteInfo(example_query)
        site_info.pending_urls = ['https://yahoo.com', "https://duckduckgo.com", 'https://yahoo.com',
                                  "https://duckduckgo.com"]
        if 'https://yahoo.com' in site_info.pending_urls and "https://duckduckgo.com" in site_info.pending_urls:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name + "list mode")
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        site_info = YDHP_SiteInfo.SiteInfo(example_query)
        site_info.pending_urls = "https://yahoo.com"
        if "https://yahoo.com" in site_info.pending_urls:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name + "string mode")
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        module_name = "Fetched URI"
        site_info = YDHP_SiteInfo.SiteInfo(example_query)
        site_info.start_url = 'https://yahoo.com'
        site_info.pending_urls = ['https://baidu.com', 'https://www.bing.com']
        site_info.pending_urls = "https://google.com"
        site_info.fetched_urls = ['https://yahoo.com', 'https://baidu.com', 'https://www.bing.com',
                                  "https://google.com"]

        if 'https://yahoo.com' in site_info.fetched_urls and \
            'https://baidu.com' in site_info.fetched_urls and \
            'https://www.bing.com' in site_info.fetched_urls and \
            "https://google.com" in site_info.fetched_urls and \
                site_info.pending_urls == [] and 'https://yahoo.com' == site_info.start_url:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

    @staticmethod
    def scrapper_recorder():
        scrapper_recorder = YDHP_ScrapyRecorder.ScrapperRecorder()

        module_name = scrapper_recorder.__class__.__name__ + "time_consumed"
        if type(scrapper_recorder.time_consumed) is datetime:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        elif type(scrapper_recorder.time_consumed_string()) is str:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

    @staticmethod
    def splash_request():
        site_info = YDHP_SiteInfo.SiteInfo(example_query={
             'query_string': 'stevejobs'
            ,'example_uri': 'http://www.dogpile.com/info.dogpl/search/images?qsi=1&fcoid=4&fcop=results-bottom&om_nextpage=True&fpid=2&q=stevejobs'
        })
        sp = YDHP_SplashRequester.SplashRequester(site_info)

        module_name = "splash_request + string"
        try:
            yield sp.splash_requests(uris="https://www.bing.com/", callback=lambda response: YDHP_ScrapySystem.ScrapySystem.test_passed(module_name))
        except:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        module_name = "splash_request + list"
        try:
            yield sp.splash_requests(uris=["https://www.bing.com/"], callback=lambda response: YDHP_ScrapySystem.ScrapySystem.test_passed(module_name))
        except:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

    @staticmethod
    def next_page():
        site_info = YDHP_SiteInfo.SiteInfo(example_query={
            'example_uri': 'https://baidu.com/zhixingzhewangyuqi'
        })
        site_info.start_url = "https://baidu.com/"
        next_page = YDHP_NextPages.NextPage('<html><body><a href="https://baidu.com/></a></body></html>', site_info)

        module_name = "Larget Distance Target Removal"
        possible_dicts_list = [{'distance': 1}, {'distance': 4}]
        next_page.remove_large_distance_target(3, {'distance': 4}, possible_dicts_list)
        if {'distance': 4} not in possible_dicts_list:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        module_name = "Average Distance"
        possible_dicts_list = [{'distance': 4}, {'distance': 4}]
        average_distance = next_page.avge_distance(possible_dicts_list)
        if average_distance == 4:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

        module_name = "Jaro Distance"
        possible_dicts_list = list()
        next_page.jaro_distance('http://sogou.com/', possible_dicts_list)
        for dict in possible_dicts_list:
            if 'distance' not in dict: YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)
        YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)

        module_name = "Fina <a href = ""> tags"
        if not next_page.find_a_href_tags() == []:
            YDHP_ScrapySystem.ScrapySystem.test_passed(module_name)
        else:
            YDHP_ScrapySystem.ScrapySystem.test_failed(module_name)

