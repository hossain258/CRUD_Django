from django import forms
from first_app import models

class studentForm(forms.ModelForm):
    class Meta:
        model =models.Student
        fields = "__all__"
