from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from comments.models import CommentsModel


class CommentsModelAdmin(ModelAdmin):
    list_display = ['content', 'story', 'user', 'created']


admin.site.register(CommentsModel, CommentsModelAdmin)
