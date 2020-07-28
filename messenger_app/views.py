from django.shortcuts import render
from django.http import HttpResponse
from . import forms


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#the view that i want to require login just put the @login_required tag.

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

def user_login(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if(user):
            if(user.is_active):
                login(request,user)
                return(HttpResponseRedirect(reverse("messenger_app:create_post")))

            else:
                return HttpResponse("Your account is not active!")
        else:
            return HttpResponse("Please recheck the details you have supplied either they are wrong or you are not registered")

    else:
        return render(request,"messenger_app/login.html")

@login_required
def create_post(request):
    return render(request,"messenger_app/create_post.html")
