from django import forms
from . import models
from users.models import User

class GalleryForm(forms.Form):

    name = forms.CharField()
    gallery_type = forms.ModelChoiceField(
            required=False,
            queryset= models.gallerytype.objects.all(),
            empty_label="nothing",
        )

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("password does not match"))
        except user.DoesNotExist:
            self.add_error("email", forms.ValidationError("email does not exists"))