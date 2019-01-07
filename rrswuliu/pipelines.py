# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class rrs_cangkuPipeline(object):
    def process_item(self, item, spider):
        with open('rrs_cangku.csv', 'a', newline='') as csvou:
            writer = csv.writer(csvou, dialect='excel')
            rows = item['province'], item['city'], item['name'], item['province_city'], item['dizh'], \
               item['lianxDianh'], \
               item['shijMianj'], item['shengyMianj'],item['jingwd']
            writer.writerow(rows)
        return item

class rrs_fuwuPipeline(object):
    def process_item(self, item, spider):
        with open('rrs_fuwu.csv', 'a', newline='') as csvou:
            writer = csv.writer(csvou, dialect='excel')
            rows = item['province'], item['city'], item['district'], item['name'], item['province_city'], \
               item['dizh'], item['jingwd']
            writer.writerow(rows)
        return item

class kuaidiw_timePipeline(object):
    def process_item(self, item, spider):
        with open('kuaidiw_time.csv', 'a', newline='') as csvou:
            writer = csv.writer(csvou, dialect='excel')
            rows = item['name'], item['exname'], item['logo'], item['placefrom'], item['placeto'], \
               item['time']
            writer.writerow(rows)
        return item

class kuaidiw_pricePipeline(object):
    def process_item(self, item, spider):
        with open('kuaidiw_price.csv', 'a', newline='') as csvou:
            writer = csv.writer(csvou, dialect='excel')
            rows = item['name'], item['price'], item['weight'], item['exname'], item['logo'], \
               item['placefrom'], \
               item['placeto'], item['wastetime']
            writer.writerow(rows)
        return item        