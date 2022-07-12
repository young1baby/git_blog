from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 指定表单中要显示的内容
        fields = {'name', 'email', 'url', 'text'}