from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Subscriber, upcomingproject1,upcomingproject2,news,merch1,merch2

class NewsInline(admin.StackedInline):
    model = news
    extra = 2



# Register your models here.
admin.site.register(Subscriber)
admin.site.register(upcomingproject1)
admin.site.register(upcomingproject2)
admin.site.register(news)
admin.site.register(merch1)
admin.site.register(merch2)
