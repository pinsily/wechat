from sqlalchemy import MetaData

from wechat.database import engine
from wechat.models import Service

if __name__ == '__main__':
    meta = MetaData(bind=engine, schema=Service)
    meta.create_all()