from django.db import models
from django.utils.text import slugify
from jalali_date import datetime2jalali, date2jalali
from account_module.models import User


# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Is active')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = "Articl's Categories"




class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=400, db_index=True, unique=True, verbose_name='عنوان در url', allow_unicode=True, blank=True)
    image = models.ImageField(upload_to='images/Article', verbose_name='تصویر')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی')
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخته شده', editable=False)


    def __str__(self):
        return self.title
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def date_time_created(self):
        return date2jalali(self.created_date)

    def get_date_created_time(self):
        return self.created_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = "Article's"


class ArticleComments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=' مقاله')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    parent = models.ForeignKey('ArticleComments', on_delete=models.CASCADE, verbose_name='پاسخ والد', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن')


    def __str__(self):
        return f'{self.article} - {self.author}'

    class Meta:
        verbose_name = 'Article_Comment'
        verbose_name_plural = 'Article_Comments'
