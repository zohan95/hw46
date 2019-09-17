from django import forms
from .models import Article

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['description', 'detail', 'status', 'date']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control inp', 'autofocus':'autofocus'}),
            'detail': forms.Textarea(attrs={'class': 'form-control inp', 'wrap': 'soft'}),
        }

class DeleteForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = []

