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


class AccountHelpView(View):
    def __init__(self, title='帳號系統', text='帳號頁面指令小幫手'):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="account help button message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    MessageTemplateAction(
                        label='line帳號綁定學號',
                        text='account/register'
                    ),
                    MessageTemplateAction(
                        label='帳號喜好',
                        text='account/hobby'
                    ),
                    MessageTemplateAction(
                        label='帳號喜好設定',
                        text='account/hobby/time'
                    )
                ]
            )
        )


class AccountHobbyTimeHelpView(View):
    def __init__(self, title='帳號喜好設定時間', text='請設定喜好時間', last_input=""):
        self.title = title
        self.text = text
        self.last_input = last_input

    def show(self):
        return TemplateSendMessage(
            alt_text="account help button message",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期一早上',
                                text=self.last_input+'/1'
                            ),
                            MessageTemplateAction(
                                label='星期一下午',
                                text=self.last_input+'/2'
                            ),
                            MessageTemplateAction(
                                label='星期一晚上',
                                text=self.last_input+'/3'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期二早上',
                                text=self.last_input+'/4'
                            ),
                            MessageTemplateAction(
                                label='星期二下午',
                                text=self.last_input+'/5'
                            ),
                            MessageTemplateAction(
                                label='星期二晚上',
                                text=self.last_input+'/6'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期三早上',
                                text=self.last_input+'/7'
                            ),
                            MessageTemplateAction(
                                label='星期三下午',
                                text=self.last_input+'/8'
                            ),
                            MessageTemplateAction(
                                label='星期三晚上',
                                text=self.last_input+'/9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期四早上',
                                text=self.last_input+'/10'
                            ),
                            MessageTemplateAction(
                                label='星期四下午',
                                text=self.last_input+'/11'
                            ),
                            MessageTemplateAction(
                                label='星期四晚上',
                                text=self.last_input+'/12'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期五早上',
                                text=self.last_input+'/13'
                            ),
                            MessageTemplateAction(
                                label='星期五下午',
                                text=self.last_input+'/14'
                            ),
                            MessageTemplateAction(
                                label='星期五晚上',
                                text=self.last_input+'/15'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期六早上',
                                text=self.last_input+'/16'
                            ),
                            MessageTemplateAction(
                                label='星期六下午',
                                text=self.last_input+'/17'
                            ),
                            MessageTemplateAction(
                                label='星期六晚上',
                                text=self.last_input+'/18'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期日早上',
                                text=self.last_input+'/19'
                            ),
                            MessageTemplateAction(
                                label='星期日下午',
                                text=self.last_input+'/20'
                            ),
                            MessageTemplateAction(
                                label='星期日晚上',
                                text=self.last_input+'/21'
                            )
                        ]
                    ),
                ]
            )
        )


class AccountHobbyCourtHelpView(View):
    def __init__(self, title='帳號喜好設定場地', text='請設定喜好場地', last_input=""):
        self.title = title
        self.text = text
        self.last_input = last_input

    def show(self):
        return TemplateSendMessage(
            alt_text="account help button message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    MessageTemplateAction(
                        label='籃球場',
                        text=self.last_input+'/court/1'
                    ),
                    MessageTemplateAction(
                        label='排球場',
                        text=self.last_input+'/court/2'
                    ),
                ]
            )
        )


class MaintainHelpView(View):
    def __init__(self, title='報修系統', text='請選擇要報修的球場'):
        self.title = title
        self.text = text

    def show(self):
        return TemplateSendMessage(
            alt_text="maintain help button message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    MessageTemplateAction(
                        label='目前所有報修',
                        text='maintain/all'
                    ),
                    MessageTemplateAction(
                        label='新增報修',
                        text='maintain/post'
                    )
                ]
            )
        )


class MaintainPostHelpView(View):
    def __init__(self, title='報修球場', text='報修球場指令小幫手', last_input="maintain/post"):
        self.title = title
        self.text = text
        self.last_input = last_input

    def show(self):
        return TemplateSendMessage(
            alt_text="maintain help button message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    MessageTemplateAction(
                        label='籃球場',
                        text=self.last_input+'/1'
                    ),
                    MessageTemplateAction(
                        label='排球場',
                        text=self.last_input+'/2'
                    )
                ]
            )
        )


class SearchTimeHelpView(View):
    def __init__(self, title='搜尋小幫手', text='請選擇搜尋時間', last_input="search"):
        self.title = title
        self.text = text
        self.last_input = last_input

    def show(self):
        return TemplateSendMessage(
            alt_text="account help button message",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期一早上',
                                text=self.last_input+'/time/1'
                            ),
                            MessageTemplateAction(
                                label='星期一下午',
                                text=self.last_input+'/time/2'
                            ),
                            MessageTemplateAction(
                                label='星期一晚上',
                                text=self.last_input+'/time/3'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期二早上',
                                text=self.last_input+'/time/4'
                            ),
                            MessageTemplateAction(
                                label='星期二下午',
                                text=self.last_input+'/time/5'
                            ),
                            MessageTemplateAction(
                                label='星期二晚上',
                                text=self.last_input+'/time/6'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期三早上',
                                text=self.last_input+'/time/7'
                            ),
                            MessageTemplateAction(
                                label='星期三下午',
                                text=self.last_input+'/time/8'
                            ),
                            MessageTemplateAction(
                                label='星期三晚上',
                                text=self.last_input+'/time/9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期四早上',
                                text=self.last_input+'/time/10'
                            ),
                            MessageTemplateAction(
                                label='星期四下午',
                                text=self.last_input+'/time/11'
                            ),
                            MessageTemplateAction(
                                label='星期四晚上',
                                text=self.last_input+'/time/12'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期五早上',
                                text=self.last_input+'/time/13'
                            ),
                            MessageTemplateAction(
                                label='星期五下午',
                                text=self.last_input+'/time/14'
                            ),
                            MessageTemplateAction(
                                label='星期五晚上',
                                text=self.last_input+'/time/15'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期六早上',
                                text=self.last_input+'/time/16'
                            ),
                            MessageTemplateAction(
                                label='星期六下午',
                                text=self.last_input+'/time/17'
                            ),
                            MessageTemplateAction(
                                label='星期六晚上',
                                text=self.last_input+'/time/18'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=self.title,
                        text=self.text,
                        actions=[
                            MessageTemplateAction(
                                label='星期日早上',
                                text=self.last_input+'/time/19'
                            ),
                            MessageTemplateAction(
                                label='星期日下午',
                                text=self.last_input+'/time/20'
                            ),
                            MessageTemplateAction(
                                label='星期日晚上',
                                text=self.last_input+'/time/21'
                            )
                        ]
                    ),
                ]
            )
        )

class SearchCourtHelpView(View):
    def __init__(self, title='搜尋場地', text='請選擇要搜尋的場地', last_input=""):
        self.title = title
        self.text = text
        self.last_input = last_input

    def show(self):
        return TemplateSendMessage(
            alt_text="search court help button message",
            template=ButtonsTemplate(
                title=self.title,
                text=self.text,
                actions=[
                    MessageTemplateAction(
                        label='籃球場',
                        text=self.last_input+'/court/1'
                    ),
                    MessageTemplateAction(
                        label='排球場',
                        text=self.last_input+'/court/2'
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
