# -*- coding: utf-8 -*-
# import requests
# import os
from scrapy import Request
# from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
# from hashlib import md5
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HuabanPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagePipeline(ImagesPipeline):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':  'gzip, deflate',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection':  'keep-alive',
        'Host': 'img.hb.aicdn.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Upgrade-Insecure-Requests: ': 1,
        'Cookie':'_uab_collina=153572835042485686577819; __auc=1347e9a0165908af7a381f97a1d; __gads=ID=33e8c3248d63a6b2:T=1535728349:S=ALNI_MYuKpeTylFniJoQYMOFGPKElTIUOw; UM_distinctid=165928d4c649ca-046ed74c237be7-9393265-144000-165928d4c66119; CNZZDATA1256914954=1691845574-1536568949-null%7C1536568949; sid=K6dSvfe91zRqyV2iy5tar6qkG8X.4lv%2FrHOY6dyww6%2FtSCQqhVCB1h8SsHBeaVEulp%2FiX38; _hmt=1; uid=19470664; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAAC00lEQVRYR%2BWWT0hUURSHv6MTUZs2swgiZhH2RxdROEYUOBUYlhQRSAxEUUwhUbNIUFq4cFEKBg4RhkNRCbOQIgLDiEiFXDiK1CKMosUsQ5EMskU2J%2B6b%2B4ZxbMYpxsp8m7nz7n33nu%2F8fue8J6gq%2BS4RyTv%2FhyY7pzvzxikGZO3sLNFQiGAsRiwYJBSN0tLaSlN7uwlzBKgTmMoXs4IX6AO6Be4Um68gEHOod2qKSDhMOBJhyuvFwHU0NtLQ1VUuMFFIYApnzLp%2FFgQ4BQSA08BdYFCgWaENaAJiQAg4AVQCh4Bhe88H9APm96DdawZYB2wqRG2TnF9SpK%2Bujl0jxkmpK%2BHz4UskyoFJIAKEgQqgFrgHXARagFbgBrAbOGABzP13wGYLYrY0zxko86wZHwMeFaL4L4HkstbPQKwibl2st4EZEMdaCtUm43ZsLHcbMEVnQGozFO0XGFrMusUCSdjMdwBHbJZNVs3%2FBqA5QxEXxNjOCdoq8yFDkaUBKaRrAY22Hp4C24ALwE2byY%2FAgLVYFAgCZ60abh3FAQ9QCmy36pj6KqgrFqxITmmX03vkv3khrlgQfRmv4Js8QfChJFilh%2FlesoGk9jpJKZF6qa58Zobz1%2Bp12Vdlai196UC8A5HL7j6yt%2BqNO6lDYzV2z089W8d906u%2F5q6A3%2F3WcgKckweI3pLqKvOOQQfHLiG8dSFS90YfO6d79Apz0oNIcxoyFWg3JXKOZLIGkTIJ%2BI%2FOAzVrVNt6tozvWBKQzCDdw3Uw3oKHh%2FOyOjg6jGivgXWgVN%2B7quhQPIxKvQT8e5zsq7bh0ZMLVFlykIzDHWupHpeA%2F3zaGlmqLQBJ2Wq%2FBPw7%2FyqIVWUc1RcInxFmXJulYZaDIg6IzSroBB6uZtpi2dRIVld6nV2oubqWbQAbHUtlda1U90vep4RrlPLc7Y6Ta74QK3tV%2FK612EdesedXzCfKD1HkETenQIVMAAAAAElFTkSuQmCC%2CWin32.1536.864.24; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1539492274,1540619161,1541761884; _trs_uv=joa0x5cb_1245_8a52; Hm_lvt_e9fe99c2267a6f7a9215a8724ce995b4=1541768102; Hm_lpvt_e9fe99c2267a6f7a9215a8724ce995b4=1541768102; _ga=GA1.2.2132483355.1541768102; _gid=GA1.2.587293805.1541768102; md_href=http%3A%2F%2Fhuaban.com%2Fboards%2F18398025%3Fmd%3Dnewbn%26beauty%3D; md=newbn; CNZZDATA1256903590=1150130295-1535761091-%7C1541773377; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1541775234069%26urlname%7Ck5spfh6f1d%7C1541775234070%26md%7Cnewbn%7C1541775235070; __asc=d64e2570166f93977f10a32fa22; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1541779640',

    }

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1] + '.jpg'
        return file_name

    # def item_completed(self, results, item, info):
    #     if isinstance(item, dict) or self.images_result_field in item.fields:
    #         item[self.images_result_field] = [x for ok, x in results if ok]
    #     return item

    def get_media_requests(self, item, info):
        yield Request(item['image'], headers=self.headers)

#     def get_media_requests(self, item, info):
#         # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
#             # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
#         # print(item['image'])
#         path = '.images/beauty/'
#         if not os.path.exists(path):
#             os.makedirs(path)
#         try:
#             image_url = item.get('image')
#             response = requests.get(image_url)
#             if response.status_code == 200:
#                 file_path = path + '{0}.{1}'.format(item.get('title') + md5(response.content).hexdigest(), 'jpg')
#                 if not os.path.exists(file_path):
#                     with open(file_path, 'wb') as f:
#                         f.write(response.content)
#                     print('Downloaded image path is %s' % file_path)
#                 else:
#                     print('Already Downloaded', file_path)
#         except requests.ConnectionError:
#             print('Failed to Save Image，item %s' % item)



