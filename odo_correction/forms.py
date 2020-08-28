from django import forms
from .models import Excel

class ExcleForm(forms.ModelForm):
    class Meta:
        model = Excel
        fields = ('country','file')