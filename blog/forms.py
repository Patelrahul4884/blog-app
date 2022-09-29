from dataclasses import field
from django import forms
from .models import Comment

class BlogCommentForm(forms.ModelForm):
    content = forms.CharField(label='')
    class Meta:
        model=Comment
        fields=['content']