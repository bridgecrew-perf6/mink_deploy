from django import forms
from django_summernote.widgets import SummernoteWidget

from board.models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 사용할 모델
        fields = ['subject', 'content', 'tag']
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = '제목'
        self.fields['subject'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control t-my-3',
            'autofocus': True,
        })
        self.fields['tag'].label = '태그'
        self.fields['tag'].widget.attrs.update({
            'placeholder': '태그를 입력해주세요.   ex) #동물 #유머',
            'class': 'form-control t-my-3',
            'autofocus': True,
        })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 사용할 모델
        fields = ['content']