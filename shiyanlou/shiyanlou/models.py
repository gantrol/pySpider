from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime


engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()


class repositories(Base):
    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    update_time = Column(DateTime)
    commits = Column(Integer)
    branches = Column(Integer)
    releases = Column(Integer)
# class Course(Base):
#     __tablename__ = 'courses'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), index=True)
#     description = Column(String(1024))
#     type = Column(String(64), index=True)
#     students = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)