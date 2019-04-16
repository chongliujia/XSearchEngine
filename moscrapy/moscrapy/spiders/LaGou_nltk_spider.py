# -*- coding: utf-8 -*-


import scrapy
from moscrapy.items import LaGouItem

class LaGouspider_nltk(scrapy.Spider):
    name = 'lagou_nltk'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/ziranyuyanchuli/?labelWords=label']

    def parse(self, response):
        groups = response.xpath('//*[@id="s_position_list"]/ul/li')
        for group in groups:
            item = LaGouItem()
            item['position'] = group.xpath('div[1]/div[1]/div[1]/a/h3/text()').extract_first()
            item['salary']   = group.xpath('div[1]/div[1]/div[2]/div/span/text()').extract_first()
            item['demand']   = group.xpath('div[1]/div[1]/div[2]/div/text()').extract()[2].strip()
            item['address']  = group.xpath('div[1]/div[1]/div[1]/a/span/em/text()').extract_first()
            item['company_name'] = group.xpath('div[1]/div[2]/div[1]/a/text()').extract_first()
            item['company_industry'] = group.xpath('div[1]/div[2]/div[2]/text()').extract_first().strip()
            item['corporate_welfare'] = group.xpath('div[2]/div[2]/text()').extract_first()
            print(item['position'], item['salary'], item['demand'], item['address'], item['company_name'],
            item['company_industry'], item['corporate_welfare'])
            yield item
        next_page = response.xpath('//*[@id="s_position_list"]/div[2]/div/a[6]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
