from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Subscriber, project

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(project)