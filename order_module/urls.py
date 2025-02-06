from django.urls import path
from . import views

urlpatterns = [
    path(
        "add-product-to-order",
        views.add_product_to_order.as_view(),
        name="add-product-to-order",
    ),
    path("Order", views.Order_View.as_view(), name="OrderView"),
    path("Order-delete-product", views.Order_remove_product, name="rmProduct"),
    path(
        "order-edit-count",
        views.EditOrderDetailCount.as_view(),
        name="EditOrderDetailCount",
    ),
]
