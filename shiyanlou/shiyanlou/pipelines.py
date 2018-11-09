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
