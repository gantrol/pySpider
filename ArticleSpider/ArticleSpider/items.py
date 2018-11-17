# -*- coding: utf-8 -*-

import re
import scrapy
from datetime import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def datetime_type(value):
    try:
        time_create = datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        time_create = datetime.now().date()
    finally:
        return time_create


def get_nums(value):
    match = re.match(r".*?(\d+).*?", value)
    if match:
        return int(match.group(1))
    return 0


def remove_comment_tags(value):
    if "评论" in value:
        return ""
    return value


class TakeFirstItem(ItemLoader):
    # 自定义itemLoader
    default_output_processor = TakeFirst()


class JobboleItem(scrapy.Item):
    title = scrapy.Field()
    time_create = scrapy.Field(
        input_processor=MapCompose(datetime_type),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()  ## 需要md5
    img_url = scrapy.Field()  # list还是不是list？
    img_path = scrapy.Field()
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(","),
    )
    mark = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    comment = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
    )
    favor = scrapy.Field()
    content = scrapy.Field()



