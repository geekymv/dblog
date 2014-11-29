from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
                       
    url(r'^$', 'blog_list', name='blog_list'),
    url(r'^detail/(?P<id>\d+)/$', 'detail', name='detail')
)
