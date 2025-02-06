from django.db import models
from account_module.models import User
from product_module.models import product

# Create your models here.


class Order_Model(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="صاحب سبد خرید"
    )
    is_paid = models.BooleanField(default=False, verbose_name="خرید نهایی شده؟")
    payment_date = models.DateField(null=True, blank=True, verbose_name="تاریخ برداخت")

    def __str__(self):
        return f"{self.User} - {self.is_paid}"

    def calculate_total_price(self):
        total_price = 0
        if self.is_paid:
            for product in self.order_detail_set.all():
                total_price += product.final_price * product.count

        else:
            for product in self.order_detail_set.all():
                total_price += product.product.price * product.count

        return total_price

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Order_detail(models.Model):
    order = models.ForeignKey(Order_Model, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name="محصول")
    final_price = models.IntegerField(
        null=True, blank=True, verbose_name="قیمت نهایی  تکی محثول"
    )
    count = models.IntegerField(verbose_name="تعداد")

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = "Order Detail"
        verbose_name_plural = "Order Details"
