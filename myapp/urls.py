from django.contrib import admin
from django.urls import path
from .views import signup,login_view,student_main,teacher_main,registrar_main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signup,name='signup'),
    path('login/',login_view,name='login'),
    path('student_main/',student_main,name='student_main'),
    path('teacher_main/',teacher_main,name='teacher_main'),
    path('registrar_main/',registrar_main,name='registrar_main')
]