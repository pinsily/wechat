from unittest import TestCase

from utils.xml_utils import xml_to_dict


class Test(TestCase):
    def test_xml_to_dict(self):
        xml_str = """
        <xml>
          <ToUserName><![CDATA[toUser]]></ToUserName>
          <FromUserName><![CDATA[fromUser]]></FromUserName>
          <CreateTime>1348831860</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[this is a test]]></Content>
          <MsgId>1234567890123456</MsgId>
        </xml>
        """
        xml_dict = xml_to_dict(xml_str)
        assert xml_dict.get("to_user_name") == "toUser"
