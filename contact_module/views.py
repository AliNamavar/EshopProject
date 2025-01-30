from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from site_module.models import siteSettings
from .forms import ContactModelForm
from django.views import View
from django.views.generic.edit import FormView, CreateView
from .models import Contact, CreateProfile


# Create your views here.
class ContactView(CreateView):
    # model = Contact
    # fields = ['title', 'email', 'full_name', 'message']
    form_class = ContactModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        site_settings: siteSettings = siteSettings.objects.filter(is_main_setting=True).first()
        context['site_settings'] = site_settings
        return context
class CreateProfileView(CreateView):
    template_name = 'contact_module/create_pprofile.html'
    model = CreateProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


# class ContactView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactModelForm
#     success_url = '/contact-us'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ProfileView(ListView):
#     template_name = 'contact_module/prifile_list_page.html'
#     model = CreateProfile
#     context_object_name = 'profiles'
