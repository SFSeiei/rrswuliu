# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.support.select import Select
from rrswuliu.items import rrs_fuwuItem
import time
import os
import re
import json
from scrapy.mail import MailSender
from scrapy.utils.project import get_project_settings

class RrswlFuwuSpider(scrapy.Spider):
    name = 'rrs_fuwu'
    allowed_domains = ['www.rrswl.com']
    start_urls = []
    
    def start_requests(self):
        url = "https://www.rrswl.com/ckwd/searchWangdian?cangkLeix=1"
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Firefox(firefox_options=options)
        self.browser.set_page_load_timeout(40)
        print("开始爬取服务网点！")
        self.browser.get(url)
        time.sleep(3)
        #print(self.browser.page_source)
        #获取下拉菜单
        p = Select(self.browser.find_element_by_xpath('//*[@id="province"]')).options
        for option1 in p:
            value1 = option1.get_attribute('value')   #获取下拉选项的value值
            text1 = option1.text                      #获取下拉文本
            if value1 !="":
                item = rrs_fuwuItem()
                item["province"] = text1
                option1.click()
                c = Select(self.browser.find_element_by_xpath('//*[@id="city"]')).options
                for option2 in c:
                    value2 = option2.get_attribute('value')
                    text2 = option2.text
                    if value2 !="":
                        item["city"] = text2
                        option2.click()
                        d = Select(self.browser.find_element_by_xpath('//*[@id="district"]')).options
                        for option3 in d:
                            value3 = option3.get_attribute('value')
                            text3 = option3.text
                            if value3 !="":
                                item['district'] = text3
                                #print(value1,text1,value2,text2,value3,text3)
                                FormData = {'chengsh': value2, 'qux':value3,'shengf': value1}
                                time.sleep(0.1)
                                yield scrapy.FormRequest(url=url,formdata=FormData,meta=item,callback=self.parse_content,dont_filter=True)
        self.browser.close()
        
    def parse_content(self,response):
        #print(response.meta["province"])
        #print(response.text)
        #print(response.xpath('//script/text()')[-1].extract())
        f = open("D:\\"+response.meta["district"]+".txt",'w+')
        f.writelines(response.xpath('//script/text()')[-1].extract())
        f.seek(0)
        bzlist = f.readlines()[2]
        #print(bzlist)
        f.close()
        os.remove("D:\\"+response.meta["district"]+".txt")
        pattern = re.compile(r'var bzlist = \[.*?\];$', re.MULTILINE | re.DOTALL)
        print(pattern.search(bzlist).group(0)[13:-1])
        #print(get_vars(js2xml.parse(bzlist)))
        datas = json.loads(pattern.search(bzlist).group(0)[13:-1])
        #print(datas)
        for data in datas:
            item = rrs_fuwuItem()
            item['province'] = response.meta["province"]
            item['city'] = response.meta["city"]
            item['district'] = response.meta["district"]
            item['name'] = data['cangkMingch']
            item['province_city'] = data['shengf']+data['chengsh']
            item['dizh'] = data['dizh']
            item['jingwd'] = data['jingwd']
            #print(item)
            yield item

    def close(self):
        settings = get_project_settings()
        mailer = MailSender.from_settings(settings = settings)
        body = u'''
        rrs_fuwu爬虫结束！
        '''
        subject = u'爬虫结束邮件'
        mailer.send(to=["740969264@qq.com"], subject = subject, body = body)