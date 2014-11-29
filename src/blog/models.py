#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# 标签
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.tag_name

# 分类    
class Classification(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name 

# 作者
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name

# 文章
class Article(models.Model):
    caption = models.CharField(max_length=30) # 标题
    subcaption = models.CharField(max_length=50, blank=True) # 子标题
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author)
    classfication = models.ForeignKey(Classification)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()

