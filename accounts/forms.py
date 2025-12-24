from django import forms


class LoginForm(forms.Form):
    """ class defines the form for login creds """

    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    