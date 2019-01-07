# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class rrs_cangkuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()     #省
    city = scrapy.Field()         #市
    name = scrapy.Field()         #仓库名字
    province_city = scrapy.Field()#省市区
    dizh = scrapy.Field()         #详细地址
    lianxDianh = scrapy.Field()   #电话
    shijMianj = scrapy.Field()    #实际面积
    shengyMianj = scrapy.Field()  #剩余面积
    jingwd = scrapy.Field()       #经纬度

class rrs_fuwuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()     #省
    city = scrapy.Field()         #市
    district = scrapy.Field()     #区
    name = scrapy.Field()         #仓库名字
    province_city = scrapy.Field()#省市区
    dizh = scrapy.Field()         #详细地址
    jingwd = scrapy.Field()       #经纬度

class kuaidiw_timeItem(scrapy.Item):
    name = scrapy.Field()         #快递名
    exname = scrapy.Field()       #exname
    logo = scrapy.Field()         #logo
    placefrom = scrapy.Field()    #出发地
    placeto = scrapy.Field()      #目的地
    time = scrapy.Field()         #时效

class kuaidiw_priceItem(scrapy.Item):
    name = scrapy.Field()         #快递名
    price = scrapy.Field()        #价格
    weight = scrapy.Field()       #重量
    exname = scrapy.Field()       #exname
    logo = scrapy.Field()         #logo
    placefrom = scrapy.Field()    #出发地
    placeto = scrapy.Field()      #目的地
    wastetime = scrapy.Field()    #wastetime