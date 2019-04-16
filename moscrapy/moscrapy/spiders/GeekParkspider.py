# -*- encoding: utf-8 -*-


from moscrapy.items import GeekParkItem
import scrapy
import json


class GeekParkspider(scrapy.Spider):
    name = "geekpark"
    allowed_domains = ["mainssl.geekpark.net"]

    def start_requests(self):
        for i in range(1, 100):
            url = "https://mainssl.geekpark.net/api/v2?page={}".format(i)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = GeekParkItem()
        i = 1
        begin = True
        groups = json.loads(response.text)
        one_group = groups['homepage_posts'][i]['post']

        print(one_group)
        while begin:
            data = groups['homepage_posts'][i]['post']
            #print(data)
            for authors in data["authors"]:
                item['author'] = authors['nickname']
            item['link']      = "http://www.geekpark.net/news/{}".format(data['id'])
            item['title']     = data['title']
            item['abstract']  = data['abstract']
            item['published'] = data['published_at']
            item['tag']       = "科技新闻"
            if i == 19:
                begin = False
            i = i + 1
            yield item
