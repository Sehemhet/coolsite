from django import forms
from .models import *

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=100, label='Имя',
#         widget=forms.TextInput(attrs={
#         'class':'form-input'
#     }))
#     slug = forms.SlugField(max_length=100, label='URL')
#     photo = forms.ImageField(required=False)
#     content = forms.CharField(label='Контент')
#     is_publish = forms.BooleanField(label='Публикация', initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='категория не выбрана')

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_publish', 'cat']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':60, 'rows':10}),
        }