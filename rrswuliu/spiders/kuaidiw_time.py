# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from rrswuliu.items import kuaidiw_timeItem
import json
import time
from scrapy.mail import MailSender
from scrapy.utils.project import get_project_settings
class KuaidiwTimeSpider(scrapy.Spider):
    name = 'kuaidiw_time'
    allowed_domains = ['www.kuaidi.com']
    start_urls = []

    def start_requests(self):
        url = "http://www.kuaidi.com/shixiaoindex.html"
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Firefox(firefox_options=options)
        self.browser.set_page_load_timeout(40)
        print("开始爬取快递网的时效信息！")
        self.browser.get(url)
        time.sleep(3)
        #print(self.browser.page_source)
        addressList = []
        self.browser.find_element_by_id("area_s").click()
        self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
        for x in self.browser.find_elements_by_xpath("//div[@id='content2_s']/dl/dd/a"):
            province = x.text
            print(province)
            x.click()
            if province in ["北京","重庆","上海","天津","广西","内蒙古","宁夏","新疆","西藏"]:
                if province in ["北京","重庆","上海","天津"]:
                    for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                        zone = z.text
                        print(zone)
                        if province in ["北京"]:
                            data = province+"-北京市-"+zone
                        elif province in ["重庆"]:
                            data = province+"-重庆市-"+zone
                        elif province in ["上海"]:
                            data = province+"-上海市-"+zone
                        else:
                            data = province+"-天津市-"+zone
                        addressList.append(data)
                    self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
                elif province in ["广西"]:
                    for y in self.browser.find_elements_by_xpath("//div[@id='content3_s']/a"):
                        city = y.text
                        print(city)
                        y.click()
                        for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                            zone = z.text
                            print(zone)
                            data = province+"壮族自治区-"+city+"-"+zone
                            addressList.append(data)
                        self.browser.find_elements_by_xpath("//a[@class='biaoqian3_s']")[0].click()
                    self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
                elif province in ["内蒙古"]:
                    for y in self.browser.find_elements_by_xpath("//div[@id='content3_s']/a"):
                        city = y.text
                        print(city)
                        y.click()
                        for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                            zone = z.text
                            print(zone)
                            data = province+"自治区-"+city+"-"+zone
                            addressList.append(data)
                        self.browser.find_elements_by_xpath("//a[@class='biaoqian3_s']")[0].click()
                    self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
                elif province in ["宁夏"]:
                    for y in self.browser.find_elements_by_xpath("//div[@id='content3_s']/a"):
                        city = y.text
                        print(city)
                        y.click()
                        for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                            zone = z.text
                            print(zone)
                            data = province+"回族自治区-"+city+"-"+zone
                            addressList.append(data)
                        self.browser.find_elements_by_xpath("//a[@class='biaoqian3_s']")[0].click()
                    self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
                elif province in ["新疆"]:
                    for y in self.browser.find_elements_by_xpath("//div[@id='content3_s']/a"):
                        city = y.text
                        print(city)
                        y.click()
                        for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                            zone = z.text
                            print(zone)
                            data = province+"-"+city+"-"+zone
                            addressList.append(data)
                        self.browser.find_elements_by_xpath("//a[@class='biaoqian3_s']")[0].click()
                    self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
                else:
                    for y in self.browser.find_elements_by_xpath("//div[@id='content3_s']/a"):
                        city = y.text
                        print(city)
                        y.click()
                        for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                            zone = z.text
                            print(zone)
                            data = province+"-"+city+"-"+zone
                            addressList.append(data)
                        self.browser.find_elements_by_xpath("//a[@class='biaoqian3_s']")[0].click()
                    self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
            else:
                for y in self.browser.find_elements_by_xpath("//div[@id='content3_s']/a"):
                    city = y.text
                    print(city)
                    if city in ["永济市","河津市","侯马市"]:
                        print("======")
                    else:
                        y.click()
                        for z in self.browser.find_elements_by_xpath("//div[@id='content4_s']/a"):
                            zone = z.text
                            print(zone)
                            data = province+"省-"+city+"-"+zone
                            addressList.append(data)
                        self.browser.find_elements_by_xpath("//a[@class='biaoqian3_s']")[0].click()
                self.browser.find_elements_by_xpath("//a[@class='biaoqian2_s']")[0].click()
        iofourl = 'http://www.kuaidi.com/orderindex-timeout.html'
        for placefrom in addressList:
            for placeto in addressList:
                formdata = {'placefrom':placefrom,'placeto':placeto}
                time.sleep(0.1)
                yield scrapy.FormRequest(url=iofourl,method='POST',formdata=formdata, meta = formdata,callback = self.parse_content,dont_filter = True)
        self.browser.close()
        
    def parse_content(self,response):
        print(response.meta['placefrom'],response.meta['placeto'])
        datas = json.loads(response.text)['data']
        for data in datas:
            item = kuaidiw_timeItem()
            item['name'] = data['name']
            item['exname'] = data['exname']
            item['logo'] = 'http://www.kuaidi.com'+data['ico']
            item['placefrom'] = response.meta['placefrom']
            item['placeto'] = response.meta['placeto']
            item['time'] = data['timeavg']
            yield item

    def close(self):
        settings = get_project_settings()
        mailer = MailSender.from_settings(settings = settings)
        body = u'''
        kuaidiw_time爬虫结束！
        '''
        subject = u'爬虫结束邮件'
        mailer.send(to=["******@qq.com"], subject = subject, body = body)