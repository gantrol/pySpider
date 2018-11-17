# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib.parse import urljoin
from ..items import JobboleItem, TakeFirstItem
from ..utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    ## http://blog.jobbole.com/all-posts/
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        posts = response.xpath('//div[@class="post floated-thumb"]')

        for post in posts:
            item = JobboleItem()
            item['url'] = post.xpath('.//a[@class="archive-title"]/@href').extract_first()
            item['img_url'] = post.xpath('.//img/@src').extract_first()
            request = Request(url=urljoin(response.url, item['url']), callback=self.parse_detail)
            request.meta['item'] = item
            yield request

        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first("")
        if next_url:
            yield Request(url=urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        item_loader = TakeFirstItem(item=response.meta['item'], response=response)
        item_loader.add_xpath("title", '//h1/text()') # 相当于完成前面的操作
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_xpath("time_create", '//p[@class="entry-meta-hide-on-mobile"]/text()')
        item_loader.add_xpath("tags", '//p[@class="entry-meta-hide-on-mobile"]/a/text()')
        item_loader.add_xpath("mark", '//div[@class="post-adds"]/span[contains(@class, "bookmark-btn")]/text()')
        item_loader.add_xpath("comment", '//div[@class="post-adds"]/a[@href="#article-comment"]//text()')
        item_loader.add_xpath("favor", '//div[@class="post-adds"]/span[contains(@class, "vote-post-up")]/h10/text()')
        item_loader.add_xpath("content", '//div[@class="entry"]')
        article_item = item_loader.load_item()
        yield article_item
