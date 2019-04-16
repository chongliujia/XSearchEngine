# -*- coding: utf-8 -*-

# Scrapy settings for moscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'moscrapy'

SPIDER_MODULES = ['moscrapy.spiders']
NEWSPIDER_MODULE = 'moscrapy.spiders'
#HTTPERROR_ALLOWED_CODES = [403]





MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB   = "moscrapysdatabase"
MONGO_COLL = "csdn"

IPPOOL = [
    {"ipaddr": "171.44.208.216:33300"},
    {"ipaddr": "171.44.209.139:50216"},
    {"ipaddr": "180.108.195.233:53558"},
    {"ipaddr": "180.122.147.199:49605"},
    {"ipaddr": "61.174.152.139:41754"},
    {"ipaddr": "27.156.197.40:54985"},
    {"ipaddr": "27.157.3.137:25070"},
    {"ipaddr": "60.168.207.119:60230"},
    {"ipaddr": "58.19.81.96:34243"},
    {"ipaddr": "49.70.85.137:43149"}

]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'moscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
#HTTPCACHE_STORAGE = 'scrapy_splash.SplasgAwareFSCacheStorage'
#SPLASH_URL = 'http://localhost:8050'


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
     'moscrapy.middlewares.RandomUserAgent': 543,
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
#     'moscrapy.middlewares.PhantomJSDownloadHandler': 543,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#      'moscrapy.middlewares.MyproxiesMiddleware': 125
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy_splash.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
#    'moscrapy.middlewares.MyCustomDownloaderMiddleware': 543,
}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#   'moscrapy.pipelines.MoscrapyPipeline': 300,
    'moscrapy.pipelines.JsonWithEncodingPipeline': 300,
    'moscrapy.pipelines.ElasticsearchPipeline':300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
