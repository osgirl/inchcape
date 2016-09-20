# forms.py
from django import forms


class TOTPForm(forms.Form):
    token = forms.CharField(label='token', max_length=100)

