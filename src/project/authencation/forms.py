from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
  

    def clean(self):        
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')        
        print("{user} {passwd}".format(user=username, passwd=password))
        if not (username and password):
            # Don't authenticate, just let the other validators handle it.
            return self.cleaned_data

        try:
            self.user_cache = authenticate(
                username=username,
                password=password)            
        except exceptions.KeystoneAuthException as exc:            
            raise forms.ValidationError(exc)        
        return self.cleaned_data