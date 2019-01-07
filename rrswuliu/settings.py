# -*- coding: utf-8 -*-

# Scrapy settings for rrswuliu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'rrswuliu'

SPIDER_MODULES = ['rrswuliu.spiders']
NEWSPIDER_MODULE = 'rrswuliu.spiders'

PROXIES = ['http://101.4.132.21:80','http://123.132.232.254:61017',
           'http://183.232.113.50:80','http://119.180.181.249:8060']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rrswuliu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'rrswuliu.middlewares.RrswuliuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
    #'rrswuliu.middlewares.RrswuliuDownloaderMiddleware': 543,
    #'rrswuliu.middlewares.ProxyMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'rrswuliu.pipelines.rrs_cangkuPipeline': 300,
#    'rrswuliu.pipelines.rrs_fuwuPipeline': 300,
#    'rrswuliu.pipelines.kuaidiw_timePipeline': 300,
#    'rrswuliu.pipelines.kuaidiw_pricePipeline': 300
}

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


MAIL_HOST = 'smtp.qq.com'     ##默认值: 'localhost'发送email的SMTP主机(host)
MAIL_FROM = '740969264@qq.com'##'scrapy@localhost'用于发送email的地址(address)(填入 From:) 。
MAIL_USER = '740969264@qq.com'##默认值: None SMTP用户。如果未给定，则将不会进行SMTP认证(authentication)。
MAIL_PASS = 'mslnstaoosptbeji'##默认值: None 用于SMTP认证，与 MAIL_USER 配套的密码。
MAIL_PORT = 25                ##默认值: 25发用邮件的SMTP端口
MAIL_TLS = False              ##默认值: False 强制使用STARTTLS。STARTTLS能使得在已经存在的不安全连接上，通过使用SSL/TLS来实现安全连接。
MAIL_SSL = False              ##默认值: False强制使用SSL加密连接
