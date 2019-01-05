from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings 
from django.conf.urls.static import static


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '已发布'),
    )
    BLOG_TYPE = (
        ('normal', '普通'),
        ('star', '精选')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              verbose_name='状态',
                              default='draft')
    blog_type  = models.CharField(
        max_length = 10,
        choices=BLOG_TYPE,
        default='normal',
        verbose_name='类型'
        )
    image = models.ImageField(upload_to='upload', 
        verbose_name='图片', 
        null=True)


    # 显示排序
    class Meta:
        ordering = ('-publish',)

    # 返回title名称
    def __str__(self):
        return self.title

