from django.db import models

# Create your models here.


class siteSettings(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام سایت')
    site_url = models.CharField(max_length=100, verbose_name='دامنه سایت')
    about_us_text = models.TextField(verbose_name='توضیحات سایت')
    is_main_setting = models.BooleanField(default=True, verbose_name='تنظیمات اصلی')
    address = models.CharField(max_length=100, verbose_name='آدرس سایت')
    phone_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='شماره ی سایت')
    fax_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='فکس سایت')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='ایمیل سایت')
    copyright_holder = models.TextField(verbose_name='متن کپی رایت')
    site_logo = models.ImageField(upload_to='images/site_setting', verbose_name='لوگو سایت')
    work_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name='ساعات کاری')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Setting's"
        verbose_name_plural = 'Settings'

class footerLinkBox(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')


    class Meta:
        verbose_name = "Category link footer"
        verbose_name_plural = "Category's link footer"

    def __str__(self):
        return self.title

class footerLink(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(verbose_name='لینک')
    footer_link_box = models.ForeignKey(footerLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = " footer link"
        verbose_name_plural = 'footer links'

    def __str__(self):
        return f'{self.title} - {self.url}'



class slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=100, verbose_name='عنوان لینک')
    descriptions = models.TextField(verbose_name='توضیحات')
    images = models.ImageField(upload_to='images/slider', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='Active / Inactive')

    class Meta:
        verbose_name = "slayder"
        verbose_name_plural = "slayder's"

    def __str__(self):
        return self.title


class site_banner(models.Model):
    class site_banner_position(models.TextChoices):
        product_list = 'product_list', 'صفحه ی لیست محصولات'
        product_detail = 'product_detail', 'صفحه ی جزییات محصولات'
        article_detail = 'article_detail', 'جزییات مقاله'

    title = models.CharField(max_length=100, verbose_name='عنوان بنر')
    url_title = models.URLField(max_length=400, verbose_name='عنوان بنر در url', null=True, blank=True)
    image = models.ImageField(upload_to='images/banner', verbose_name='عکس بنر')
    is_active = models.BooleanField(max_length=100, verbose_name='فعال / غیر فعال ')
    position = models.CharField(max_length=100, verbose_name='جایگاه نمایش محصول', choices=site_banner_position.choices)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "banners"