from django.contrib import admin
from django.urls import path
from .views import signup,login_view,student_profile,teacher_main,registrar_main,admin_dashboard,admin_announcement,admin_live,student_management,teacher_management,add_teacher,view_teacher,upload_csv,delete_teacher,update_teacher,display_updated_record,student_register,student_assignment,student_live,student_notes,student_announcement,student_fees,success_page,fees_management,add_student,student_csv,view_student
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',login_view,name='login'),
    path('student_profile/',student_profile,name='student_profile'),
    path('teacher_main/',teacher_main,name='teacher_main'),
    path('registrar_main/',registrar_main,name='registrar_main'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('admin_announcement/',admin_announcement,name='announcement'),
    path('admin_live_class/',admin_live,name='admin_live'),
    path('student_management/',student_management,name='student_management'),
    path('student_register/',student_register,name='student_register'),
    path('student_notes/',student_notes,name='student_notes'),
    path('student_live/',student_live,name='student_live'),
    path('student_fees/',student_fees,name='student_fees'),
    path('student_assignment/',student_assignment,name='student_assignment'),
    path('student_announcement/',student_announcement,name='student_announcement'),
    path('teacher_management/',teacher_management,name='teacher_management'),
    path('fees_management/',fees_management,name='fees_management'),
    path('add_teacher/',add_teacher,name='add_teacher'),
    path('add_student/',add_student,name='add_student'),
    path('student_csv/',student_csv,name='student_csv'),
    path('student_view/',view_student,name='view_student'),
    path('delete_teacher/',delete_teacher,name='delete_teacher'),
    path('update_teacher/',update_teacher,name='update_teacher'),
    path('display_update_teacher/<str:username>/',display_updated_record,name='display'),
    

    path('view_teacher/',view_teacher,name='view_teacher'),
    path('success/',success_page,name='success'),
    path('upload_csv/',upload_csv,name='upload_csv'),
  
]