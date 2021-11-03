from utils.str_utils import hump2underline


def test_hump2underline():
    """
    驼峰转下划线测试方法
    :return:
    """
    assert hump2underline("FromUserName") == "from_user_name"
    assert hump2underline("Content") == "content"
    assert hump2underline("toUser") == "to_user"
