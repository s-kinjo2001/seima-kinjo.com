from django.shortcuts import render
from .models import Tweet, Like, User
from django.db.models import Count

def index(request):
    tweets = Tweet.objects.filter(reply_to__isnull=True).annotate(num_likes=Count('like')).select_related('user_id').order_by('-tweeted_at')
    return render(request, 'sns/index.html', 
        {'tweets': tweets})

def LoginView(BaseLoginView):
    from_class = LoginForm
    template_name = sns/login.html