import jellyfish
import math
import numpy as np
from bs4 import BeautifulSoup
import requests
import threading
import re
from . import YDHP_SiteInfo, YDHP_ScrapySystem


class NextPage:

    def __init__(self, html, site_info):
        self.m_html = html
        self.m_site_info = site_info

    def next_page(self):
        """
        § Find all the links hidden inside html
        § Remove duplicated and fetched uris
        § jaro distance between these uris and the example uri
        § Find the mean distance
        § Select uris that distance < mean distance
        @:return list of urls that might be possible for next page(s)
        """
        possible_uris = self.find_a_href_tags()

        possible_uris = list(set(possible_uris))
        for fetched_url in self.m_site_info.fetched_urls:
            try:
                possible_uris.remove(fetched_url)
            except:
                pass

        re_possible_dicts_list = list()
        threads = []
        for target in possible_uris:
            threads.append(threading.Thread(target=self.jaro_distance(target, re_possible_dicts_list)))
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

        average_distance = self.avge_distance(re_possible_dicts_list)
        threads = list()
        for target in re_possible_dicts_list:
            threads.append(threading.Thread(target=self.remove_large_distance_target, args=(average_distance, target, re_possible_dicts_list)))
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

        next_uris = list()
        [next_uris.append(possible_dict['target']) for possible_dict in re_possible_dicts_list]

        return next_uris

    def remove_large_distance_target(self, average_distance, target, re_possible_dicts_list):
        if target['distance'] >= average_distance: re_possible_dicts_list.remove(target)

    def avge_distance(self, possible_dicts_list):
        distances = list()
        for possible_dict in possible_dicts_list:
            distances.append(possible_dict['distance'])
        return np.average(distances)

    def jaro_distance(self, target, re_possible_dicts_list):
            possible_dict = {
                 'target': target
                ,'distance': float(jellyfish.jaro_distance(self.m_site_info.start_url, target))
            }
            re_possible_dicts_list.append(possible_dict)

    def find_a_href_tags(self):
        bs_obj = BeautifulSoup(self.m_html, 'lxml')
        targets = []
        for target in bs_obj.findAll("a"):
            if 'href' in target.attrs:
                targets.append(target.attrs['href'])
        return targets



