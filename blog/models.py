from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


# Create your models here.

# 利用ORM，django将python语言映射为数据库语法。这就是Model(不过要继承models.Model)
class Category(models.Model):
    """
    文章分类
    """ 
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

     # 数据库的字段
    def __str__(self):
        return self.name  

    
class Tag(models.Model):
    """
    文章标签
    """

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=100)


class Post(models.Model):
    """
    发布文章的主数据库
    """    

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']  # "-" ->逆序,使用列表存储，可以指定多个排序关键字(append即可)

    title = models.CharField('标题', max_length=70)

    body = models.TextField('正文')  # 长文本类型

    # 设置文章摘要，blank参数表示允许字段值为空
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    created_time = models.DateTimeField('创建时间', default=timezone.now)   
    modified_time = models.DateTimeField('修改时间')   

    # 文章与分类是一对多的关系，文章与标题是多对多的关系
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)  # 外键必须要设置on——delete模式
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
            return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                ])
        # 将body正文(md格式)中的渲染成html文本
        # convert转换时会忽视html标签，所以可以直接strip_tag取html文本前54个字符作为摘要
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        获得pk并组合规则为<ip>/detail/posts/<pk>,返回给“django”该结果
        """
        # blog:detail表示这个detailurl属于blogapp(声明了命名空间在app/urls文件中)
        return reverse('blog:detail', kwargs={'pk': self.pk})
    
    