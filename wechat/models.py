from sqlalchemy import Boolean, Column, Integer, String, DATETIME, BIGINT, VARCHAR

from .database import Base


class Service(Base):

    __tablename__ = "t_service"

    windex = Column(BIGINT, primary_key=True, autoincrement=True, index=True, comment="自增索引")
    wapp_name = Column(String(64), default="", nullable=False, comment="主体名称")
    wapp_type = Column(Integer, default=0, nullable=False, comment="类型 1-服务号 2-小程序 3-APP")
    wapp_id = Column(String(64), default="", nullable=False, comment="主体appid")
    wapp_sec = Column(String(64), default="", nullable=False, comment="主体秘钥DES加密串")
    worigin_id = Column(String(64), default="", nullable=False, comment="微信originId")
    wapr_status = Column(Integer, default=0, nullable=False, comment="审批状态")
    wextend_info = Column(String(4096), default="", nullable=False, comment="扩展信息")
    woperator = Column(String(64), default="", nullable=False, comment="操作人")


