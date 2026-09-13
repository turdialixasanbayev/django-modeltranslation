from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(TranslationAdmin):
    list_display = ('title', 'completed', 'created_at')
