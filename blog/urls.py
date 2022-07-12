from django.urls import path
from . import views

# 命名空间防止与其他应用的类似页面（同名之类的）引起冲突
app_name = 'blog'

# 使用path函数绑定url(即django中Views里编写的函数)
urlpatterns = [
    path('', views.index, name='index'),  # 这里是index函数,name参数设置别名（不会起作用，起作用的是view里绑定的函数）
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tag/<int:pk>/', views.tag, name='tag'),    
]