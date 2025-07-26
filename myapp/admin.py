from django.contrib import admin
from .models import User,Teacher,Student,Announcement,Assignment,Notes,Student_submission

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(Notes)
admin.site.register(Student_submission)
