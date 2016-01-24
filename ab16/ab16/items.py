# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pid = scrapy.Field()
    title = scrapy.Field()
    details = scrapy.Field()
    authors = scrapy.Field()
    url = scrapy.Field()

class SessionItem(scrapy.Item):
    salloon = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    topic = scrapy.Field()
    ids = scrapy.Field()
