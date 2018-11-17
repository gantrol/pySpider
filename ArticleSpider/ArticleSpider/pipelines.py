# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
import MySQLdb.cursors
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class AritcleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        def item_completed(self, results, item, info):
            try:
                for ok, value in results:
                    img_path = value["path"]
                item["img_path"] = img_path
            except TypeError:
                print("'Failure' object is not subscriptable")
            finally:
                return item

    def get_media_requests(self, item, info):
        yield Request(item['img_url'])  # , headers=self.headers)


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


class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异常

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = """
            insert into jobbolespider(title, url, url_object_id, create_date, favor) VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_sql,
                       (item["title"], item["url"], item["url_object_id"], item["time_create"], item["favor"]))
