from datetime import datetime

from sqlalchemy import Column, Integer, String, DATETIME, BIGINT
from sqlalchemy.orm import Session

from wechat.database import Base


class Service(Base):

    __tablename__ = "t_service"

    service_id = Column(BIGINT, primary_key=True, autoincrement=True, index=True, comment="自增索引")
    app_name = Column(String(64), default="", nullable=False, comment="主体名称")
    app_type = Column(Integer, default=0, nullable=False, comment="类型 1-服务号 2-小程序 3-APP")
    app_id = Column(String(64), default="", nullable=False, comment="主体appid")
    app_sec = Column(String(64), default="", nullable=False, comment="主体秘钥DES加密串")
    origin_id = Column(String(64), default="", nullable=False, comment="微信originId")
    apr_status = Column(Integer, default=0, nullable=False, comment="审批状态")
    extend_info = Column(String(4096), default="", nullable=False, comment="扩展信息")
    operator = Column(String(64), default="", nullable=False, comment="操作人")
    status = Column(Integer, default=0, nullable=False, comment="状态")
    create_time = Column(DATETIME, default=datetime.now, nullable=False, comment="创建时间")
    modify_time = Column(DATETIME, default=datetime.now, onupdate=datetime.now, nullable=False, comment="修改时间")
    version = Column(Integer, default=0, nullable=False, comment="版本号")

    @classmethod
    def add(cls, db: Session, data):
        db.add(data)
        db.commit()

    @classmethod
    def query_by_service_id(cls, db: Session, service_id: int):
        return db.query(cls).filter_by(service_id=service_id).first()

    @classmethod
    def query_by_app_id(cls, db: Session, app_id: str):
        return db.query(cls).filter_by(app_id=app_id).first()

    @classmethod
    def query_by_origin_id(cls, db: Session, origin_id: str):
        return db.query(cls).filter_by(origin_id=origin_id).first()

    def __repr__(self):
        return f"Service(service_id={self.service_id}, app_name=>{self.app_name}, app_id={self.app_id}, origin_id=>{self.origin_id})"

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    pass