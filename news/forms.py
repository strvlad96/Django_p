from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'short_text', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'short_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата добавления'
            })
        }
