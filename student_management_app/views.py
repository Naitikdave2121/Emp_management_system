from django.db import connection
from django.utils import timezone
from django.shortcuts import render, redirect,HttpResponse
from django.db.models import Count, Case, When, Value, CharField
from.models import*
from datetime import datetime,date
from django.contrib import messages
from django.http import Http404
def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, "login.html")

#def registration(request):
 #   return render(request,"registration.html")

def regist(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        user=request.POST['user']
        email=request.POST['email']
        passs=request.POST['pass']

        if fname=="":
                    message="fname can not be blank"
                    return render(request,"registration.html",{'msg':message})
        if lname=="":
                    message="lname can not be blank"
                    return render(request,"registration.html",{'msg':message})
        if user=="":
                    message="Username can not be blank"
                    return render(request,"registration.html",{'msg':message})
        if email=="":
                    message="Email can not be blank"
                    return render(request,"registration.html",{'msg':message})
        if passs=="":
                    message="You Must Enter Password"
                    return render(request,"registration.html",{'msg':message})
        else:
                    Registration.objects.create(FirstName=fname,LastName=lname,username=user,Email=email,Password=passs)
                    return redirect('login')
    else:
            return render(request,"registration.html")
    
def sidebar1(request):
        return render(request,"hod_template/sidebar_template.html")

def admin(request):
        return render(request,"hod_template/admin_profile.html")

def b(request):
        return render(request,"hod_template/base_template.html")
def co(request):
        return render(request,"hod_template/add_course_template.html")



def entry(request):
        if request.POST['Role']=="Admin":
                email=request.POST['email']
                password=request.POST['password']
                a1=Registration.objects.get(Email=email,Password=password)
                if a1:
                        return redirect('admin_home')
        else:
                if request.POST['Role']=='Employee':
                  email=request.POST['email']
                  password=request.POST['password']
                  Emp_fetch=Employee.objects.get(Email=email,password=password)
                  if Emp_fetch:
                        if Emp_fetch.password==password:
                                request.session['Emp_Name']=Emp_fetch.Emp_Name
                                request.session['Email']=Emp_fetch.Email
                                request.session['id']=Emp_fetch.id
                                emp_id=Employee.objects.get(id=request.session['id'])
                                Attandance.objects.create(Emp_id=emp_id,Check_in=datetime.now())
                                return render(request,"Employee_template/Employee_profile.html")
                        else:
                                 messages.success(request,"data saved successfully")
                                 return redirect('login')       

def staff(request):
        return render(request,"hod_template/Add_Department.html")

def dept(request):
        all=Department.objects.all()
        return render(request,"hod_template/Manage_Dept.html",{'a':all})
def position(request):
               all_pos=Position.objects.all()
               return render(request,"hod_template/Add_Position.html",{'msg2':all_pos})
def manage(request):
        all=Position.objects.all()
        return render(request,"hod_template/Manage_Pos.html",{'a':all})
def empl(request): 
        all2=Position.objects.raw("SELECT * FROM student_management_app_position")
        all=Department.objects.all()
        return render(request,"hod_template/Add_Employee.html",{'msg1':all,'msg2':all2})

def manage_e(request):
        all_emp=Employee.objects.raw("SELECT * FROM student_management_app_employee e,student_management_app_department d WHERE d.id=e.Dept_id")
        return render(request,"hod_template/Manage_Emp.html",{'data':all_emp})

def manage_leave(request):
        QUery=Leave.objects.filter(status='pending')
        return render(request,"hod_template/Manage_Leave.html",{'re':QUery})


def notice(request):
        return render(request,"hod_template/add_notice.html")
def base(request):
        return render(request,"hod_template/base_template.html")
def department(request):
        if request.method=="POST":
                name=request.POST['name']
                desc=request.POST['desc']
                Department.objects.create(Dept_Name=name,Description=desc)
                messages.success(request,"data saved successfully")
                return redirect('st')
def delete_dep(request,pk):
        del_data=Department.objects.get(id=pk)
        del_data.delete()
        return redirect('department_manage')
def pos(request):
        if request.method=='POST':
                p_Name= request.POST['p_Name']
                desc= request.POST['desc']
                Position.objects.create(Pos_Name=p_Name,Description=desc)
                message="data added successfully"
                return render(request,"hod_template/Add_Position.html",{'msg':message})
def del_pos(request,pk):
        del_pos=Position.objects.get(id=pk)
        del_pos.delete()
        return redirect('position')

def position_m(request):
        pos_all=Position.objects.all()
        return render(request,"hod_template/Add_Employee.html",{'msg2':pos_all})
def addemployee(request):
        if request.method=='POST':
                name=request.POST['name']
                city=request.POST['city']
                add=request.POST['add']
                mno=request.POST['mno']
                sal=request.POST['sal']
                age=request.POST['age']
                dob=request.POST['dob']
                pass1=request.POST['pass']
                Dept_Name=request.POST['Dept_Name']
                email=request.POST['email']
                dept_get=Department.objects.get(id=Dept_Name)
                e1=Employee.objects.create(Emp_Name=name,City=city,Address=add,Mobileno=mno,Salary=sal,Age=age,Date_Of_Birth=dob,Dept=dept_get,password=pass1,Email=email)
                messages.success(request, "Data Saved SuccessFully ")
                return redirect('emp')
def delete(request,pk):
        d1=Employee.objects.get(id=pk)
        d1.delete()
        return redirect('manageemployee')
def task(request):
        if request.method=='POST':
                tname=request.POST['tname']
                desc=request.POST['desc']
                empname=request.POST['empname']
                stdate=request.POST['sdate']
                edate=request.POST['edate']

                emp_fetch=Employee.objects.get(Emp_Name=empname)
                if emp_fetch:
                        Task.objects.create(Emp_id=emp_fetch,Task_Name=tname,Description=desc,Start_Date=stdate,End_Date=edate)
                        messages.success(request, "Task send SuccessFully ")
                        return redirect('add-task')
                
                else:
                        messages.error(request,"Employee Does Not Found")
                        return redirect('add-task')
        else:
                return render(request,"hod_template/add_task.html")
        
def admin_home(request):
        return render(request,"hod_template/admin_profile.html")
def notice1(request):
        if request.method=='POST':
                name=request.POST['name']
                desc=request.POST['desc']
                Notice.objects.create(Notice_Name=name,Description=desc)
                messages.success(request, "Data Saved SuccessFully ")
                return redirect('not')
        
        else:           
                 return render(request,"hod_template/add_notice.html")

def departmentedit(request,pk):
        update_dept=Department.objects.get(id=pk)
        return render(request,"hod_template/edit_department.html",{'data':update_dept})
def deprtmentupdate(request,pk):
        update_final=Department.objects.get(id=pk)
        
        update_final.Dept_Name=request.POST['tname']
        update_final.Description=request.POST['desc']
        update_final.save()
        return redirect('department_manage')
def studentprofile(request):
        return render(request,"Employee_template/Employee_profile.html")

def leave_emp(request):
        alldata=Employee.objects.get(id=request.session['id'])
        all=Leave.objects.filter(Emp_id=alldata)
        return render(request,"Employee_template/Employee_leave.html",{'d':all})

def att(request):
        return render(request,"Employee_template/Employee_view_att.html")

def emp1l(request):
   if request.method=='POST':
        lm=request.POST['leave_message']
        stdate=request.POST['stdate']
        eddate=request.POST['eddate']
        Emp_id=Employee.objects.get(id=request.session['id'])
        insert_leave=Leave.objects.create(Emp_id=Emp_id,Reason=lm,Start_Date=stdate,End_Date=eddate)
        messages.success(request,"Leave Apply successfully")
        return redirect('leave-add')
   
def l_m(request,pk):
        sql=Leave.objects.get(id=pk)
        return render(request,"hod_template/view_leave.html",{'data':sql})
def app_leave1(request,pk):
       update_leave=Leave.objects.get(id=pk)
       update_leave.status="Approve"
       update_leave.save()
       return redirect('l-manage')
def reject(request,pk):
        delete_leave=Leave.objects.get(id=pk)
        delete_leave.status="Reject"
        delete_leave.save()
        return redirect('l-manage')
def emp_show(request,pk):
        Emp_data=Employee.objects.get(id=pk)
        return render(request,"hod_template/View_Employee.html",{'data1':Emp_data})

def t_m(request):
        emp_id=Task.objects.filter(Emp_id=request.session['id'],status="pending")
        return render(request,"Employee_template/Task_manage.html",{'d':emp_id})

def manage_task(request):
        if request.method=="POST":
                se=request.POST['se']
                all=Task.objects.filter(status=se)
                return render(request,"hod_template/manage_task.html",{'a':all})
        else:
                return render(request,"hod_template/manage_task.html")
        
def e(request):
    with connection.cursor() as cursor:
        cursor.execute('''
           SELECT id FROM student_management_app_employee WHERE id=2
        ''')
        leave_data = cursor.fetchall()
        return render(request,"index.html",{'l':leave_data})
    
def log(request):
        emp=Employee.objects.get(id=request.session['id'])
        attandane=Attandance.objects.filter(Emp_id=emp).order_by('Check_Out').first()
        
        if attandane:
                attandane.Check_Out=datetime.now()
                attandane.save()
        return redirect('login')

def att_report(request):
         return render(request,"hod_template/Attandance_view1.html")

def repreport(request):
        Current_Month = datetime.now().month
        report = Attandance.objects.filter(
            check_i=Current_Month
    ).values('Emp_id__Emp_Name').annotate(
        days_present=Count('Check_in', filter=models.Q(Check_in__isnull=False, Check_Out__isnull=False)),
        days_absent=Count('Check_in', filter=models.Q(Check_in__isnull=True) | models.Q(Check_Out__isnull=True)),
        total_days=Count('id'),
        status=Case(
            When(Check_in__isnull=False, Check_Out__isnull=False, then=Value('PRESENT')),
            default=Value('Absent'),
            output_field=CharField()
        )
    )
        return render(request,"hod_template/Attandance_report.html",{'report':report})
def yearly_reports(request):
        current_year = datetime.now().year
        report = Attandance.objects.filter(
            Check_in__year=current_year
    ).values('Emp_id__Emp_Name').annotate(
        days_present=Count('Check_in', filter=models.Q(Check_in__isnull=False, Check_Out__isnull=False)),
        days_absent=Count('Check_in', filter=models.Q(Check_in__isnull=True) | models.Q(Check_Out__isnull=True)),
        total_days=Count('id'),
        status=Case(
            When(Check_in__isnull=False, Check_Out__isnull=False, then=Value('PRESENT')),
            default=Value('Absent'),
            output_field=CharField()
        )
    )
        return render(request,"hod_template/Attandance_report.html",{'report':report})
def attandance_report(request): 
         query="SELECT e1.Emp_Name,a1.Check_in,a1.Check_Out FROM student_management_app_employee e1,student_management_app_attandance a1 WHERE e1.id=a1.Emp_id_id AND e1.id=session['id'] "
         with connection.cursor()as cursor:       
                 cursor.execute(query) 
                 result=cursor.fetchall()
                 return HttpResponse(result)
       
def notice(request):
        all_data=Notice.objects.all()
        return render(request,"Employee_template/view_notice.html",{'a':all_data})

def taskview(request,pk):
        all_data1=Task.objects.get(id=pk)
        return render(request,"Employee_template/Taskview.html",{'a2':all_data1});

def tcomplete(request,pk):
        update_id=Task.objects.get(id=pk)
        update_id.status="Complete"
        update_id.save()
        return redirect('Task-manage')
   
def updateeprofile(request):
        getdata=Employee.objects.get(id=request.session['id']);
        return render(request,"Employee_template/Employee_profile.html",{'d':getdata});

def empup(request, pk):
    try:
        getemp = Employee.objects.get(id=pk)
        empname = request.POST.get('empname', '')
        cty=request.POST.get('cty','')   
        add=request.POST.get('add','')   
        mno=request.POST.get('mno','')  
        age=request.POST.get('age','')
        email=request.POST.get('email','')
        # Use get() to access the value safely
        getemp.Emp_Name = empname
        getemp.City=cty
        getemp.Address=add
        getemp.Mobileno=mno
        getemp.Age=age 
        getemp.Email=email
        getemp.save()
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")
    
    return HttpResponse("data updated successfully")

def dash(request):
        total_employee=Employee.objects.count()
        return render(request,"Employee_template/dashboard.html",{'t':total_employee})

def t_task(request):
        total_task=Task.objects.count()
        return render(request,"Employee_template/dashboard.html",{'t_task':total_task})
def edit_emp(request,pk):
        emp_edit=Employee.objects.get(id=pk)
        emp_edit.Emp_Name=request.POST['empname']
        emp_edit.City=request.POST['ct']
        emp_edit.Address=request.POST['add']
        emp_edit.Mobileno=request.POST['mno']
        emp_edit.Salary=request.POST['sal']
        emp_edit.Email=request.POST['email'] 
        emp_edit.save()
        return redirect('manageemployee')

def p_task(request):
        data=Task.objects.filter(status='pending')
        return render(request,"hod_template/manage_task.html",{'d':data})

def completedtask(request):
        data1=Task.objects.filter(status="Complete")
        return render(request,"hod_template/manage_task.html",{'d1':data1})
        