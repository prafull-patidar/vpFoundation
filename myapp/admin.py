from django.contrib import admin
from myapp.models import Contact, helpModel, joinUsModel
# Register your models here.

class custJoinUsModel(admin.ModelAdmin):
    list_display = ['pk','name','email','phone','wpPhone','address','occupation','date','varified']
    list_display_links = ['pk','name','email','phone','wpPhone','address','occupation','date','varified']
    list_filter = ('date','varified')

class custHelpModel(admin.ModelAdmin):
    list_display = ['pk','help_type','name','email','phone','wpPhone','currentAddress','permanentAddress','city','date','isHelpReached','message']
    list_display_links = ['pk','help_type','name','email','phone','wpPhone','currentAddress','permanentAddress','city','date','isHelpReached','message']
    list_filter = ('date','isHelpReached','city')

class custContact(admin.ModelAdmin):
    list_display = ['name','email','subject','suggestion']
    list_display_links = ['name','email','subject','suggestion']

admin.site.site_title = "Vedprakash Foundation Admin"
admin.site.site_header = "Vedprakash Foundation Admin Panel"
admin.site.index_title = "Welcome to Vedprakash Foundation Admin Panel"
admin.site.register(joinUsModel,custJoinUsModel)
admin.site.register(helpModel,custHelpModel)
admin.site.register(Contact,custContact)
