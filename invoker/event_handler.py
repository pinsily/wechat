from typing import Dict


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
        return "success"

    def video_handler(self):
        """
        视频处理器
        :return:
        """
        return "success"
