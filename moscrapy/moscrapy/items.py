# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from moscrapy.models.es_types import ArticleType


class GeekParkItem(scrapy.Item):
    title     = scrapy.Field()
    abstract  = scrapy.Field()
    author    = scrapy.Field()
    published = scrapy.Field()
    link        = scrapy.Field()
    tag       = scrapy.Field()


class FreeBufItem(scrapy.Item):
    title     = scrapy.Field()
    author    = scrapy.Field()
    published = scrapy.Field()
    abstract  = scrapy.Field()
    tag       = scrapy.Field()
    link      = scrapy.Field()


class LaGouItem(scrapy.Item):
    position  = scrapy.Field()
    salary    = scrapy.Field()
    demand    = scrapy.Field()
    company_name      = scrapy.Field()
    company_industry  = scrapy.Field()
    corporate_welfare = scrapy.Field()
    address   = scrapy.Field()

class BoleItem(scrapy.Item):
    title     = scrapy.Field()
    published = scrapy.Field()
    abstract  = scrapy.Field()
    tag   = scrapy.Field()
    link      = scrapy.Field()

class CSDNItem(scrapy.Item):
    title     = scrapy.Field()
    published = scrapy.Field()
    author    = scrapy.Field()
    abstract  = scrapy.Field()
    pageview  = scrapy.Field()
    article_type = scrapy.Field()
    link      = scrapy.Field()
