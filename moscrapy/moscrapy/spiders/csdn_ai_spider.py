# -*- coding: utf-8 -*-

import scrapy
import time

from selenium import webdriver
from moscrapy.items import CSDNItem

class CSDN_AI_Spider(scrapy.Spider):
    name = 'csdnai'
    allowed_domains = ['www.csdn.net']
    start_url = ['https://www.csdn.net/nav/ai']

    def parse(self, response):
        groups = response.xpath('//*[@id="feedlist_id"]/li/div')
        for group in groups:
            item = BoleItem()
            item['title'] = group.xpath('div[1]/h2/a/text()').extract_first().strip()
            item['author'] = group.xpath('dl/dd[1]/a/text()').extract_first().strip()
            item['published'] = group.xpath('dl/dd[2]/text()').extract_first().strip()
            item['pageview'] = group.xpath('dl/div[2]/dd[1]/a/span[2]/text()').extract_first()
            item['abstract'] = group.xpath('div[2]/text()').extract_first().strip()
            item['link'] = group.xpath('div[1]/h2/a/@href').extract_first()
            print(item['title'], item['abstract'], item['tag'], item['published'], item['link'])
            yield item
