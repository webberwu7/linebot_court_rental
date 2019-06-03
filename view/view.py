from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

class View():
    def show(self):
        pass


class TextView(View):
    def __init__(self, inputStr):
        self.inputStr = str(inputStr)

    def show(self):
        return TextSendMessage(text=self.inputStr)
