from django.http import HttpResponseForbidden, HttpResponse
import environ
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler

from linebot.models import MessageEvent, TextMessage, ImageMessage, PostbackEvent, TextSendMessage, VideoSendMessage

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(Path.joinpath(BASE_DIR, '.env'))

ACCESSTOKEN = env('ACCESSTOKEN')
LINE_ACCESS_SECRET = env('LINE_ACCESS_SECRET')
line_bot_api = LineBotApi(channel_access_token=ACCESSTOKEN)

handler = WebhookHandler(channel_secret=LINE_ACCESS_SECRET)

@csrf_exempt
def callback(request):
    # signatureの取得
    signature = request.headers['X-Line-Signature']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    return HttpResponse(status=200)


# メッセージイベントの場合の処理
# かつテキストメッセージの場合
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    if event.message.text == "クリスマス" or event.message.text == "xmas":
        line_bot_api.reply_message(
            event.reply_token,
            VideoSendMessage(original_content_url="https://seima-kinjo.com:10443/static/bot/video/xmas-video-01.mp4",
                    preview_image_url="https://seima-kinjo.com:10443/static/bot/img/xmas-thumbnail-01.jpg")
        )