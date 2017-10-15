import re

from . import YDHP_ScrapySystem


class SiteInfo:
    def __init__(self, example_query):
        self._site_url = SiteInfo.extract_site_uri(example_query)
        self._scrap_urls = list()
        self._pending_urls = list()
        self._fetched_urls = list()
        self._start_url = None

    """
    e.g. site_url = "https://www.yahoo.com"
    """
    @property
    def site_url(self):
        return self._site_url

    @site_url.setter
    def site_url(self, value):
        self._site_url = value

    """
    Extract the url from dict ['example_uri']
    """
    @staticmethod
    def extract_site_uri(example_query):
        try:
            return re.match(r'(^(https?):\/\/|^)(([^\.]+)\.([^\.]+\.[^\/$]+)|([^\.]+\.[^\/$]+))?',
                            example_query['example_uri']).group(0)
        except:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("Example URI is not working")

    # @return: the first uri that need to be crawled
    @property
    def start_url(self):
        if len(self._scrap_urls) > 0:
            return self._start_url
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("No start_url available, set it first ?")

    @start_url.setter
    def start_url(self, value):
        if type(value) is str:
            self._start_url = value

            self._scrap_urls.append(value)
            self._pending_urls.append(value)
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("start_url expect a string uri value")

    # URIs that are waiting to be crawled
    @property
    def pending_urls(self):
        return self._pending_urls

    @pending_urls.setter
    def pending_urls(self, value):
        if type(value) is str:
            self._scrap_urls.append(value)
            self._pending_urls.append(value)
            self._scrap_urls = list(set(self._scrap_urls))
            self._pending_urls = list(set(self._pending_urls))
        elif type(value) is list:
            for target in value:
                self._scrap_urls.append(target)
                self._pending_urls.append(target)
                self._scrap_urls = list(set(self._scrap_urls))
                self._pending_urls = list(set(self._pending_urls))
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("This is not a valid pending_urls type [`%s`]" % type(value))

    # Stores all the urls that have been fetched
    @property
    def fetched_urls(self):
        return self._fetched_urls

    @fetched_urls.setter
    def fetched_urls(self, value):
        if type(value) is str:
            try:
                self._fetched_urls.append(value)
                self._pending_urls.remove(value)
            except:
                pass
            finally:
                self._fetched_urls = list(set(self._fetched_urls))
                self.pending_urls = list(set(self.pending_urls))
        elif type(value) is list:
            for target in value:
                try:
                    self._fetched_urls.append(target)
                    self._pending_urls.remove(target)
                except:
                    pass
                finally:
                    self._fetched_urls = list(set(self._fetched_urls))
                    self.pending_urls = list(set(self.pending_urls))
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("This is not a valid fetched_urls type [`%s`]" % type(value))





