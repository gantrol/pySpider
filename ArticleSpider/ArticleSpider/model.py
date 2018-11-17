from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, VARCHAR, LONGTEXT


engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/articlespiders?charset=utf8')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'jobboleSpider'
    title = Column(VARCHAR(200), nullable=False)
    create_date = Column(DATETIME)
    url = Column(VARCHAR(300), nullable=False)
    url_object_id = Column(VARCHAR(50), primary_key=True, nullable=False)
    img_url = Column(VARCHAR(300))
    img_path = Column(VARCHAR(300))
    tags = Column(VARCHAR(100))
    mark = Column(INTEGER(11), default=0)
    comment = Column(INTEGER(11), default=0)
    favor = Column(INTEGER(11), default=0)
    content = Column(LONGTEXT)

if __name__ == '__main__':
    Base.metadata.create_all(engine)