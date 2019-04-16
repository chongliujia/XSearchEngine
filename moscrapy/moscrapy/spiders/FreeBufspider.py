# -*- coding: utf-8 -*-


import re
import scrapy
from moscrapy.items import FreeBufItem



class FreeBufspider(scrapy.Spider):
    name = 'FreeBuf'
    allowed_domains = ['www.freebuf.com']
    start_urls = []
    for i in range(1, 300):
        start_urls.append("https://www.freebuf.com/page/{}".format(i))


    def parse(self, response):
        groups = response.xpath('//*[@id="timeline"]/div[1]/div[2]')
        for group in groups:
            item = FreeBufItem()
            item['title'] = group.xpath('dl/dt/a/text()').extract_first().strip()
            item['abstract'] = group.xpath('dl/dd[2]/text()').extract_first().strip()
            item['published'] = group.xpath('dl/dd[1]/span[3]/text()').extract_first().strip()
            item['tag']       = group.xpath('div/span[1]/a/text()').extract_first()
            item['link']      = group.xpath('dl/dt/a/@href').extract_first()
            item['author']    = group.xpath('dl/dd[1]/span[1]/a/text()').extract_first()
            print(item['title'], item['abstract'], item['tag'], item['published'], item['link'])
            yield item

"""
    def parse(self, response):
        groups = response.xpath('//*[@id="timeline"]/div[1]/div[2]')
        for group in groups:
            item = FreeBufItem()
            item['link']      = group.xpath('dl/dt/a/@href').extract_first()
            url = response.urljoin(item['link'])
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        item = FreeBufItem()
        item['title']     = response.xpath('//*[@id="getWidth"]/div[2]/div/div[1]/h2/text()').extract_first()
        item['author']    = response.xpath('//*[@id="getWidth"]/div[2]/div/div[1]/div/span[1]/a/text()').extract_first().strip()
        item['published'] = response.xpath('//*[@id="getWidth"]/div[2]/div/div[1]/div/span[3]/text()').extract_first().strip()
        item['abstract']  = response.xpath('//*[@id="contenttxt"]/p[2]/b/text()').extract_first()

        paper_list = response.xpath('//div[@id="contenttxt"]').extract()
        paper_string = ''.join(paper_list)
        text = re.sub('<[^<]+?>', '', paper_string).replace('\n', '').strip()
        item['text'] = text
        yield item
"""
