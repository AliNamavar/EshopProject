from http.cookiejar import cut_port_re

from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.http import JsonResponse
from product_module.models import product
from .models import Order_Model, Order_detail
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.


class add_product_to_order(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        count = request.POST.get('count')
        if count is None:
            count = 1
        if request.user.is_authenticated:
            if int(count) < 1:
                return JsonResponse({
                    'status': 'error',
                    'message': 'تعداد محصول نمیتواند کمتر از 1 باشد',
                    'icon': 'error'
                })
            else:
                product_get = product.objects.filter(id=product_id, is_active=True, is_deleted=False).first()
                if product_get is None:
                    return JsonResponse({
                        'status': 'error',
                        'message': 'محصول مورد نظر یافت نشد',
                        'icon': 'error'

                    })
                else:
                    current_order, created = Order_Model.objects.get_or_create(User=request.user, is_paid=False)
                    product_detail = current_order.order_detail_set.filter(product_id=product_get).first()
                    if product_detail is not None:
                        product_detail.count += int(count)
                        product_detail.save()
                        return JsonResponse({
                            'status': 'success',
                            'message': 'محصول با موفقیت در سبد خرید شما ذخیره شد',
                            'icon': 'success'
                        })
                    else:
                        current_order.order_detail_set.create(
                            product=product_get,
                            count=int(count),
                            order=current_order,
                        )
                        return JsonResponse({
                            'status': 'success',
                            'message': 'محصول با موفقیت در سبد خرید شما ذخیره شد',
                            'icon': 'success'
                        })
        else:
            return JsonResponse({
                'status': 'not_auth',
                'message': 'you most log in to your account first',
                'icon': 'info'

            })


class Order_View(View):
    def get(self, request, *args, **kwargs):
        current_order, created = Order_Model.objects.prefetch_related('order_detail_set').get_or_create(
            User=request.user, is_paid=False)
        total_price = current_order.calculate_total_price()

        context = {
            'Order': current_order,
            'total_price': total_price,

        }
        return render(request, 'order_module/OrderListView.html', context)


def Order_remove_product(request):
    product_id = int(request.GET.get('product_id'))
    if product_id is not None:
        current_order, created = Order_Model.objects.get_or_create(User=request.user, is_paid=False)
        product_detail = Order_detail.objects.filter(product_id=product_id, order=current_order).first()
        if product_detail is None:
            return JsonResponse({
                'status': 'error',
                'message': 'محصول مورد نظر یافت نشد toye'

            })
        else:
            product_detail.delete()
            total_price = current_order.calculate_total_price()
            return JsonResponse({
                'status': 'success',
                'data': render_to_string('order_partials/order_rm_partials.html', context={
                    'Order': current_order,
                    'total_price': total_price,

                })
            })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'محصول مورد نظر یافت نشد'
        })


class EditOrderDetailCount(View):
    def post(self, request, *args, **kwargs):
        product_id = int(request.POST.get('product_id'))
        newCount = str(request.POST.get('newCount'))

        current_order, created = Order_Model.objects.prefetch_related('order_detail_set').get_or_create(
            User=request.user, is_paid=False)

        current_order.refresh_from_db()


        Detail = Order_detail.objects.filter(order=current_order, pk=product_id).first()


        if Detail is None:
            return JsonResponse({
                'status': 'error',
                'message': 'محصول مورد نظر سافت نشد'
            })

        if newCount == 'up':
            Detail.count += 1
            Detail.save()
            return JsonResponse({
                'status': 'success',
                'message': 'تعداد با موفقیت افزایش یافت',
                'data': render_to_string('order_partials/order_rm_partials.html', context={
                    'Order': current_order,
                    'total_price': current_order.calculate_total_price,
                })
            })
        else:
            if Detail.count == 1:
                Detail.delete()
                return JsonResponse({
                    'status': 'success',
                    'data': render_to_string('order_partials/order_rm_partials.html', context={
                        'Order': current_order,
                        'total_price': current_order.calculate_total_price,
                    })
            })
            else:
                Detail.count -= 1
                Detail.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'تعداد با موفقیت کاهش یافت',
                    'data': render_to_string('order_partials/order_rm_partials.html', context={
                        'Order': current_order,
                        'total_price': current_order.calculate_total_price,
                    })
                })
