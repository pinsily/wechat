from settings import pre_settings
from wx_api.wx_api import WxApi


def test_access_token():
    """
    测试获取token
    :return:
    """
    wx_api = WxApi(pre_settings.test_appid, pre_settings.test_appsec)
    token = wx_api.get_access_token()

    assert token is not None


