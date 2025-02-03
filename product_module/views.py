from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Count
from utils.http_service_get_ip import get_client_ip
from site_module.models import site_banner
from .models import product, productCategory, product_Brands, ProductVisitCount
from django.db.models import Q

# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 2



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = product.objects.all()
        products: product = query.order_by('-price').first()
        db_max_price = products.price if products is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = site_banner.objects.filter(is_active=True, position__iexact=site_banner.site_banner_position.product_list)
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        request = self.request

        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if end_price is not None:
            query = query.filter(price__lte=end_price)

        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        brand_name = self.kwargs.get('brand')
        if brand_name is not None:
            query = query.filter(Brand__url_title__iexact=brand_name)

        search_query = self.request.GET.get('search')
        if search_query is not None:
            query = query.filter(Q(title__icontains=search_query))

        return query



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'

    model = product
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.object
        request = self.request
        favorite_products = request.session.get('favorite_products')
        context['is_favorite'] = favorite_products == str(products.id)
        context['banners'] = site_banner.objects.filter(is_active=True, position__iexact=site_banner.site_banner_position.product_detail)


        user_ip = get_client_ip(request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id

        hasBeenVisisted = ProductVisitCount.objects.filter(
            ip__iexact=get_client_ip(request),
            product = products,
        ).exists()
        if hasBeenVisisted is False:
            new_visit = ProductVisitCount.objects.create(
                ip = user_ip,
                product = products,
                user_id = user_id,
            )



        return context




class addProductFavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        products = product.objects.get(pk=product_id)
        request.session['favorite_products'] = product_id
        return redirect(products.get_absolute_url())

def products_category_component(request):
    products_category = productCategory.objects.filter(is_active=True, parent_id=None, is_deleted=False).prefetch_related('productcategory_set')
    context = {
        'products_category': products_category
    }
    return render(request, 'Category_component/product_category_component.html', context)


def product_brand_component(request):
    product_brand = product_Brands.objects.filter(is_active=True).annotate(product_count=Count('product'))
    context = {
        'product_brand': product_brand
    }
    return render(request, 'Category_component/product_brand_component.html', context)