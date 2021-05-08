from django import forms
from tinymce import TinyMCE


class MyForm(forms.Form):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 700}))