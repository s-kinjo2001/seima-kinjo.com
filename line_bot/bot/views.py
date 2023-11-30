from django.http import HttpResponseForbidden, HttpResponse
import environ
from pathlib import Path

from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler

import base64
import hashlib
import hmac

from linebot.models import (
    MessageEvent,
    TextMessage ,ImageMessage, AudioMessage
)

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(Path.joinpath(BASE_DIR, '.env'))

ACCESSTOKEN = env('ACCESSTOKEN')
LINE_ACCESS_SECRET = env('LINE_ACCESS_SECRET')
line_bot_api = LineBotApi(channel_access_token=ACCESSTOKEN)

handler = WebhookHandler(channel_secret=LINE_ACCESS_SECRET)

def callback(request):
    body = body = request.body.decode('utf-8')
    hash = hmac.new(LINE_ACCESS_SECRET.encode('utf-8'),
        body.encode('utf-8'), hashlib.sha256).digest()
    try:
        signature = base64.b64encode(hash)
    except InvalidSignatureError:
        HttpResponseForbidden()
    # handleの処理を終えればOK
    return HttpResponse('OK', status=200)


# メッセージイベントの場合の処理
# かつテキストメッセージの場合
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # メッセージでもテキストの場合はオウム返しする
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )