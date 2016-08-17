from django.contrib import admin

# Register your models here.
from .models import Tweet, User, Clergy

admin.site.register(Tweet)
admin.site.register(User)
admin.site.register(Clergy)