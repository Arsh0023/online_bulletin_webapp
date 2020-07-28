from django import forms
from django.core import validators
from messenger_app import models


#create forms here
class student_register_form(forms.ModelForm):

    class Meta:
        model = models.student
        fields = "__all__"
