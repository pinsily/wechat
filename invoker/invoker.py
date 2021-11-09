import hashlib

from utils.xml_utils import xml_to_dict

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

from settings import logger, pre_settings

invoker = APIRouter()


@invoker.get(
    "/verify/"
)
async def check_signature(
        request: Request,
        signature: str,
        timestamp: str,
        nonce: str,
        echostr: str,
):
    """
    接入指南：https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html

    signature 微信加密签名，signature结合了开发者填写的token参数和请求中的timestamp参数、nonce参数。
    timestamp 时间戳
    nonce 随机数
    echostr 随机字符串

    开发者通过检验signature对请求进行校验（下面有校验方式）。
    若确认此次GET请求来自微信服务器，请原样返回echostr参数内容，则接入生效，成为开发者成功，否则接入失败。
    加密/校验流程如下：
        1）将token、timestamp、nonce三个参数进行字典序排序
        2）将三个参数字符串拼接成一个字符串进行sha1加密
        3）开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    """
    logger.info(f"signature: {signature}")
    logger.info(f"timestamp: {timestamp}")
    logger.info(f"nonce: {nonce}")
    logger.info(f"echostr: {echostr}")

    _ = "".join(sorted([pre_settings.api_token, timestamp, nonce]))
    sign = hashlib.sha1(_.encode('UTF-8')).hexdigest()
    return HTMLResponse(content=echostr if sign == signature else "error")


@invoker.post(
    "/event_handler/"
)
async def event_handler(
        request: Request,
        xml_param: str
):
    logger.info("receive wechat request=>{}")
    # xml转dict
    event_data = xml_to_dict(xml_param)


    pass


if __name__ == '__main__':
    pass