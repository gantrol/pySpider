# 爬取github仓库的提交、分支、版本

## 相关技术

- python与mysql
- scrapy

## 准备

### 环境

- Python3.6
- scrapy1.5
- mysql5.6
- sqlalchemy
- mysqlclient

### mysql配置：编码、新建数据库

要先解决mysql的编码问题，然后新建数据库

## 初建项目

进入到 `/home/shiyanlou/Code` 目录，使用 `scrapy` 提供的 `startproject` 命令创建一个 `scrapy` 项目 ，再进入这个目录，创建爬虫

```
cd /home/shiyanlou/Code
scrapy startproject shiyanlou
cd shiyanlou
scrapy genspider Sylgit github.com/shiyanlou?tab=repositories
```



```shell
# 真实环境应该不用输入下面两个命令
pip3 install sqlalchemy
sudo apt-get install libmysqlclient-dev
# 一定要安装，避免后面出现的No module named 'MySQLdb';如果在虚拟环境中，不需要sudo
sudo pip3 install mysqlclient
```

### 创建表models.py

创建这个文件并写完代码后，再命令行输入下面一行命令来创建表

```shell
$ python3 models.py
```



```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime


engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')
Base = declarative_base()


class repositories(Base):
    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    update_time = Column(DateTime)
    commits = Column(Integer)
    branches = Column(Integer)
    releases = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
```


## 配置其他文档

### Items.py

```python
class SylgitItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()
    commits = scrapy.Field()
    branches = scrapy.Field()
    releases = scrapy.Field()
```


### settings.py

改两部分

```python
ROBOTSTXT_OBEY = False
```



```python
ITEM_PIPELINES = {
   'shiyanlou.pipelines.ShiyanlouPipeline': 300,
}
```

### pipelines.py

```python
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import repositories, engine
# from shiyanlou.items import SylgitItem


class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        """ 对不同的 item 使用不同的处理函数
        """
        # item['update_time'] = datetime.strptime(item['update_time'], '%b %d, %Y').date()
        # self.session.add(repositories(**item))
        self._process_github_item(item)
        return item

    def _process_github_item(self, item):
        item['update_time'] = datetime.strptime(item['update_time'], '%b %d, %Y').date()
        # item['learn_courses_num'] = int(item['learn_courses_num'])
        # adds to session
        self.session.add(repositories(**item))

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

```



### Spider/Sylgit.py

```python
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

```

## 运行

```shell
scrapy crawl shiyanlou-github
```