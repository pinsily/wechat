import json

import requests

import logging
from typing import Dict

from settings import pre_settings

logging.basicConfig(level=logging.INFO)


class WxApi:

    def __init__(self, appid: str, appsec: str):
        self.appid = appid
        self.appsec = appsec
        self.headers = {
            "content-type": "application/json"
        }

    def get_access_token(self) -> str:
        """
        获取access token
        :return:
        """

        # todo 增加缓存

        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.appid}&secret={self.appsec}"

        response = requests.get(url, headers=self.headers)

        result = json.loads(response.text)

        if result.get("errcode"):
            # todo 学习自定义异常
            raise Exception(f"errcode=>{result.get('errcode')}, errmsg=>{result.get('errmsg')}")

        return result.get("access_token")

    def get_userinfo(self, openid: str) -> Dict:
        """
        获取用户基本信息
        :param openid:
        :return:
        """
        token = self.get_access_token()
        if not token:
            logging.error("获取token失败")
            return dict()

        url = f"https://api.weixin.qq.com/cgi-bin/user/info?access_token={token}&openid={openid}&lang=zh_CN"
        response = requests.get(url, headers=self.headers)
        logging.info(response.text)
        result = json.loads(response.text)
        logging.info(result)
        return dict(result)


if __name__ == '__main__':
    wx_api = WxApi(pre_settings.test_appid, pre_settings.test_appsec)
    # token = wx_api.get_access_token()
    userinfo = wx_api.get_userinfo(pre_settings.test_openid)
