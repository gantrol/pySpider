# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SylgitItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()
    commits = scrapy.Field()
    branches = scrapy.Field()
    releases = scrapy.Field()


class MovieItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    summary = scrapy.Field()
    score = scrapy.Field()

class CourseItem(scrapy.Item):
    """定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取
  的数据声明为 scrapy.Field()。下面的代码是我们每个课程要爬取的 4个数据。
  """
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()