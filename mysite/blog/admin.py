#coding: utf-8
from django.contrib import admin
#导入Post表单模型
from .models import Post

#把Post模型添加在django自带的管理页面上
admin.site.register(Post)
