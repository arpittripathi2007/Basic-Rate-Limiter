from django.contrib import admin
from django.db import models
from handlers.models import User, RateLimitUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(User)
admin.site.register(RateLimitUser)