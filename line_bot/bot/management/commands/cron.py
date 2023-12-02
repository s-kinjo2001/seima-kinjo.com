from django.core.management.base import BaseCommand
import environ
from pathlib import Path
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, ImageMessage, PostbackEvent, TextSendMessage, VideoSendMessage
from datetime import datetime, date
from monthdelta import monthmod

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

        waddingdate = datetime(2023,1,6)
        today = datetime.now()
        elapsed = today - waddingdate
        mmod =  monthmod(waddingdate, today)

        elapsed_month = mmod[0].months % 12
        elapsed_year = mmod[0].months // 12

        if elapsed_year == 0:
            msg = "結婚してから今日で" + str(elapsed_month) + "ヶ月が経ちました。"
        elif elapsed_month == 0:
            msg = "結婚してから今日で" + str(elapsed_year) + "年" + "が経ちました！"
        else:
            msg = "結婚してから今日で" + str(elapsed_year) + "年と" + str(elapsed_month) + "ヶ月が経ちました。"

        line_bot_api = LineBotApi(channel_access_token=ACCESSTOKEN)
        line_bot_api.push_message(GROUP_ID, TextSendMessage(text=msg))
