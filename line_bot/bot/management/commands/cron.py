from django.core.management.base import BaseCommand
import environ
from pathlib import Path
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, ImageMessage, PostbackEvent, TextSendMessage

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(Path.joinpath(BASE_DIR, '.env'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        BASE_DIR = Path(__file__).resolve().parent.parent
        env = environ.Env()
        environ.Env.read_env(Path.joinpath(BASE_DIR, '.env'))
        ACCESSTOKEN = env('ACCESSTOKEN')
        LINE_ACCESS_SECRET = env('LINE_ACCESS_SECRET')
        GROUP_ID = env('GROUP_ID')
        line_bot_api = LineBotApi(channel_access_token=ACCESSTOKEN)
        line_bot_api.push_message(GROUP_ID, TextSendMessage(text=msg))
