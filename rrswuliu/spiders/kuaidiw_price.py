# -*- coding: utf-8 -*-
import scrapy
import json
import time
from rrswuliu.items import kuaidiw_priceItem
from scrapy.mail import MailSender
from scrapy.xlib.pydispatch import dispatcher
from scrapy.utils.project import get_project_settings

class KuaidiwPriceSpider(scrapy.Spider):
    name = 'kuaidiw_price'
    allowed_domains = ['www.kuaidi.com']
    start_urls = ['http://www.kuaidi.com/orderindex-ajaxgetprovince.html']
    pros = []
    routes = []
    
    def parse(self, response):
        p_infos = [json.loads(response.text)['ltagtg'],json.loads(response.text)['lthgtk'],json.loads(response.text)['ltlgts'],json.loads(response.text)['lttgtz']]
        for p_info in p_infos:
            for pro in p_info:
                province = {}
                province['pid'] = pro['id']
                province['pname'] = pro['name']
                print(province)
                time.sleep(0.05)
                yield scrapy.Request(url='http://www.kuaidi.com/orderindex-ajaxgetcounty-'+pro['id']+'-city.html',meta = province,callback=self.parse_city,dont_filter = True)
        #print(self.pros)
        
    def parse_city(self, response):
        #print(response.meta['pid'],response.meta['pname'])
        c_infos = json.loads(response.text)
        #print(c_infos)
        for c_info in c_infos:
            pro_city = {}
            pro_city['pid-cid'] = response.meta['pid']+'-'+c_info['id']
            pro_city['pname-cname'] = response.meta['pname']+'-'+c_info['name']  
            time.sleep(0.1)
            yield scrapy.Request(url='http://www.kuaidi.com/orderindex-ajaxgetcounty-'+c_info['id']+'-classify.html',meta = pro_city,callback=self.parse_classify,dont_filter = True)
           
    def parse_classify(self, response):
        '''
        if response.meta['pname'] in self.pros:
            pass
        else:
            self.pros.append(response.meta['pname'])
        print(self.pros) 
        '''
        cl_infos = json.loads(response.text)
        for cl_info in cl_infos:
            pro_city_cla = {}
            pro_city_cla['pid-cid-clid'] = response.meta['pid-cid']+'-'+cl_info['id']
            pro_city_cla['pname-cname-clname'] = response.meta['pname-cname']+'-'+cl_info['name']
            #print(pro_city_cla)
            self.routes.append(pro_city_cla)
        for placefrom in self.routes:
            for placeto in self.routes:
                for weight in [0.5,1,2]:
                    formdata ={'sadd':placefrom['pname-cname-clname'],'saddcode':placefrom['pid-cid-clid'],'dadd':placeto['pname-cname-clname'],'daddcode':placeto['pid-cid-clid'],'weight':str(weight)}
                    time.sleep(0.1)
                    yield scrapy.FormRequest(url='http://www.kuaidi.com/orderindex-waybillinfo.html',method='POST',formdata = formdata, meta = formdata,callback = self.parse_content,dont_filter = True)
    def parse_content(self,response):
        #print(json.loads(response.text))
        datas = json.loads(response.text)['data']
        for data in datas:
            item = kuaidiw_priceItem()
            item['name'] = data['name']
            item['price'] = data['price']
            item['weight'] = response.meta['weight']
            item['exname'] = data['exname']
            item['logo'] = 'http://www.kuaidi.com'+data['ico']
            item['placefrom'] = response.meta['sadd']
            item['placeto'] = response.meta['dadd']
            if data['wastetime'] =='':
                item['wastetime'] = '暂无'
            else:
                item['wastetime'] = data['wastetime']
            yield item
    
    def close(self):
        settings = get_project_settings()
        mailer = MailSender.from_settings(settings = settings)
        body = u'''
        kuaidiw_price爬虫结束！
        '''
        subject = u'爬虫结束邮件'
        mailer.send(to=["******@qq.com"], subject = subject, body = body)
