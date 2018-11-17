# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobboleItem(scrapy.Item):
    title = scrapy.Field()
    time_create = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()  ## 需要md5
    img_url = scrapy.Field()
    img_path = scrapy.Field()
    tags = scrapy.Field()
    mark = scrapy.Field()
    comment = scrapy.Field()
    favor = scrapy.Field()
    content = scrapy.Field()
