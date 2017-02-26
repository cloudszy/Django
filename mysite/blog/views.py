#coding:utf-8
'''
动态模板
通过views视图功能，连接模型Post和模板templates显示在首页上面
再通过QuerySet将数据库中的数据检索出来，传给模板显示出来
'''
#render包含post，get等请求，来获取数据库表单的数据，再传送到模板内显示出来，{}，标签属于占位符，负责给模板传递数据
from django.shortcuts import render
from .models import Post


def post_list(request):
	#QuerySet语句，过滤Post内的数据，按时间发布逆序排序
	posts = Post.objects.filter(published_date__isnull= False).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})