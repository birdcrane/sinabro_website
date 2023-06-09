from django import forms
from django.core.exceptions import ObjectDoesNotExist

from member.models import BoardMember
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    # 입력받을 값 두개
    username = forms.CharField(error_messages={
        'required': '아이디를 입력하세요!'
    }, max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력하세요!'
    }, widget=forms.PasswordInput, max_length=100, label="비밀번호")

    # 처음 값이 들어왔다 는 검증 진행

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                member = BoardMember.objects.get(username=username)
            except ObjectDoesNotExist:
                self.add_error('username', '존재하지 않는 사용자입니다!')
                return

            if not check_password(password, member.password):
                self.add_error('password', '비밀번호가 다릅니다!')
            else:
                self.user_id = member.id
