from django import forms
from .models import Nursery

class ProForm(forms.ModelForm):
    class Meta:
        model = Nursery
        fields = "__all__"