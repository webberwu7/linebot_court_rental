from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ButtonsTemplate,
    TemplateSendMessage, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,
    CarouselTemplate, CarouselColumn
)


class View():
    def show(self):
        pass


class TextView(View):
    def __init__(self, inputStr):
        self.inputStr = str(inputStr)

    def show(self):
        return TextSendMessage(text=self.inputStr)


class HelperView(View):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="help order carousel template message",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
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
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='報修',
                                text='maintain'
                            ),
                            MessageTemplateAction(
                                label='佈告欄',
                                text='bulletin'
                            ),
                            MessageTemplateAction(
                                label='幫助',
                                text='help'
                            )
                        ]
                    ),
                ]
            )
        )


class ButtonDataView(View):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="button data template message",
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
