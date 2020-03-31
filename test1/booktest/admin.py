from django.contrib import admin

from booktest.models import BookInfo
from booktest.models import HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    '''自定义模型管理类'''
    list_display = ['id', 'btitle', 'bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    '''自定义管理类'''
    list_display = ['id', 'hname', 'hcommtent']

# Register your models here.
# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
