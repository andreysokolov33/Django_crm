from django import forms
from .models import Operator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()

class OperatorModelForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = (
            'fullname',
            'login',
            'password',
            'nds',
            'proc',
				'sogl_date'
        )


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username',)
		field_classes = {'username': UsernameField}

# class OperatorForm(forms.Form):
#     fullname = forms.CharField()
#     login = forms.CharField()
#     password = forms.CharField()
#     nds = forms.IntegerField()
#     proc = forms.IntegerField()
