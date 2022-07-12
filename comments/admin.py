from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    
    # 注册哪些模型，一般当然全注册呀
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    
    # 实际展示哪些
    fields = ['name', 'email', 'url', 'post']

# 注册到app的admin后台，admin.site.register(pos1, pos2) -> 被注册的模型，管理模型的类(admin.py写的)
admin.site.register(Comment, CommentAdmin)