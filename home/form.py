from django import forms
from froala_editor.fields import FroalaField
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content', 'image']