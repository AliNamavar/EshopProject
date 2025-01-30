from django.shortcuts import render, redirect
from django.views import View
from .models import User
from account_module.forms import RegisterForm, Login, forgot_password, reset_password
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import login, logout
from utils.email_service import send_email
from django.contrib import messages
# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
                return render(request, 'account_module/register.html', {
                    'register_form': register_form
                })
            else:
                new_user = User(
                    username=user_email,
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()
                send_email(
                    'فعالسازی اکانت در فروشگاه',
                    to=new_user.email,
                    context={'user': new_user},
                    template_name='emails/active_account.html')
                messages.success(request, 'لینک فعالسازی به ایمیل شما ارسال شد. لطفاً ایمیل خود را بررسی کنید.')
                return redirect(reverse('login'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = Login()

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = Login(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email').lower()
            password = login_form.cleaned_data.get('password').lower()
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده')
                    return render(request, 'account_module/login.html', {
                        'login_form': login_form
                    })

                else:
                    is_password_correct = user.check_password(password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('index_home_module'))
                    else:
                        login_form.add_error('email', 'کاربر یافت نشد')
            else:
                login_form.add_error('email', 'ایمیل وارد شده صحیح نیست')
                return render(request, 'account_module/login.html', {
                    'login_form': login_form
                })

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class activate_accountView(View):
    def get(self, request, email_activate_code):
        user: User = User.objects.filter(email_active_code__iexact=email_activate_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login'))
            else:
                pass
        raise Http404


class forgot_passwordView(View):
    def get(self, request):
        forgot_password_context = forgot_password()
        return render(request, 'account_module/forgot_password.html', {
            'forgot_form': forgot_password_context
        })

    def post(self, request):
        forgot_password_context = forgot_password(request.POST)
        if forgot_password_context.is_valid():
            user_email = forgot_password_context.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email(
                    'بازیابی پسوورد اکانت در فروشگاه',
                    to=user.email,
                    context={'user': user},
                    template_name='emails/forgot_password.html')
                return redirect(reverse('login'))

        return render(request, 'account_module/forgot_password.html', {
            'forgot_form': forgot_password_context
        })


class forgot_passwordConfirmView(View):
    def get(self, request, confirmation_code):
        user: User = User.objects.filter(email_active_code__iexact= confirmation_code).first()
        if user is None:
            return redirect(reverse('login'))

        reset_password_context = reset_password()
        context = {
            'reset_password_context': reset_password_context,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request, confirmation_code):
        reset_password_context = reset_password(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=confirmation_code).first()
        if reset_password_context.is_valid():
            if user is None:
                return redirect(reverse('login'))
            new_pass_user = reset_password_context.cleaned_data.get('password')
            user.set_password(new_pass_user)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login'))
        reset_password_context = reset_password()
        context = {
            'reset_password_context': reset_password_context,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)


class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))