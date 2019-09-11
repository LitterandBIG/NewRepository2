from sqlalchemy import (
    create_engine,
    Integer,
    String,
    Column,
    Enum,
    Float,
    Boolean,
    DECIMAL,
    DateTime,
    Date,
    Time
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
import enum

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'second_sql'
USERNAME = 'root'
PASSWORD = 'abc80231124'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)
Base = declarative_base(engine)

session = sessionmaker(engine)()


class TagNum(enum.Enum):
    python = 'python'
    linux = 'linux'
    mysql = 'mysql'


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    is_delete = Column(Boolean)
    prices = Column(DECIMAL(10, 4))
    tag = Column(Enum(TagNum))
    create_time = Column(DateTime)
    content = Column(LONGTEXT)


Base.metadata.create_all()

article = Article(prices=10000.999)
session.add(article)
session.commit()
