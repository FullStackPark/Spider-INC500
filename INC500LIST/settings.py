# -*- coding: utf-8 -*-

BOT_NAME = 'INC500LIST'

SPIDER_MODULES = ['INC500LIST.spiders']
NEWSPIDER_MODULE = 'INC500LIST.spiders'

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

SPLASH_URL = 'http://45.32.70.135:8050'

SPIDER_MIDDLEWARES = {
	'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware':723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY = 2

COOKIES_ENABLED = False

# DEFAULT_REQUEST_HEADERS = {
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br'
# }

