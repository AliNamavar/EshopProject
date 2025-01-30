from django.urls import path
from product_module import views

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    path('', views.ProductListView.as_view(), name='product_list'),
    path('p-cate/<str:category>', views.ProductListView.as_view(), name='product_category'),
    path('p-brand/<str:brand>', views.ProductListView.as_view(), name='product_Brand'),
    path('favorite', views.addProductFavorite.as_view(), name='product_favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]