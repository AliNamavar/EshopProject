from django.db import models


# Create your models here.


class Contact(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    email = models.EmailField(max_length=300, verbose_name='Email')
    full_name = models.CharField(max_length=300, verbose_name='Full_name')
    message = models.TextField(verbose_name='contact us text')
    created_date = models.DateTimeField(verbose_name='created day time', auto_now_add=True)
    response = models.TextField(verbose_name='response text', null=True, blank=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='read by admin')

    class Meta:
        verbose_name = 'contact-us'
        verbose_name_plural = 'contact-us-list'

    def __str__(self):
        return self.title


class CreateProfile(models.Model):
    image = models.ImageField(upload_to='images')

