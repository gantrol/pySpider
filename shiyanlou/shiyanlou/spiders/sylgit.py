# -*- coding:utf-8 -*-
import scrapy
from shiyanlou.items import SylgitItem


class SylgitSpider(scrapy.Spider):
    name = 'shiyanlou-github'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for repo in response.css('.public'):
            item = SylgitItem()
            item['name'] = repo.xpath('div/h3/a/text()').extract_first().strip()
            item['update_time'] = repo.xpath('div/relative-time/text()').extract_first()
            repo_url = 'https://github.com/shiyanlou/' + item['name']
            request = scrapy.Request(repo_url, callback=self.parse_repo)
            request.meta['item'] = item
            yield request
        next_page = response.xpath("//a[@rel='nofollow']").re('href="(.*?)">Next')[0]
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_repo(self, response):
        item = response.meta['item']
        numbers_summary = response.xpath('//ul[@class="numbers-summary"]/li/a/span/text()').extract()
        item['commits'] = numbers_summary[0].split()[0]
        item['branches'] = numbers_summary[1].split()[0]
        item['releases'] = numbers_summary[2].split()[0]
        yield item
