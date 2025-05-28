from django import forms
from .models import *


class UsersignupForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = "__all__"


class UpdateForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = [
            "firstname",
            "lastname",
            "username",
            "password",
            "state",
            "city",
            "mobile",
            "pphoto",
        ]


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title","desc","cate","notefile"]