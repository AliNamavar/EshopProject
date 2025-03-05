from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from account_module.models import User
from product_module.models import product
from site_module.models import siteSettings, footerLink, footerLinkBox, slider
from utils.product_list_for_index_page import split_list

# Create your views here.


class HomeView(TemplateView):
    template_name = "home_module/index_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["sliders"] = slider.objects.filter(is_active=True)
        product_new = list(
            product.objects.filter(is_active=True, is_deleted=False).order_by("-id")[:8]
        )
        chuncked_product = split_list(product_new)
        context["new_product"] = chuncked_product

        product_visits = list(
            product.objects.filter(is_active=True, is_deleted=False)
            .annotate(visits_count=Count("productVisitCount"))
            .order_by("-visits_count")
        )[:12]
        product_visits_listed = split_list(product_visits)
        context["product_visits"] = product_visits_listed

        return context


def site_header_component(request):
    site_settings = siteSettings.objects.filter(is_main_setting=True).first()
    context = {
        "site_settings": site_settings,
        "query_search": request.GET.get("search", ""),
    }
    return render(request, "shared/site_header_component.html", context)


def site_footer_component(request):

    site_settings = siteSettings.objects.filter(is_main_setting=True).first()
    footerLinks = footerLinkBox.objects.all()

    context = {"site_settings": site_settings, "footerCategory": footerLinks}
    return render(request, "shared/site_footer_component.html", context)


class InfoView(TemplateView):
    template_name = "home_module/about_us_page.html"

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        site_settings: siteSettings = siteSettings.objects.filter(
            is_main_setting=True
        ).first()
        context["site_settings"] = site_settings
        return context

class checkAddress(View):
    def get(self, request):
        user = request.user
        context = {
            'user': user,
        }
        return render(request, 'home_module/check_address.html', context)

    def post(self, request):
        new_address = request.POST.get("address")
        if new_address:
            user: User = User.objects.get(id=request.user.id)
            print(new_address)
            if user:
                user.address = new_address
                user.save()
                return JsonResponse({
                    'status': 'success',
                    'text': 'wait for our paying complete',
                    'button': 'ok',
                    'icon': 'success',
                })


            return JsonResponse({"message": 'address does not exist'})

        return JsonResponse({
            'status': 'success',
            'text': 'wait for our paying complete',
            'button': 'ok',
            'icon': 'error',
        })
