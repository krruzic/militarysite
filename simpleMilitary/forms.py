from django import forms
from simpleMilitary.models import Person
from django.contrib.auth.models import User
class RegistrationForm(forms.Form):
    username = forms.CharField(label=u'SIN', max_length=9)
    password1 = forms.CharField(label=u'Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label=u'Password (Again)', widget=forms.PasswordInput())


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        #validate username
        personExists = Person.objects.filter(sin=username)
        userExists = User.objects.filter(username=username)
        if not personExists:
            raise forms.ValidationError("No Service person with inputted SIN")
        if userExists:
            raise forms.ValidationError("That SIN is already registered")
        #validate password
        if password1 != password2:
            raise forms.ValidationError("Your current and confirm password do not match.")

        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']