from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="images/users", verbose_name="نصویر آواتار", null=True, blank=True
    )
    email_active_code = models.CharField(
        max_length=75, verbose_name="کد فعالسازی ایمیل"
    )
    about_user = models.TextField(verbose_name="درباره ی کاربر", null=True, blank=True)
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        if self.username and self.last_name is not "":
            return self.get_full_name()

        return self.email
