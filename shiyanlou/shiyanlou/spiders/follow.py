# -*- coding: utf-8 -*-
import scrapy


class FollowSpider(scrapy.Spider):
    name = 'follow'
    allowed_domains = ['www.shiyanlou.com/courses/']
    start_urls = ['http://www.shiyanlou.com/courses/63']

    def parse(self, response):
        yield{
            'name': response.xpath("//h4[@class='course-infobox-title']/span/text()").extract_first(),
            'author': response.xpath("//div[@class='name']/strong/text()").extract_first()
        }
        for url in response.xpath("//div[@class='sidebox-body course-content']/a/@href"):
            yield response.follow(url, callback=self.parse)
