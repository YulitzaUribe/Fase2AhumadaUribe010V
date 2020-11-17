from django import forms

from . models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titulo',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    content = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Post
        fields = ('title', 'content',)

