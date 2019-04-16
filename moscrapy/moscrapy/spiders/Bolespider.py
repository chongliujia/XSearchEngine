# -*- coding: utf-8 -*-


import re
import scrapy
from moscrapy.items import BoleItem



class Bolespider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['blog.jobbole.com']
    #start_urls = ['http://blog.jobbole.com/all-posts/']
    start_urls = []
    for i in range(1, 550):
        start_urls.append("http://blog.jobbole.com/all-posts/page/{}/".format(i))


    def parse(self, response):
        groups = response.xpath('//*[@id="archive"]/div/div[2]')
        for group in groups:
            item = BoleItem()
            item['title'] = group.xpath('p[1]/a[1]/text()').extract_first()
            item['abstract'] = group.xpath('span/p/text()').extract_first().strip()
            item['published'] = group.xpath('p[1]/text()').extract()[1].strip()[:10]
            item['tag']       = group.xpath('p[1]/a[2]/text()').extract_first()
            item['link']      = group.xpath('p[2]/span/a/@href').extract_first()
            print(item['title'], item['abstract'], item['tag'], item['published'], item['link'])
            yield item
        """
        next_page = response.xpath('//*[@id="archive"]/div[21]/a[4]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        """
