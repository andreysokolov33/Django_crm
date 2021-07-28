from django import forms
from .models import Operator


class OperatorModelForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = (
            'fullname',
            'login',
            'password',
            'nds',
            'proc',
        )


class OperatorForm(forms.Form):
    fullname = forms.CharField()
    login = forms.CharField()
    password = forms.CharField()
    nds = forms.IntegerField()
    proc = forms.IntegerField()
