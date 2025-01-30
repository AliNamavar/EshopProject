from django import forms
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'about_user',)
        # exclude = ('created_at', 'updated_at') on hayi ke nemikhay
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'درباره ی شما',
                'rows': 6,

            })

        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'عکس پروفایل',
            'about_user': 'درباره ی شما',
        }


class ChangePasswordForm(forms.Form):
    correct_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='پسوورد فعلی'
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='پسوورد جدید'
    )

    Repeat_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='تکرار پسوورد جدید'
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = self.cleaned_data.get('new_password')
        correct_password = self.cleaned_data.get('Repeat_new_password')
        if new_password != correct_password:
            self.add_error('Repeat_new_password', 'پسوورد جدید و تکرار آن مطابقت ندارند.')
        return cleaned_data