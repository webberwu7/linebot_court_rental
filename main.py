import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
from router import text_router

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ.get('ChannelAccess', 'ChannelAccess'))
# Channel Secret
handler = WebhookHandler(os.environ.get('ChannelSecret', 'ChannelSecret'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    print("signature : ", signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user input message
    inputText = event.message.text

    # parser user input message
    print("debug: " + str(inputText))
    inputCommand = text_router.parser_text(inputText)

    # return somthing to user
    message = TextSendMessage(text=inputCommand)
    line_bot_api.reply_message(
        event.reply_token,
        message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
