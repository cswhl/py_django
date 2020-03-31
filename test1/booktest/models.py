from django.db import models
# 设计和表对应的类、模型类
# Create your models here.

# 图书类


class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle


class HeroInfo(models.Model):
    '''英雄类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcommtent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        # 返回英雄名
        return self.hname
