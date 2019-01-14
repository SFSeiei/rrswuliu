# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.support.select import Select
from rrswuliu.items import rrs_cangkuItem
from bs4 import BeautifulSoup
from js2xml.utils.vars import get_vars
import re
import time
import os
import json
from scrapy.mail import MailSender
from scrapy.utils.project import get_project_settings

class Rrswl_cangkuSpider(scrapy.Spider):
    name = 'rrs_cangku'
    allowed_domains = ['www.rrswl.com']
    start_urls = []
    def start_requests(self):
        url = "https://www.rrswl.com/ckwd/searchCangku?cangkLeix=0&quyucode="
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Firefox(firefox_options=options)
        self.browser.set_page_load_timeout(40)
        print("开始爬取仓库！")
        self.browser.get(url)
        time.sleep(3)
        #print(self.browser.page_source)
        #获取下拉菜单
        p = Select(self.browser.find_element_by_xpath('//*[@id="province"]')).options
        for option1 in p:
            value1 = option1.get_attribute('value')   #获取下拉选项的value值
            text1 = option1.text                      #获取下拉文本
            if value1 !="":
                item = rrs_cangkuItem()
                item["province"] = text1
                #print(value1,text1)
                option1.click()
                c = Select(self.browser.find_element_by_xpath('//*[@id="city"]')).options
                for option2 in c:
                    value2 = option2.get_attribute('value')
                    text2 = option2.text
                    if value2 !="":
                        item["city"] = text2
                        FormData = {'chengsh': value2, 'shengf': value1}
                        #print(value2,text2)
                        time.sleep(0.1)
                        yield scrapy.FormRequest(url=url,formdata=FormData,meta=item,callback=self.parse_content,dont_filter=True)
        self.browser.close()
        
    def parse_content(self,response):
        #print(response.meta["province"])
        #print(response.text)
        #print(response.xpath('//script/text()')[-1].extract())
        f = open("D:\\"+response.meta["city"]+".txt",'w+')
        f.writelines(response.xpath('//script/text()')[-1].extract())
        f.seek(0)
        bzlist = f.readlines()[2]
        f.close()
        os.remove("D:\\"+response.meta["city"]+".txt")
        pattern = re.compile(r'var bzlist = \[.*?\];$', re.MULTILINE | re.DOTALL)
        #print(pattern.search(bzlist).group(0)[13:-1])
        #print(get_vars(js2xml.parse(bzlist)))
        datas = json.loads(pattern.search(bzlist).group(0)[13:-1])
        for data in datas:
            item = rrs_cangkuItem()
            item['province'] = response.meta["province"]
            item['city'] = response.meta["city"]
            item['name'] = data['cangkMingch']
            item['province_city'] = data['shengf']+data['chengsh']
            item['dizh'] = data['dizh']
            item['lianxDianh'] = data['lianxDianh']
            item['shijMianj'] = data['shijMianj']
            item['shengyMianj'] = data['shengyMianj']
            item['jingwd'] = data['jingwd']
            yield item
            
    def close(self):
        settings = get_project_settings()
        mailer = MailSender.from_settings(settings = settings)
        body = u'''
        rrs_cangku爬虫结束！
        '''
        subject = u'爬虫结束邮件'
        mailer.send(to=["******@qq.com"], subject = subject, body = body)