from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:pinsily96@localhost:3306/wechat_db"

# connect_args={"check_same_thread": False} 只用在SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 实际的数据库链接
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据库ORM基类
Base = declarative_base()
