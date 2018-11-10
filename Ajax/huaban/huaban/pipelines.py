# -*- coding: utf-8 -*-
import requests
import os
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from hashlib import md5
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HuabanPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        # print(item['image'])
        path = '.images/beauty/'
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            image_url = item.get('image')
            response = requests.get(image_url)
            if response.status_code == 200:
                file_path = path + '{0}.{1}'.format(item.get('title') + md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print('Downloaded image path is %s' % file_path)
                else:
                    print('Already Downloaded', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image，item %s' % item)



