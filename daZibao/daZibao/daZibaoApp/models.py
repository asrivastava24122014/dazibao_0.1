# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
#from django import forms


# Register your models here.
   
class Image(models.Model):
    imageid = models.AutoField(db_column='imageID', primary_key=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)
    imagehostpagedisplayurl = models.CharField(db_column='imageHostPageDisplayURL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imagehumaneval = models.IntegerField(db_column='imageHumanEval', blank=True, null=True)  # Field name made lowercase.
    imageracyscore = models.FloatField(db_column='imageRacyScore')  # Field name made lowercase.
    image_imagemarketid = models.ForeignKey('Imagemarket', on_delete=models.CASCADE, db_column='image_imageMarketID')  # Field name made lowercase.
    imageadultscore = models.FloatField(db_column='imageAdultScore')  # Field name made lowercase.
    imagename = models.CharField(db_column='imageName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imagethumbnail = models.TextField(db_column='imageThumbnail', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.imagename

    class Meta:
        managed = False
        db_table = 'image'


class Imagemarket(models.Model):
    imagemarketid = models.AutoField(db_column='imageMarketID', primary_key=True)  # Field name made lowercase.
    imagemarket = models.CharField(db_column='imageMarket', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imagemarketdescription = models.CharField(db_column='imageMarketDescription', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.imagemarket

    class Meta:
        managed = False
        db_table = 'imagemarket'


class Imsource(models.Model):
    imsourceid = models.AutoField(db_column='imsourceID', primary_key=True)  # Field name made lowercase.
    imsource = models.CharField(max_length=50)

    def __str__(self):
        return self.imsource

    class Meta:
        managed = False
        db_table = 'imsource'


class Language(models.Model):
    languageid = models.AutoField(db_column='languageID', primary_key=True)  # Field name made lowercase.
    language = models.CharField(max_length=45, blank=True, null=True)
    languagecode = models.CharField(db_column='languageCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    languageimage = models.TextField(db_column='languageImage', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.language

    class Meta:
        managed = False
        db_table = 'language'
        ordering = ['languageid']
       

class Pinyin(models.Model):
    pinyinid = models.AutoField(db_column='pinyinID', primary_key=True)  # Field name made lowercase.
    pinyin = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.pinyin

    class Meta:
        managed = False
        db_table = 'pinyin'
        ordering = ['pinyinid']
       
class Source(models.Model):
    sourceid = models.AutoField(db_column='sourceID', primary_key=True)  # Field name made lowercase.
    source = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.source

    class Meta:
        managed = False
        db_table = 'source'
        ordering = ['sourceid']


class Translation(models.Model):
    translationid = models.AutoField(db_column='translationID', primary_key=True)  # Field name made lowercase.
    translation = models.CharField(max_length=300, blank=True, null=True)
    translation_languageid = models.ForeignKey(Language, on_delete=models.CASCADE, db_column='translation_languageID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.translation

    class Meta:
        managed = False
        db_table = 'translation'
        ordering = ['translationid']


class Translationsource(models.Model):
    translationsourceid = models.AutoField(db_column='translationSourceID', primary_key=True)  # Field name made lowercase.
    translationsource_translationid = models.ForeignKey(Translation, on_delete=models.CASCADE, db_column='translationSource_translationID')  # Field name made lowercase.
    translationsource_sourceid = models.ForeignKey(Source, on_delete=models.CASCADE, db_column='translationSource_sourceID')  # Field name made lowercase.

    def __str__(self):
        return str(self.translationsourceid)

    class Meta:
        managed = False
        db_table = 'translationsource'
        ordering = ['translationsourceid']


class Word(models.Model):
    wordid = models.AutoField(db_column='wordID', primary_key=True)  # Field name made lowercase.
    wordchinese = models.CharField(db_column='wordChinese', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    wordcount = models.IntegerField(db_column='wordCount', blank=True, null=True)  # Field name made lowercase.
    wordpos = models.CharField(db_column='wordPOS', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.wordchinese

    class Meta:
        managed = False
        db_table = 'word'
        ordering = ['-wordcount']

class Wordimage(models.Model):
    wordimageid = models.AutoField(db_column='wordImageID', primary_key=True)  # Field name made lowercase.
    wordimage_wordid = models.ForeignKey(Word, on_delete=models.CASCADE, db_column='wordImage_wordID')  # Field name made lowercase.
    wordimage_imageid = models.ForeignKey(Image, on_delete=models.CASCADE, db_column='wordImage_imageID')  # Field name made lowercase.

    def __str__(self):
        return self.wordimageid

    class Meta:
        managed = False
        db_table = 'wordimage'
        ordering = ['wordimageid']

class Wordpinyin(models.Model):
    wordpinyinid = models.AutoField(db_column='wordPinyinID', primary_key=True)  # Field name made lowercase.
    wordpinyin_wordid = models.ForeignKey(Word, on_delete=models.CASCADE, db_column='wordPinyin_wordID')  # Field name made lowercase.
    wordpinyin_pinyinid = models.ForeignKey(Pinyin, on_delete=models.CASCADE, db_column='wordPinyin_pinyinID')  # Field name made lowercase.
    wordpinyinpreferred = models.IntegerField(db_column='wordPinyinPreferred', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.wordpinyinid)

    class Meta:
        managed = False
        db_table = 'wordpinyin'
        ordering = ['wordpinyinid']


class Wordtranslation(models.Model):
    wordtranslationid = models.AutoField(db_column='wordTranslationID', primary_key=True)  # Field name made lowercase.
    wordtranslation_wordid = models.ForeignKey(Word, on_delete=models.CASCADE, db_column='wordTranslation_wordID')  # Field name made lowercase.
    wordtranslation_translationid = models.ForeignKey(Translation, on_delete=models.CASCADE, db_column='wordTranslation_translationID')  # Field name made lowercase.
    wordtranslationeval = models.IntegerField(db_column='wordTranslationEval', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.wordtranslationid)

    class Meta:
        managed = False
        db_table = 'wordtranslation'
        ordering = ['wordtranslationid']

#class WordpinyinForm(forms.ModelForm):
#    parent = forms.ChoiceField(required=False,
#                              choices=Wordpinyin.objects.values_list('wordpinyinid', 'wordpinyinid'))
#    word = forms.ChoiceField(required=False,
#                              choices=Word.objects.values_list('wordid', 'wordid'))
#    pinyin = forms.ChoiceField(required=False,
#                              choices=Pinyin.objects.values_list('pinyinid', 'pinyinid'))

#    class Meta:
#        model = Wordpinyin
