import requests

from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#the view that i want to require login just put the @login_required tag.

# Create your views here.
def index(request):
    info_list = models.info.objects.all().order_by('-date')
    return_dict = {"info_list":info_list}
    return render(request,"messenger_app/homepage.html",context=return_dict)

def about(request):
    return render(request,"messenger_app/about.html")

def reg_success(request):
    return render(request,"messenger_app/reg_success.html")

def student_register(request):
    student_register_form = forms.student_register_form()
    if(request.method == "POST"):
        student_register_form = forms.student_register_form(request.POST)
        if(student_register_form.is_valid()):
            student_register_form = forms.student_register_form(request.POST)
            student_register_form.save(commit=True)
            return render(request,"messenger_app/reg_success.html")

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
                return(HttpResponseRedirect(reverse(create_post)))

            else:
                return HttpResponse("Your account is not active!")
        else:
            return HttpResponse("Please recheck the details you have supplied either they are wrong or you are not registered")

    else:
        return render(request,"messenger_app/login.html")

def send_sms(phone,text):
    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers={}".format(text,phone)

    headers = {
    'authorization': "BR6gtTay8dxMOQV7EbW5HC3FkIGrPwS9jLiuKJANU4vXZfDqhsIo9PptBGHvXU1dkYCbmOKewqWA2MZL",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    # if __name__ == '__main__':
    #     print(response.text)


def create_post(request):
    form = forms.create_post_form()

    if(request.method == "POST"):
        form = forms.create_post_form(request.POST)
        if(form.is_valid()):
            #authenticate the user
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if(user):
                #filled the one to one field
                form.user = user

                #commit it to databse
                form.save(commit="True")
                if(form.cleaned_data["send_as_message"]):
                    students = models.student.objects.all()
                    for s in students:
                        send_sms(s.phone_no,form.cleaned_data["information"])
                    #it will be displayed on the homepage and the user will be returned to the homepages
                return HttpResponseRedirect(reverse("index"))

            else:
                return HttpResponse("Maybe you entered username or password wrong,if the problem still persists after retrying contact the admin")
        else:
            return HttpResponse("The form you entered is Invalid!")

    return render(request,"messenger_app/create_post.html",{"create_post_form":form})
