from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from flask import Flask, request, abort
import os

app = Flask(__name__)

# Ganti dengan Channel access token Anda
wnpXRw4OFuXa7VJwZj9ABq7uTPpSXnN2Om8cfu8mtbQUTYWTKI7sTfNL9es722d5g+lmq9oTjEqwSrtPKw/Qi/ZTZPibfGmQdw2gPRu+UpuH//8FqLRAb+s1MWePl3Zxwl91hVNUFRrTwjsomNNbQwdB04t89/1O/w1cDnyilFU= = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
if not wnpXRw4OFuXa7VJwZj9ABq7uTPpSXnN2Om8cfu8mtbQUTYWTKI7sTfNL9es722d5g+lmq9oTjEqwSrtPKw/Qi/ZTZPibfGmQdw2gPRu+UpuH//8FqLRAb+s1MWePl3Zxwl91hVNUFRrTwjsomNNbQwdB04t89/1O/w1cDnyilFU=:
    print("Error: LINE_CHANNEL_ACCESS_TOKEN tidak ditemukan di environment variable.")
    exit()

line_bot_api = LineBotApi(wnpXRw4OFuXa7VJwZj9ABq7uTPpSXnN2Om8cfu8mtbQUTYWTKI7sTfNL9es722d5g+lmq9oTjEqwSrtPKw/Qi/ZTZPibfGmQdw2gPRu+UpuH//8FqLRAb+s1MWePl3Zxwl91hVNUFRrTwjsomNNbQwdB04t89/1O/w1cDnyilFU=)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # handle webhook body
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e)
    return 'OK'

from linebot.models.events import MessageEvent, TextMessageContent
from linebot.models.messages import TextSendMessage
from linebot.exceptions import InvalidSignatureError
from linebot import WebhookHandler

# Ganti dengan Channel secret Anda
89d7ff71173f8f8db68da3a9d4ea20a2 = os.environ.get('LINE_CHANNEL_SECRET')
if not 89d7ff71173f8f8db68da3a9d4ea20a2:
    print("Error: LINE_CHANNEL_SECRET tidak ditemukan di environment variable.")
    exit()

handler = WebhookHandler(89d7ff71173f8f8db68da3a9d4ea20a2)

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text + " (Bot ini sedang dalam pengembangan)"))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
