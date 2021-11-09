from invoker.event_handler import Event
from settings import logger


class TestEvent:

    def test_text_handler(self):
        """
        文本消息处理器
        :return:
        """
        event_data = {'to_user_name': 'toUser', 'from_user_name': 'fromUser', 'create_time': '1348831860',
                      'msg_type': 'text', 'content': 'this is a test', 'msg_id': '1234567890123456'}

        event = Event(event_data)
        result = event.dispatch()
        logger.info(f"text handler result=>{result}")
        assert result == event_data.get("content")

    def test_video_handler(self):
        event_data = {'to_user_name': 'toUser', 'from_user_name': 'fromUser', 'create_time': '1348831860',
                      'msg_type': 'video', 'content': 'this is a test', 'msg_id': '1234567890123456'}

        event = Event(event_data)
        result = event.dispatch()
        logger.info(f"video handler result=>{result}")
        assert result == "success"

    def test_subscribe_event_handler(self):
        event_data = {'to_user_name': 'toUser', 'from_user_name': 'fromUser', 'create_time': '1348831860',
                      'msg_type': 'event', 'event': 'subscribe', 'event_key': 'qrscene_123123'}
        event = Event(event_data)
        result = event.dispatch()
        logger.info(f"subscribe handler result=>{result}")
        assert result == "subscribe"