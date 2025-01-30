from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from .forms import EditProfileModelForm, ChangePasswordForm


# Create your views here.

class user_dashboard(TemplateView):
    template_name = 'user_panel_module/user_dashbord_page.html'


class editUserProfile(View):

    def get(self, request):
        correct_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=correct_user)
        context = {
            'form': edit_form,
            'correct_user': correct_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request):
        correct_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=correct_user)
        
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form,
            'correct_user': correct_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)



class ChangePasswordView(View):
    def get(self, request):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('correct_password')):
                current_user.set_password(form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login'))
            else:
                form.add_error(
                    'correct_password',
                    'کلمه ی عبور وارد شده اشتباه میباشد'
                )

        context = {
                'form': form
            }
        return render(request, 'user_panel_module/change_password_page.html', context)





def user_panel_menu_component(request):
    return render(request, 'component/user_panel_menu_component.html')
