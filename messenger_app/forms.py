from django import forms
from django.core import validators
from messenger_app import models


#create forms here
class student_register_form(forms.ModelForm):
    class Meta:
        model = models.student
        fields = "__all__"

class create_post_form(forms.ModelForm):
    username = forms.CharField(max_length=264)
    password = forms.CharField(widget=forms.PasswordInput)
    send_as_message = forms.BooleanField(label="Send as message",required=False)

    class Meta:
        model = models.info
        fields = "__all__"
        widgets = {"information":forms.Textarea(),}#"user":forms.HiddenInput
        labels = {
            'stream':'For Stream',
            'year':'For Year'
        }
