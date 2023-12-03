from django.core.management.base import BaseCommand
import environ
from pathlib import Path
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, ImageMessage, PostbackEvent, TextSendMessage, VideoSendMessage
from datetime import datetime, date
from monthdelta import monthmod
import requests

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

        Request_URL_weather = 'https://weather.tsukumijima.net/api/forecast'

        city_id = '130010'
        res = requests.get(Request_URL_weather + '/city/' + city_id)
        result = res.json()
        weather_td = result['forecasts'][0]
        date_year = date.today().year
        date_month = date.today().month
        date_day = date.today().day
        date_td = str(date_year) + "年" + str(date_month) + "月" + str(date_day) + "日"
        

        if weather_td['temperature']['min']['celsius'] is None:
            weather_td['temperature']['min']['celsius'] = '--'
            temperature = [weather_td['temperature']['min']['celsius'],weather_td['temperature']['max']['celsius']]
            chanceOfRain = [weather_td['chanceOfRain']['T06_12'],weather_td['chanceOfRain']['T12_18'],weather_td['chanceOfRain']['T18_24']] 
        else:
            temperature = [weather_td['temperature']['min']['celsius'],weather_td['temperature']['max']['celsius']]
            chanceOfRain = [weather_td['chanceOfRain']['T06_12'],weather_td['chanceOfRain']['T12_18'],weather_td['chanceOfRain']['T18_24']]        
        title_td = weather_td['image']['title']
        print(chanceOfRain)
        print(title_td)
        print(temperature)
        msg = '★' + date_td + 'の東京都の天気★\n＜今日は ' + title_td + ' です！🐢＞\n・・・・・・・・・・・・\n最高気温：' + temperature[1] + '℃\n最低気温：' + temperature[0] + '℃\n\n【降水確率】\n06時-12時:'+ chanceOfRain[0] + '\n12時-18時:' + chanceOfRain[1] + '\n18時-24時:' + chanceOfRain[2] + "\n・・・・・・・・・・・・"
        line_bot_api = LineBotApi(channel_access_token=ACCESSTOKEN)
        line_bot_api.push_message(GROUP_ID, TextSendMessage(text=msg))