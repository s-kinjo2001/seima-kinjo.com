from django.http import HttpResponseForbidden, HttpResponse
import environ
from pathlib import Path

from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
import os
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
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['HTTP_X_LINE_SIGNATURE']
    # リクエストボディを取得
    body = request.body.decode('utf-8')
    try:
        # 署名を検証し、問題なければhandleに定義されている関数を呼び出す
        handler.handle(body, signature)
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