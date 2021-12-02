from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.
from apps.accounts.models import UserProfile


class NewUserForm(UserCreationForm):
    email = forms.EmailField()
    rut = forms.CharField(max_length=15, required=True)
    direccion = forms.CharField(max_length= 50, required=True)
    telefono = forms.CharField(max_length=15, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'rut','direccion','telefono','password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono', ]
