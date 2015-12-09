from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Username")}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'maxlength': 60, 'class': 'form-control', 'placeholder': ("Email Address")}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Password")}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Confirm your password")}))

   


    def clean_email(self):
        try:
            user = User.objects.get(
                email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("Account already exists.")


    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match.")
        return self.cleaned_data


