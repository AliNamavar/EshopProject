from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

from account_module.models import User


# verbose_name har ja bod midge ke in har namayesh dade shod ba on esme verbose namayesh dade beshe
# Create your models here.


class productCategory(models.Model):
    parent = models.ForeignKey(
        "productCategory",
        on_delete=models.CASCADE,
        verbose_name="دسته بندی والد",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=300, db_index=True, verbose_name="عنوان")
    url_title = models.CharField(
        max_length=300, db_index=True, verbose_name="عنوان در url"
    )
    is_active = models.BooleanField(verbose_name="Active / Inactive")
    is_deleted = models.BooleanField(verbose_name="Deleted / NoDeleted")

    def __str__(self):
        return f"({self.title} - {self.url_title})"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category's"


class product_Brands(models.Model):
    title = models.CharField(max_length=300, verbose_name="نام برند", db_index=True)
    url_title = models.CharField(
        max_length=300, db_index=True, verbose_name="عنوان در دامنه"
    )
    is_active = models.BooleanField(verbose_name="Avtive / Inactive")

    class Meta:
        verbose_name = "Berand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.title


class product(models.Model):  # hatman max_lenght ro bayad bedy
    category = models.ManyToManyField(
        productCategory, related_name="product_Category", verbose_name="Category's"
    )
    Brand = models.ForeignKey(
        product_Brands,
        on_delete=models.CASCADE,
        verbose_name="brand",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=300)
    price = models.IntegerField(verbose_name="Price")
    images = models.ImageField(
        upload_to="images/product", verbose_name="تصویر", null=True, blank=True
    )
    # raiting = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.CharField(
        max_length=360, null=True, db_index=True, verbose_name="Short Description"
    )
    description = models.TextField(verbose_name="Description", db_index=True)
    is_active = models.BooleanField(default=False, verbose_name="Active / inactive")
    slug = models.SlugField(
        default="", null=False, blank=True, db_index=True, max_length=200, unique=True
    )
    is_deleted = models.BooleanField(verbose_name="Deleted / NoDeleted")

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "Product's"


class Product_Tags(models.Model):
    Caption = models.CharField(max_length=50, db_index=True, verbose_name="Tag")
    product_tag = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name="productTags"
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.Caption


class ProductVisitCount(models.Model):
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name="productVisitCount"
    )
    ip = models.CharField(max_length=20, verbose_name="IP")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="productVisitCount",
        null=True,
        blank=True,
    )
