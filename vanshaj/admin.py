from django.contrib import admin
from vanshaj.models import User, Comment, Topic


# Register your models here.
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Comment)