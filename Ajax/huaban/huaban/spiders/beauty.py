# -*- coding: utf-8 -*-
import json
import scrapy
from urllib.parse import urlencode


class BeautySpider(scrapy.Spider):
    name = 'beauty'
    params = {
        'max': 2108834067,
        'limit': 20,
        'wfl': 1
    }
    url = 'http://huaban.com/favorite/beauty?jo9yikt6&' + urlencode(params)
    # print(url)
    start_urls = [url, ]

    def parse(self, response):
        json0 = json.loads(response.text)
        pins = json0.get('pins')
        # print(pins)
        if pins:
            for pin in pins:
                yield{
                    'image': 'http://img.hb.aicdn.com/' + pin.get('file').get('key'),
                    'title': pin.get('board').get('title')
                }

        self.params['max'] = pins[-1].get('pin_id')
        next_page = 'http://huaban.com/favorite/beauty?jo9yikt6&' + urlencode(self.params)
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)