from django import forms
from .models import Contact


# class ContactForm(forms.Form):
#     full_name = forms.CharField(
#         max_length=200,
#         label='نام و نام خانوادگی',
#         error_messages={
#             'required': 'نام فیلد الزامی است'
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'نام و نام خانوادگی'
#
#         })
#     )
#
#     email = forms.EmailField(
#         label="ایمیل",
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'ایمیل'
#         })
#     )
#     title = forms.CharField(
#         label="عنوان",
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'عنوان'
#             })
#     )
#     message = forms.CharField(label="متن پیام", widget=forms.Textarea(attrs={
#         'placeholder': 'متن',
#         'class': 'form-control',
#         'id': 'message'
#     })
#                               )


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("full_name", "email", "title", "message")
        # exclude = ('created_at', 'updated_at') on hayi ke nemikhay
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "نام و نام خانوادگی"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "ایمیل"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "عنوان"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "متن پیام",
                    "id": "message",
                }
            ),
        }
        labels = {
            "full_name": "نام و نام خانوادگی",
            "email": "ایمیل",
            "title": "عنوان",
            "message": "متن پیام",
        }
        error_messages = {
            "full_name": {
                "required": "نام و نام خانوادگی الزامی است",
            },
            "email": {
                "required": "ایمیل الزامی میباشد",
            },
            "title": {
                "required": "عنوان الزامی میباشد",
            },
            "message": {"required": "متن پیام الزامی میباشد"},
        }
