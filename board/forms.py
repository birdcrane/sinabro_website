from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'contents', 'image']
        labels = {
            'title': '게시글 제목',
            'contents': '게시글 내용',
            'image': '이미지',
        }
        error_messages = {
            'title': {
                'required': '제목을 입력하세요.'
            },
            'contents': {
                'required': '내용을 입력하세요.'
            },
        }
