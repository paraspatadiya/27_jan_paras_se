from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pas = request.POST['password']
        
        if unm == 'paras' and pas == 'paras123':
            request.session['admin'] = unm
            return redirect('admin_home')
        else:
            return render(request, 'admin_login.html', {'error': 'Login Failed'})
    
    return render(request, 'admin_login.html')


def admin_home(request):
    if 'admin' not in request.session:
        return redirect('admin_login')   # 🔒 protect page

    return render(request, 'admin_home.html')


def admin_logout(request):
    request.session.flush()   # simple logout
    return redirect('admin_login')

def add_doctor(request):
    if 'admin' not in request.session:
        return redirect('admin_login')

    if request.method == 'POST':
        doctor.objects.create(
            firstname=request.POST['firstname'],
            password=request.POST['password'],
            hospital=request.POST['hospital'],
            specialization=request.POST['specialization'],
            mobile=request.POST['mobile'],
            experience=request.POST['experience']
        )
        return redirect('view_doctors')

    return render(request, 'add_doctor.html')

def view_doctors(request):
    if 'admin' not in request.session:
        return redirect('admin_login')

    data = doctor.objects.all()
    return render(request, 'view_doctors.html', {'data': data})

def update_doctor(request, id):
    if 'admin' not in request.session:
        return redirect('admin_login')

    data = doctor.objects.get(id=id)

    if request.method == 'POST':
        data.firstname = request.POST['firstname']
        data.password = request.POST['password']
        data.hospital = request.POST['hospital']
        data.specialization = request.POST['specialization']
        data.mobile = request.POST['mobile']
        data.experience = request.POST['experience']
        data.save()

        return redirect('view_doctors')

    return render(request, 'edit_doctor.html', {'data': data})

def delete_doctor(request, id):
    if 'admin' not in request.session:
        return redirect('admin_login')

    data = doctor.objects.get(id=id)  
    data.delete()
    return redirect('view_doctors')