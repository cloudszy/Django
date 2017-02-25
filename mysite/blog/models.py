#coding:utf-8
'''
对象关系映射ORM
生成Post表之后，通过QuerySet与数据库交互
用来从数据库中增删改查，排序过滤等操作
最后我们的Post模型还需通过admin在django自带的web管理界面上生成

'''
from django.db import models
from django.utils import timezone # 获取系统时间
from django.contrib.auth.models import User #创建用户

#models模块内的每一个class对应数据库内的一张表格
class Post(models.Model):
	#作者为主键，和用户绑定
	author = models.ForeignKey(User)
	#标题为普通文本字段，长度限制最大100
	title = models.CharField(max_length= 100)
	#内容text字段，长文本
	text = models.TextField()
	#创建日期
	created_date = models.DateTimeField(default= timezone.now)
	#发布日期
	published_date = models.DateTimeField(blank= True, null=True)

	#保存时间为发布日期
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title




