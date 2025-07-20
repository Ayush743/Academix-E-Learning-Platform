from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Teacher,Student
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
import csv
from django.db.models import Q
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
        email=request.POST.get('email')
        password=request.POST.get('password')
        # not_hashed = User.objects.get(email=username)

        # if not not_hashed.password.startswith('pbkdf2'):
        #         not_hashed.set_password(password)
        #         not_hashed.save()
        user=authenticate(request,username=email,password=password)
        if(user is not None):
            login(request,user)
            if(user.roles=='student'):
                if( not user.fees_submitted):
                     return redirect('student_register')
                else:
                     return redirect('student_profile')
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
def student_profile(request):
    if request.user.roles != 'student':
        raise PermissionDenied 
    user=request.user
    student=Student.objects.get(user=user)
    pending_fees=110000-int(student.fees_amount)
    return render(request,'student_profile.html',{'student':student,'pending_fees':pending_fees})
@login_required
def admin_dashboard(request):
    if request.user.roles != 'admin':
        raise PermissionDenied 
    return render(request,'admin_dashboard.html',{'user':request.user})
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
    if request.method == "POST":
        operation = request.POST.get("operation")
        if operation == "add":
            return redirect("add_student")
        elif operation == "view":
            return redirect("view_student")
        elif operation == "update":
            return redirect("update_student")
        elif operation == "delete":
            return redirect("delete_student")
        else:
             return render(request,'student_management.html', {'error': 'Please select a valid operation'})
    
    return render(request,'student_management.html')


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

def add_student(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        passsword=request.POST.get('password')
        section=request.POST.get('section')
        amount=request.POST.get('amount')
        phone=request.POST.get('phone')
        branch=request.POST.get('branch')
        attendance=request.POST.get('year')
       
        if(User.objects.filter(email=email).exists()):
            return render(request,'admin_student_insert.html',{'error': 'User already exists'})
        user=User.objects.create_user(
            email=email,
            username=email,
            password=passsword,
            name=name,
            roles='student',
            fees_submitted=True
        )
        student=Student.objects.create(
            user=user,
            section=section,
            branch=branch,
            attendance=attendance,
            fees_amount=amount,
            phone_num=phone

        )
        if student :
              return render(request,'admin_student_insert.html',{'message':'Student added successfully.'})
        else:
              return render(request,'admin_student_insert.html',{'error':'Student creation failed.'})
    return render(request,'admin_student_insert.html')

def view_teacher(request):
    department=request.GET.get('department')
    query=request.GET.get('search')
    teacher=Teacher.objects.all()
    if(department):
        teacher=teacher.filter(department=department)
        return render(request,'view_teacher.html',{'teachers':teacher})
    if(query):
        teacher=teacher.filter(
            Q(user__name__icontains=query)|
            Q(user__email__icontains=query)|
            Q(subject__icontains=query)|
            Q(salary_per_month__icontains=query)
        )
        return render(request,'view_teacher.html',{'teachers':teacher})
    return render(request,'view_teacher.html',{'error':'something went wrong'})
        
def view_student(request):
    branch=request.GET.get('branch')
    section=request.GET.get('section')
    query=request.GET.get('search')
    student=Student.objects.all()
    if(branch and section):
        student=student.filter(
                Q(branch__icontains=branch) &
                Q(section__icontains=section)
        )
        return render(request,'student_view.html',{'students':student})
    if(branch):
        student=student.filter(branch=branch)
        return render(request,'student_view.html',{'students':student})
    print(section,branch)

    if(query):
        student=student.filter(
            Q(user__name__icontains=query)|
            Q(user__email__icontains=query)
        )
        return render(request,'student_view.html',{'students':student})
    return render(request,'student_view.html',{'error':'something went wrong'})
        
    
def upload_csv(request):
    if(request.method=='POST'):
        csv_file=request.FILES.get('csv_file')
        if( not csv_file.name.endswith('.csv')):
               return render(request,'upload_csv.html',{'Error':'Pls upload in csv format'})
        decoded_file=csv_file.read().decode('utf-8').splitlines()
        file=csv.DictReader(decoded_file)
        for row in file:
                name = row['name']    
                email = row['email']     
                password = row['password']
                department = row['department']
                subject = row['subject']
                section = row['section']
                salary = row['salary']
                user=User.objects.create_user(
                    name=name,
                    email=email,
                    username=email,
                    password=password,
                    roles='teacher'

                )
                Teacher.objects.create(
                    user=user,
                    department=department,
                    salary_per_month=salary,
                    subject=subject,
                    section=section
                )
        return render(request, 'admin_add_teacher.html', {'message': 'CSV data uploaded successfully!'})
            

    return render(request,'upload_csv.html')
def student_csv(request):
    if(request.method=='POST'):
        csv_file=request.FILES.get('csv_file')
        if( not csv_file.name.endswith('.csv')):
               return render(request,'admin_student_csv.html',{'Error':'Pls upload in csv format'})
        decoded_file=csv_file.read().decode('utf-8').splitlines()
        file=csv.DictReader(decoded_file)
        for row in file:
                name = row['name']    
                email = row['email']     
                password = row['password']
                branch = row['department']
                year = row['year']
                amount = row['amount']
                section = row['section']
                phone=row['phone']
                marks=row['marks_percentage']
                attendance=row['attendance_percentage']
    
                user=User.objects.create_user(
                    name=name,
                    email=email,
                    username=email,
                    password=password,
                    roles='student',
                    fees_submitted=True

                )
                Student.objects.create(
                    user=user,
                    branch=branch,
                    phone_num=phone,
                    marks=marks,
                    attendance=attendance,
                    year=year,
                    fees_amount=amount,
                    section=section
                )
        return render(request, 'admin_add_teacher.html', {'message': 'CSV data uploaded successfully!'})
            

    return render(request,'admin_student_csv.html')

def delete_teacher(request):
    if(request.method=='POST'):
        id=request.POST.get('query')
        if(User.objects.filter(email=id).exists()):
            user=get_object_or_404(User,email=id)
            user.delete()
            return render(request,'delete_teacher.html',{'Message':'Teacher deleted successfully.'})
        else:
            return render(request,'delete_teacher.html',{'Error':'Teacher not found.'})
    return render(request,'delete_teacher.html')
   
    
def update_teacher(request):
    if(request.method=='POST'):
            if 'search' in request.POST:
                email=request.POST.get('username')
                if(User.objects.filter(email=email).exists()):
                    user=User.objects.get(email=email)
                    teacher=Teacher.objects.get(user=user)
                    return render(request,'update_teacher.html',{'user':user,'teacher':teacher})
            if('update' in request.POST):
                email=request.POST.get('email')
                user=User.objects.filter(email=email).first()
                if not user:
                     return render(request, 'update_teacher.html', {'error': 'User not found'})
                teacher=Teacher.objects.filter(user=user).first()
                user.name=request.POST.get('name')
                password=request.POST.get('password')
                user.set_password(password)
                user.save()
                teacher.department=request.POST.get('department')
                teacher.section=request.POST.get('section')

                teacher.salary_per_month=request.POST.get('salary')
                teacher.save()
                return redirect('display',username=user.email)#,user_id=user.id)
    return render(request,'update_teacher.html',)
def display_updated_record(request,username):
    user=User.objects.get(username=username)
    teacher=Teacher.objects.get(user=user)
    return render(request,'display_updated_record.html',{'user':user,'teacher':teacher})


@login_required
def student_register(request):
    return render(request,'student_register.html')


@login_required
def student_live(request):
    return render(request,'student_live.html')
@login_required
def student_notes(request):
    return render(request,'student_notes.html')
@login_required
def student_assignment(request):
    return render(request,'student_assignment.html')
@login_required
def student_announcement(request):
    return render(request,'student_announcement.html')
@login_required
def student_fees(request):
    user=request.user
    if(request.method=='POST'):
        branch=request.POST.get('branch')
        amount=request.POST.get('amount')
        phone=request.POST.get('phone')
        print(phone)
        receipt=request.FILES['receipt']
        if(receipt):
            student=Student.objects.create(
                user=user,
                branch=branch,
                fees_amount=amount,
                receipt=receipt,
                phone_num=phone,
                registered=True

            )
            student.save()
            return redirect('success')
        else:
            return render(request,'student_fees_submit.html',{'error':"pls upload the fees receipt file"})
    return render(request,'student_fees_submit.html',{'user':user})


def success_page(request):
    user=request.user
    return render(request,'success.html',{'user':user})

def fees_management(request):
    marker=""
    message=""
    students=Student.objects.filter(registered=True)

    if(request.method=='POST'):
        email=request.POST.get('email')
        year=request.POST.get('year')
        section=request.POST.get('section')
        user = User.objects.get(email=email)
        student=Student.objects.get(user=user)
        student.section=section
        student.year=year
        student.save()
        user.fees_submitted=True
        user.save()
        message='student registered successfully'
        if(user.fees_submitted==True):
            marker='Registered'
    return render(request,'fees_management.html',{'students':students,'message':message,"marker":marker})