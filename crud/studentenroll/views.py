from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#This function do for Add and show
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            ps = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            form.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': form, 'stu': stud})

#Update method
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


#This function work for delete
def delete_data(request, id):
    if request.method == 'POST':
        dm = User.objects.get(pk=id)
        dm.delete()
        return HttpResponseRedirect('/')

