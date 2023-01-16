from django import forms
from .models import Sample
from django.core.exceptions import ValidationError


class printform(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ['Name']

    # def clean(self):
    #     super(printform, self).clean
    #     Na = self.cleaned_data.get('Name')
    #     if Na[0] == '-':
    #         raise ValidationError("Do not start with -")
    #     return Na
