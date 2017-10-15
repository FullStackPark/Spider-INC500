from scrapy_splash import SplashRequest as SP
from . import YDHP_ScrapySystem, YDHP_SiteInfo


class SplashRequester:
    timeout = 10

    def __init__(self, site_info=None):
        self.m_site_info = site_info

    def splash_requests(self, uris, callback):
        if type(uris) is list:
            for target in uris:
                if self.m_site_info is not None:
                    self.m_site_info.fetched_urls = target
                return SP(url=target, callback=callback, endpoint='render.html', args={'wait': self.timeout})
        elif type(uris) is str:
            if self.m_site_info is not None:
                self.m_site_info.fetched_urls = uris
            return SP(url=uris, callback=callback, endpoint='render.html', args={'wait': self.timeout})
        else:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("This is not a valid uri or uris list, your type: `%s` and value `%s`" % (type(uris), str(uris)))


