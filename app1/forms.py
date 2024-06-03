from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password


class UserRegister(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']
    
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s
    
class Login(forms.Form):
    username=forms.CharField(max_length=25)
    password=forms.CharField(widget=forms.PasswordInput())
    