from django.contrib import admin
from .models import User, Tweet, List, Like, Retweet, Follow, FollowList, ListMember
# Register your models here.

class RetweetAdmin(admin.ModelAdmin):
    readonly_fields = ('retweeted_at',)

class TweetAdmin(admin.ModelAdmin):
    readonly_fields = ('tweeted_at',)

admin.site.register(User)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(List)
admin.site.register(Like)
admin.site.register(Retweet, RetweetAdmin)
admin.site.register(Follow)
admin.site.register(FollowList)
admin.site.register(ListMember)