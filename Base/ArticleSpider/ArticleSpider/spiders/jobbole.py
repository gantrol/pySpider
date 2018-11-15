# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib.parse import urljoin
from ArticleSpider.items import JobboleItem

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
            item['img_url'] = post.xpath('.//img/@src').extract()
            request = Request(url=urljoin(response.url, item['url']), callback=self.parse_detail)
            request.meta['item'] = item
            yield request

        # next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first("")
        # if next_url:
        #     yield Request(url=urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        title = response.xpath('//h1/text()').extract_first()
        tt = response.xpath('//p[@class="entry-meta-hide-on-mobile"]')  # 存储time_create、tab的一行。
        time_create = tt.xpath('text()').extract_first().split()[0]  # Maybe if
        tag_list = tt.xpath('a/text()').extract()  # 标签列表
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        content = response.xpath('//div[@class="entry"]').extract_first()
        fmc = response.xpath('//div[@class="post-adds"]')  # 存储favor, mark, comment的一行。
        favor = fmc.xpath('span[contains(@class, "vote-post-up")]/h10/text()').extract_first()
        mark0 = fmc.xpath('span[contains(@class, "bookmark-btn")]/text()').extract_first()  # !!去掉收藏字样！！
        mark = re.match(r".*?(\d+).*?", mark0)
        if mark:
            mark = mark.group(1)
        else:
            mark = 0
        comment0 = fmc.xpath('a[@href="#article-comment"]//text()').extract_first()
        comment = re.match(r".*?(\d+).*?", comment0)
        if comment:
            comment = comment.group(1)
        else:
            comment = 0

        item = response.meta['item']
        item["title"] = title
        item["time_create"] = time_create
        item["tags"] = tags
        item["mark"] = mark
        item["comment"] = comment
        item["favor"] = favor
        item["content"] = content
        yield item
