from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    
    # 设置Post文章管理页面显示哪些列
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

    # 设置增加/修改Post时的页面(Post的表单页面)显示哪些列
    field = ['title', 'body', 'excerpt', 'category', 'tags']

    
    def save_model(self, request, obj, form, change):
        """
        修改作者，修改admin的数据并存到数据库中
        """
        obj.author = request.user        
        super().save_model(request, obj, form, change)



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

