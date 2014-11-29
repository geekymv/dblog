#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Article
from django.template.context import RequestContext

# Create your views here.
# 博客列表
def blog_list(request):
    
    blogs = Article.objects.all().order_by('-publish_time')
    
    return render_to_response('blog_list.html',
                              {'blogs': blogs},
                              context_instance=RequestContext(request))

# 查看博客
def detail(request, id):
    
    blog = get_object_or_404(Article, pk=id)
    
    return render_to_response('detail.html',
                              {'blog': blog},
                              context_instance=RequestContext(request))

def update(request, id):
    
    return render_to_response()    
    
    
    
    
     
        