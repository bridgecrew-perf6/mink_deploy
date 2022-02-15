from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['username'].label = '아이디'
        self.fields['profile_img'].widget.attrs['accept'] = 'image/png, image/gif, image/jpeg, image/jpg'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'name', 'gender', 'password1', 'password2',  'nickname', 'profile_img']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email

class FindUsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True

    class Meta:
        model = User
        fields = ['name', 'email']
