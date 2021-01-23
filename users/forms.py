from django import forms
from . import models

class InputForm(forms.Form):
    num1 = forms.IntegerField(max_value=45,min_value=1)
    num2 = forms.IntegerField(max_value=45,min_value=1)
    num3 = forms.IntegerField(max_value=45,min_value=1)
    num4 = forms.IntegerField(max_value=45,min_value=1)
    num5 = forms.IntegerField(max_value=45,min_value=1)
    num6 = forms.IntegerField(max_value=45,min_value=1)

    def clean(self):
        s = set()
        for i in range(1,7):
            s.add(self.cleaned_data.get(f"num{i}"))
        if len(s) != 6:
            print("Not all numbers are distincts")
            self.add_error("num1", forms.ValidationError("Not all numbers are distincts"))
        for i in s:
            if type(i) != type(1):
                self.add_error("num1", forms.ValidationError("Numbers should be integer"))
            
            elif i<1 or i>45:
                self.add_error("num1", forms.ValidationError("Numbers should be between 1 and 45"))


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                print("here!!")
                return self.cleaned_data
            else:
                self.add_error("password",forms.ValidationError("Password Is Wrong"))
        except models.User.DoesNotExist:
            self.add_error("email",forms.ValidationError("User Does Not Exist"))


class SignUpForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = models.User.objects.get(email=email)
            raise forms.ValidationError("Email already Exists!")
        except models.User.DoesNotExist:
            return email
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password Confirmation Does Not match")
        else:
            return password


    def save(self):
        
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(email, email, password)
        user.save()