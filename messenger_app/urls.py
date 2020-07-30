from django.urls import path
from . import views
#setting the namespace
app_name = "messenger_app"
urlpatterns = [
path("",views.index,name="index"),
path("student_register/",views.student_register,name="student_register"),
path("login/",views.user_login,name="user_login"),
path("create_post/",views.create_post,name="create_post"),
path("about/",views.about,name="about")
# path("success/",views.reg_success,name="reg_success"),
]
