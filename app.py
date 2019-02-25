# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('jECrceNAPz9o/sTtGoslmzNOQVNMN+8TkfedGMCz9FLIFijyT4ykwXFSQ6xd9g7WgCw6wG1NYZxAQLAAajRJNmrTtInWOBgSNROJO3GpjTIQIoIpAoPJm8xkXvzQly/J49U/0rByUFCDXrQ5Z9PUlwdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('fb24bc53fffdcecfbb119f5d1cc5cc98') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

if __name__ == "__main__":
    app.run()