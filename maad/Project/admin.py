#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import URLData, Project, Folder, TextData, Picture
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('user','name','publish_date')

class FolderAdmin(admin.ModelAdmin):
	list_display = ('title','created_date','proj')
class URLDataAdmin(admin.ModelAdmin):
	list_display = ('title','link','tag','folder')

class PictureAdmin(admin.ModelAdmin):
	list_display = ('folder', 'file')

admin.site.register(URLData,URLDataAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(TextData)
admin.site.register(Picture,PictureAdmin)


