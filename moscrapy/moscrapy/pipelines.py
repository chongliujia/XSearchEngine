# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymongo
from scrapy.conf import settings
from moscrapy.models.es_types import ArticleType

class MoscrapyPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db     = self.client[settings['MONGO_DB']]
        self.coll   = self.db[settings['MONGO_COLL']]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.coll.insert(postItem)
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('FreeBuf.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "," + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()




class ElasticsearchPipeline(object):
    def process_item(self, item, spider):
        article = ArticleType()
        article.title = item['title']
        article.abstract = item['abstract']
        article.published = item['published']
        article.tag       = item['tag']
        article.link      = item['link']

        article.save()
        return item

"""
import psycopg2

class MoscrapyPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '314159'
        database = 'moscrapysdatabase'

        self.connection = psycopg2.connect(host=hostname, user=username, password=password,
        dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO FreeBuf(title, author, pagetext, published) VALUES(%s, %s, %s, %s)",(item['title'], item['author'], item['text'], item['published']))
            self.connection.commit()
            return item
        except:
            self.connection.rollback()
            print("already exists.")
"""
