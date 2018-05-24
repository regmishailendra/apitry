from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from story.models import StoryModel


class StoryModelAdmin(ModelAdmin):
        list_display = ['title', 'content', 'user']

admin.site.register(StoryModel, StoryModelAdmin)
