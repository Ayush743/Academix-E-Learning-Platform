from django.contrib import admin
from django.urls import path
from .views import signup,login_view,student_main,teacher_main,registrar_main,admin_dashboard,admin_announcement,admin_live,student_management,teacher_management,course_management,add_teacher,view_teacher,upload_csv,delete_teacher,update_teacher,display_updated_record
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',login_view,name='login'),
    path('student_main/',student_main,name='student_main'),
    path('teacher_main/',teacher_main,name='teacher_main'),
    path('registrar_main/',registrar_main,name='registrar_main'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('admin_announcement/',admin_announcement,name='announcement'),
    path('admin_live_class/',admin_live,name='admin_live'),
    path('student_management/',student_management,name='student_management'),
    path('teacher_management/',teacher_management,name='teacher_management'),
    path('course_management/',course_management,name='course_management'),
    path('add_teacher/',add_teacher,name='add_teacher'),
    path('delete_teacher/',delete_teacher,name='delete_teacher'),
    path('update_teacher/',update_teacher,name='update_teacher'),
    path('display_update_teacher/<str:username>/',display_updated_record,name='display'),

    path('view_teacher/',view_teacher,name='view_teacher'),
    path('upload_csv/',upload_csv,name='upload_csv'),
  
]