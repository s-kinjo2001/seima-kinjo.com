from django.shortcuts import render
from .models import Tweet, Like, User, Retweet
from django.db.models import Count

def index(request):
    tweets = Tweet.objects.filter(reply_to__isnull=True).annotate(num_likes=Count('like', distinct=True),num_retweets=Count('retweet', distinct=True)).select_related('user_id').order_by('-tweeted_at')
    return render(request, 'sns/index.html', 
        {'tweets': tweets})

def top(request):
    return render(request, 'sns/top.html')