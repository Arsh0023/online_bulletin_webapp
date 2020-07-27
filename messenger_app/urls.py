from django.urls import path
from . import views

#setting the namespace
app_name = "messenger_app"

urlpatterns = [
path("student_register/",views.student_register,name="student_register")
]
