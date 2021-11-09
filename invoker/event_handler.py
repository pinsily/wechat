from typing import Dict

from settings import logger


class Event:
    """
    事件处理
    """

    def __init__(self, event_data: Dict, **kwargs):
        """

        :param kwargs:
        """
        self.event_data = event_data
        # 其他入参置为类的属性
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dispatch(self):
        """
        路由分发, 定向到不同的事件处理函数
        :return:
        """
        handler = getattr(self, self.event_data.get("msg_type") + "_handler", None)
        if not handler:
            raise AttributeError(f"路由处理方法不存在, msg_type=>{self.event_data.get('msg_type')}")

        return handler()

    def text_handler(self):
        """
        文本消息处理
        :return:
        """
        return self.event_data.get("content")

    def video_handler(self):
        """
        视频处理器
        :return:
        """
        return "success"

    def event_handler(self):
        """
        事件接受需要进一步分路由
        :return:
        """
        event = getattr(self, self.event_data.get("event") + "_event_handler", None)
        if not event:
            raise AttributeError(f"事件类型不存在, event=>{self.event_data.get('event')}")

        return event()

    def subscribe_event_handler(self):
        """
        用户关注事件
        :return:
        """
        # 扫码事件
        if self.event_data.get("event_key"):
            logger.info(f"扫码事件， event_key=>{self.event_data.get('event_key')}")
        return "subscribe"
