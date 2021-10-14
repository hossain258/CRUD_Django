from django.shortcuts import render
from first_app import forms
from first_app.models import Student


# Create your views here.
def index(request):
    student_list =Student.objects.order_by("first_name")
    diction = {'title':'index','student_list':student_list}
    return render(request,'first_app/index.html',context = diction)

def student_form(request):
    form=forms.studentForm()  
    
    if request.method =="POST":
        form=forms.studentForm(request.POST)
        
        if form.is_valid():
            form.save(commit = True)
            return render(request,'first_app/message.html')
    diction = {'title' :'student_form',"student_form":form}
    return render(request,'first_app/student_form.html',context = diction)

def student_info(request,student_id):
    student_info =Student.objects.get(pk =student_id)
    diction = {'title':'student_info','student_info': student_info}
    return render(request,'first_app/student_info.html',context = diction)
