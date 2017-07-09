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

line_bot_api = LineBotApi('R4TTAOd0VhSWfLhxx1R3jRTwnwzRVos9UNRKkGjf7tW/iffaL6KXn6zp3CHWafbK0z5pTfopAKBfJHIkdM6xHt+B2AcAZdfmQkESi57QDvcVLN+pMndVsi811gqmHYt0JubvPHeFV7ltS7R3hA8kMAdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('a765040c095986fff77eb159bc269c39') #Your Channel Secret

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
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
