from modeltranslation.translator import register, TranslationOptions

from .models import Todo


@register(Todo)
class TodoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
