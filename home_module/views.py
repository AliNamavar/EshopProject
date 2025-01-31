from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from product_module.models import product
from site_module.models import siteSettings, footerLink, footerLinkBox, slider
from utils.product_list_for_index_page import split_list

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = slider.objects.filter(is_active=True)
        product_new =  list(product.objects.filter(is_active=True, is_deleted=False).order_by('-id')[:8])
        chuncked_product = split_list(product_new)
        context['new_product'] = chuncked_product

        return context


def site_header_component(request):
    site_settings = siteSettings.objects.filter(is_main_setting=True).first()
    context = {
        'site_settings': site_settings
    }
    return render(request, "shared/site_header_component.html", context)


def site_footer_component(request):

    site_settings = siteSettings.objects.filter(is_main_setting=True).first()
    footerLinks = footerLinkBox.objects.all()


    context = {
        'site_settings': site_settings,
        'footerCategory': footerLinks

    }
    return render(request, "shared/site_footer_component.html", context)


class InfoView(TemplateView):
    template_name = 'home_module/about_us_page.html'


    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        site_settings: siteSettings = siteSettings.objects.filter(is_main_setting=True).first()
        context['site_settings'] = site_settings
        return context