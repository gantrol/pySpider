# -*- coding: utf-8 -*-

# Scrapy settings for huaban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'huaban'

SPIDER_MODULES = ['huaban.spiders']
NEWSPIDER_MODULE = 'huaban.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huaban (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json',
    'Accept-Encoding':  'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection':  'keep-alive',
    'Host': 'huaban.com',
    'Referer': 'http://huaban.com/favorite/beauty',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'_uab_collina=153572835042485686577819; __auc=1347e9a0165908af7a381f97a1d; __gads=ID=33e8c3248d63a6b2:T=1535728349:S=ALNI_MYuKpeTylFniJoQYMOFGPKElTIUOw; UM_distinctid=165928d4c649ca-046ed74c237be7-9393265-144000-165928d4c66119; CNZZDATA1256914954=1691845574-1536568949-null%7C1536568949; sid=K6dSvfe91zRqyV2iy5tar6qkG8X.4lv%2FrHOY6dyww6%2FtSCQqhVCB1h8SsHBeaVEulp%2FiX38; _hmt=1; uid=19470664; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAAC00lEQVRYR%2BWWT0hUURSHv6MTUZs2swgiZhH2RxdROEYUOBUYlhQRSAxEUUwhUbNIUFq4cFEKBg4RhkNRCbOQIgLDiEiFXDiK1CKMosUsQ5EMskU2J%2B6b%2B4ZxbMYpxsp8m7nz7n33nu%2F8fue8J6gq%2BS4RyTv%2FhyY7pzvzxikGZO3sLNFQiGAsRiwYJBSN0tLaSlN7uwlzBKgTmMoXs4IX6AO6Be4Um68gEHOod2qKSDhMOBJhyuvFwHU0NtLQ1VUuMFFIYApnzLp%2FFgQ4BQSA08BdYFCgWaENaAJiQAg4AVQCh4Bhe88H9APm96DdawZYB2wqRG2TnF9SpK%2Bujl0jxkmpK%2BHz4UskyoFJIAKEgQqgFrgHXARagFbgBrAbOGABzP13wGYLYrY0zxko86wZHwMeFaL4L4HkstbPQKwibl2st4EZEMdaCtUm43ZsLHcbMEVnQGozFO0XGFrMusUCSdjMdwBHbJZNVs3%2FBqA5QxEXxNjOCdoq8yFDkaUBKaRrAY22Hp4C24ALwE2byY%2FAgLVYFAgCZ60abh3FAQ9QCmy36pj6KqgrFqxITmmX03vkv3khrlgQfRmv4Js8QfChJFilh%2FlesoGk9jpJKZF6qa58Zobz1%2Bp12Vdlai196UC8A5HL7j6yt%2BqNO6lDYzV2z089W8d906u%2F5q6A3%2F3WcgKckweI3pLqKvOOQQfHLiG8dSFS90YfO6d79Apz0oNIcxoyFWg3JXKOZLIGkTIJ%2BI%2FOAzVrVNt6tozvWBKQzCDdw3Uw3oKHh%2FOyOjg6jGivgXWgVN%2B7quhQPIxKvQT8e5zsq7bh0ZMLVFlykIzDHWupHpeA%2F3zaGlmqLQBJ2Wq%2FBPw7%2FyqIVWUc1RcInxFmXJulYZaDIg6IzSroBB6uZtpi2dRIVld6nV2oubqWbQAbHUtlda1U90vep4RrlPLc7Y6Ta74QK3tV%2FK612EdesedXzCfKD1HkETenQIVMAAAAAElFTkSuQmCC%2CWin32.1536.864.24; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1539492274,1540619161,1541761884; _trs_uv=joa0x5cb_1245_8a52; Hm_lvt_e9fe99c2267a6f7a9215a8724ce995b4=1541768102; Hm_lpvt_e9fe99c2267a6f7a9215a8724ce995b4=1541768102; _ga=GA1.2.2132483355.1541768102; _gid=GA1.2.587293805.1541768102; md_href=http%3A%2F%2Fhuaban.com%2Fboards%2F18398025%3Fmd%3Dnewbn%26beauty%3D; md=newbn; CNZZDATA1256903590=1150130295-1535761091-%7C1541773377; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1541775234069%26urlname%7Ck5spfh6f1d%7C1541775234070%26md%7Cnewbn%7C1541775235070; __asc=d64e2570166f93977f10a32fa22; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1541779640',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'huaban.middlewares.HuabanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'huaban.middlewares.HuabanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'huaban.pipelines.HuabanPipeline': 300,
    'huaban.pipelines.ImagePipeline': 100,
}

IMAGES_STORE = './images/beauty'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
