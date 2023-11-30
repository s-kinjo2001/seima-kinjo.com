from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creator
from bot.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events']
        for event in events:
            message = event['message']
            reply_token = event['replyToken']
            line_message = LineMessage(message_creator.create_message(message['text']))
            line_message.reply(reply_token)
        return HttpResponse("ok")