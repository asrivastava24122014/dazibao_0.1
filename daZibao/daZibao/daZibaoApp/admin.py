from django.contrib import admin
from .models import *
#from .models import WordpinyinForm


class LanguageAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['language']}),(None,{'fields': ['languagecode']}),(None,{'fields': ['languageimage']})]
    list_display = ("languageid","language","languagecode","languageimage")

class WordAdmin(admin.ModelAdmin):
    fields = ['wordchinese','wordcount','wordpos']
    list_display = ("wordid","wordchinese","wordcount","wordpos")
    search_fields = ["=wordid","wordchinese"]
       
class PinyinAdmin(admin.ModelAdmin):
    list_display = ("pinyinid","pinyin",)
    fields = ['pinyin']
    search_fields = ["=pinyinid","pinyin"]

class WordpinyinAdmin(admin.ModelAdmin):
    list_display = ("wordpinyinid","wordpinyin_wordid","wordpinyin_pinyinid","wordpinyinpreferred")
    raw_id_fields = ('wordpinyin_wordid','wordpinyin_pinyinid',)
    search_fields = ["=wordpinyin_wordid__wordchinese","=wordpinyin_pinyinid__pinyin"]

# Word and translation admin
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("translationid","translation","translation_languageid")
    fields = ['translation','translation_languageid']
    search_fields = ["=translationid","translation"]

class WordTranslationAdmin(admin.ModelAdmin):
    list_display = ("wordtranslationid","wordtranslation_wordid","wordtranslation_translationid","wordtranslationeval")
    raw_id_fields = ('wordtranslation_wordid','wordtranslation_translationid',)
    search_fields = ["=wordtranslation_wordid__wordchinese","=wordtranslation_translationid__translation"]

# Translation and Source
class SourceAdmin(admin.ModelAdmin):
    list_display = ("sourceid","source")
    fields = ['source']

class TranslationSourceAdmin(admin.ModelAdmin):
    list_display = ("translationsourceid","translationsource_translationid","translationsource_sourceid")
    raw_id_fields = ['translationsource_translationid','translationsource_sourceid']
    search_fields = ["translationsource_translationid__translation","translationsource_sourceid__source"]


admin.site.register(Language,LanguageAdmin)
admin.site.register(Word,WordAdmin)
admin.site.register(Pinyin,PinyinAdmin)
admin.site.register(Wordpinyin,WordpinyinAdmin)
admin.site.register(Translation,TranslationAdmin)
admin.site.register(Wordtranslation,WordTranslationAdmin)
admin.site.register(Source,SourceAdmin)
admin.site.register(Translationsource,TranslationSourceAdmin)

