from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ButtonsTemplate,
    TemplateSendMessage, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)


class View():
    def show(self):
        pass


class TextView(View):
    def __init__(self, inputStr):
        self.inputStr = str(inputStr)

    def show(self):
        return TextSendMessage(text=self.inputStr)


class ButtonMessageView(View):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="button message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                image_aspect_ratio='square',
                image_size='contain',
                thumbnail_image_url="https://imgur.com/a/jnYeRXG",
                actions=[
                    MessageTemplateAction(
                        label='帳號',
                        text='account'
                    ),
                    MessageTemplateAction(
                        label='搜尋',
                        text='search'
                    ),
                    MessageTemplateAction(
                        label='預約',
                        text='booking'
                    )
                ]
            )
        )


class ButtonDataView(View):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="template message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='action=buy&itemid=1'
                    )
                ]
            )
        )

class ButtonUrlView(View):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="template message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    URITemplateAction(
                        label='uri',
                        uri='http://140.122.185.90/AdvCG/'
                    )
                ]
            )
        )