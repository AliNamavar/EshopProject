from django import forms
from django.core import validators


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label="ایمیل",
        validators=[validators.EmailValidator, validators.MaxLengthValidator(100)],
    )
    password = forms.CharField(widget=forms.PasswordInput(), label="پسوورد")

    Repeat_password = forms.CharField(
        widget=forms.PasswordInput(), label="تکرار پسوورد",
        validators=[validators.MinLengthValidator(8, "رمز عبور باید حداقل ۸ کاراکتر باشد")],
    )


    def clean_Repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("Repeat_password")
        if password != repeat_password:
            raise forms.ValidationError("پسوورد مغایرت دارد دباره امتحان کنید")

        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("رمز عبور باید شامل حداقل یک عدد باشد")

        if not any(char.isupper() for char in password):
            raise forms.ValidationError("رمز عبور باید شامل حداقل یک حرف بزرگ باشد")

        if not any(char in "!@#$%^&*()_+" for char in password):
            raise forms.ValidationError("رمز عبور باید شامل حداقل یک کاراکتر ویژه (!@#$%^&*()_+) باشد")

        return password


class Login(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label="ایمیل",
        validators=[validators.EmailValidator, validators.MaxLengthValidator(100)],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="پسوورد",
        validators=[validators.MaxLengthValidator(100)],
    )


class forgot_password(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label="ایمیل",
        validators=[validators.EmailValidator, validators.MaxLengthValidator(100)],
    )


class reset_password(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="پسوورد",
        validators=[validators.MaxLengthValidator(100)],
    )
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="تکرار پسوورد",
        validators=[validators.MaxLengthValidator(100)],
    )

    def clean_Repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("Repeat_password")
        if password == repeat_password:
            return repeat_password
        else:
            raise forms.ValidationError("پسوورد مغایرت دارد دباره امتحان کنید")
