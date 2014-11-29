from django.contrib import admin

# Register your models here.

from blog.models import Author, Article, Tag, Classification

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website')
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
  
        


admin.site.register(Author, AuthorAdmin)   
admin.site.register(Article, ArticleAdmin) 
admin.site.register(Tag)
admin.site.register(Classification)

