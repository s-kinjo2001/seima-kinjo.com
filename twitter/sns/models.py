from django.db import models
import string
import random
from datetime import datetime 

def media_save_path(instance, filename):
    extension = filename.split('.')[-1]
    today = datetime.now().strftime("%Y%m%d")
    new_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return f'{today}/{new_filename}.{extension}'

class User(models.Model):
    username = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=160, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to=media_save_path, blank=True, null=True)
    header_image = models.ImageField(upload_to=media_save_path, blank=True, null=True)

    def __str__(self):
        return f'@{self.username} {self.name}さん'

class List(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100, blank=True)
    header_image = models.ImageField(upload_to=media_save_path, blank=True, null=True)
    is_private = models.BooleanField(default=False)

class Follow(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followee_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followee")

class Tweet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    image = models.ImageField(upload_to=media_save_path, blank=True, null=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, related_name="reply", blank=True, null=True)
    quote_tweet_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name="quote", blank=True, null=True)
    tweeted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user_id}のツイート:{self.content}'

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)

class Retweet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    retweeted_at = models.DateTimeField(auto_now_add=True)

class FollowList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)

class ListMember(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)