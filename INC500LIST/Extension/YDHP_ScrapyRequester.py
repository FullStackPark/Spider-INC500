import scrapy
from . import YDHP_ScrapySystem

"""No JS Renderer"""


class ScrapyRequester:

    def __init__(self, site_info=None):
        self.m_site_info = site_info

    def scrapy_requests(self, uris, callback):
        if type(uris) is list:
            for target in uris:
                if self.m_site_info is not None:
                    self.m_site_info.fetched_urls = target
                return scrapy.Request(url=target, callback=callback)
        elif type(uris) is str:
            if self.m_site_info is not None:
                self.m_site_info.fetched_urls = uris
            return scrapy.Request(url=uris, callback=callback)
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("This is not a valid uri or uris list, your type: `%s` and value `%s`" % (type(uris), str(uris)))
