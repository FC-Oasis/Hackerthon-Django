from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    img_profile = forms.FileField(
        label='프로필 이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )
    introduce = forms.CharField(
        label='소개',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )

    def clean_username(self):
        # username field의 clean()실행 결과가 self.cleaned_data['username']에 있음
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError('이미 사용중인 아이디입니다')
        return data

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            self.add_error('password2', '비밀번호와 비밀번호확인의 값이 일치하지 않습니다')
        return self.cleaned_data

    def signup(self):
        fields = [
            'username',
            'email',
            'password',
            'img_profile',
            'introduce',
        ]
        create_user_dict = {}
        for key, value in self.cleaned_data.items():
            if key in fields:
                create_user_dict[key] = value

        def in_fields(item):
            return item[0] in fields

        result = filter(in_fields, self.cleaned_data.items())
        create_user_dict = {}
        for item in result:
            create_user_dict[item[0]] = item[1]

        # filter결과를 dict함수로 묶어서 새 dict생성
        create_user_dict = dict(filter(in_fields, self.cleaned_data.items()))
        user = User.objects.create_user(**create_user_dict)

        return user
