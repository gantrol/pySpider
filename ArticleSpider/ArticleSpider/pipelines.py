# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class AritcleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            img_path = value["path"]
        item["img_path"] = img_path
        # if isinstance(item, dict) or self.images_result_field in item.fields:
        #     item[self.images_result_field] = [x for ok, x in results if ok]
        return item


class AritcleJsonItemExporter(object):
    """调用scrapy的json exporter导出json文件"""
    def __init__(self):
        self.file = open('articleExport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleJsonPipeline(object):
    # def __init__(self):
    #     self.file = codecs.open('aricle.json', 'w', encoding='utf-8')
    def open_spider(self, spider):
        # self.file = open('items.json', 'w')
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 不False会出错？
        self.file.write(line)
        return item  # 必须返回，可能有其他pipeline会调用


class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '123456', 'articlespiders', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbolespider(title, url, url_object_id, create_date, favor) VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql,
                            (item["title"], item["url"], item["url_object_id"], item["time_create"], item["favor"]))
        self.conn.commit()
