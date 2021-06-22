from django import forms
from django.db.models import query
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

