from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def index(request):
    return render(request,"messenger_app/homepage.html")

def student_register(request):
    student_register_form = forms.student_register_form()
    if(request.method == "POST"):
        student_register_form = forms.student_register_form(request.POST)
        if(student_register_form.is_valid()):
            student_register_form = forms.student_register_form(request.POST)
            student_register_form.save(commit=True)
            return HttpResponse("Registered Successfully")

        else:
            return HttpResponse("Failed to Save!")

    return render(request,"messenger_app/student_register_page.html",{"student_register_form":student_register_form})
