from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Director)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
