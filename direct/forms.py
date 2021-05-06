from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


    #本登録していないメールアドレスがあった場合消去する
    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email


#country = CountryField(blank_label='(Select country)',).formfield()

class ProfileForm(forms.ModelForm):
    """プロフィール登録フォーム"""
    class Meta:
        model = Profile
        fields = (
            "username", "age", "sex","country"
        )

        def __init__(self, *args, **kwargs):
            super(RegisterFormTeacher, self).__init__(*args, **kwargs)
            self.fields['country'].widget.attrs['placeholder'] = 'Select a Country'