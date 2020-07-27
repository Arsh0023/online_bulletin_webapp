from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,"messenger_app/homepage.html")

def student_register(request):
    form = forms.student_register_form()
    # if(request.method == "POST"):
    #     student_register_form = forms.student_register_form(request.POST)
    return render(request,"messenger_app/student_register_page.html",{"student_register_form":form})
