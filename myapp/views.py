from django.shortcuts import render,redirect
from .models import User,Teacher
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
# Create your views here.
def signup(request):
    if(request.method=='POST'):
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']
        if(password!=confirm):
            return render(request,'signup.html',{'error':'Passwords do not match'})
        if(User.objects.filter(email=email).exists()):
            return render(request,'signup.html',{'error':'User already exists'})
        user =User.objects.create_user(
            name=username,
            username=email,
            email=email,
            password=password,
            roles='student'  
        )
        return redirect('login')

    return render(request,'signup.html')


def login_view(request):
    if(request.method=='POST'):
        username=request.POST.get('email')
        password=request.POST.get('password')
        not_hashed = User.objects.get(email=username)

        if not not_hashed.password.startswith('pbkdf2'):
                not_hashed.set_password(password)
                not_hashed.save()
        user=authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            if(user.roles=='student'):
                return redirect('student_main')
            elif(user.roles=='teacher'):
                return redirect('teacher_main')
            elif(user.roles=='registrar'):
                return redirect('registrar_main')
            elif(user.roles=='admin'):
                return redirect('admin_dashboard')
            else:
                return render(request,'index.html',{'error':'Invalid Role'})
        else:
                return render(request,'index.html',{'error':'Invalid username or password'})

            
    return render(request,'index.html')
@login_required
def student_main(request):
    if request.user.roles != 'student':
        raise PermissionDenied 
    return render(request,'student.html')
@login_required
def admin_dashboard(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    return render(request,'admin_dashboard.html')
@login_required
def teacher_main(request):
    if request.user.roles != 'teacher':
        raise PermissionDenied 
    return render(request,'teacher.html')
@login_required
def registrar_main(request):
    if request.user.roles != 'registrar':
        raise PermissionDenied 
    return render(request,'registrar.html')
@login_required
def admin_announcement(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    return render(request,'admin_announcement.html')
@login_required
def admin_live(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    return render(request,'admin_join_live.html')
@login_required
def student_management(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    return render(request,'student_management.html')
@login_required
def course_management(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    return render(request,'course_management.html')
@login_required
def teacher_management(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    if request.method == "POST":
        operation = request.POST.get("operation")
        if operation == "add":
            return redirect("add_teacher")
        elif operation == "view":
            return redirect("view_teacher")
        elif operation == "update":
            return redirect("update_teacher")
        elif operation == "delete":
            return redirect("delete_teacher")
        else:
             return render(request,'teacher_management.html', {'error': 'Please select a valid operation'})
    
    return render(request,'teacher_management.html')
@login_required
def add_teacher(request):
   
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        passsword=request.POST.get('password')
        salary=request.POST.get('salary')
        section=request.POST.get('section')
        department=request.POST.get('department')
        subject=request.POST.get('subject')
        phone_num=request.POST.get('phone')
        if(User.objects.filter(email=email).exists()):
            return render(request,'admin_add_teacher.html',{'error': 'User already exists'})
        user=User.objects.create_user(
            email=email,
            username=email,
            password=passsword,
            name=name,
            roles='teacher'
        )
        teacher=Teacher.objects.create(
            user=user,
            salary_per_month=salary,
            section=section,
            phone_num=phone_num,
            department=department,
            subject=subject

        )
        if teacher :
              return render(request,'admin_add_teacher.html',{'message':'Teacher added successfully.'})
        else:
              return render(request,'admin_add_teacher.html',{'error':'Teacher creation failed.'})
    return render(request,'admin_add_teacher.html')

def view_teacher(request):
    department=request.GET.get('department')
    teacher=Teacher.objects.all()
    if(department):
        teacher=teacher.filter(department=department)
    return render(request,'view_teacher.html',{'teachers':teacher})
