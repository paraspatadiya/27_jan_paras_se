from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myapp.models import Blog, Category, Tag

# ================= ADMIN LOGIN =================
def adminlogin(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pas = request.POST['password']

        if unm == 'paras' and pas == 'paras@123':
            request.session['admin'] = unm
            return redirect('/adminapp/adminhome/')
        else:
            return render(request, 'adminlogin.html', {'error': 'Invalid credentials'})

    return render(request, 'adminlogin.html')


# ================= ADMIN HOME =================
def adminhome(request):
    if not request.session.get('admin'):
        return redirect('/adminapp/adminlogin/')

    blogs = Blog.objects.all().order_by('-created_at')
    users = User.objects.all()

    # ✅ CORRECT WAY (use models directly)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'adminhome.html', {
        'blogs': blogs,
        'users': users,
        'categories': categories,
        'tags': tags
    })


# ================= CHANGE PASSWORD =================
def changepassword(request, id):
    if not request.session.get('admin'):
        return redirect('/adminapp/adminlogin/')

    user = User.objects.get(id=id)

    if request.method == "POST":
        user.set_password(request.POST.get('password'))
        user.save()
        return redirect('/adminapp/adminhome/')

    return render(request, 'changepassword.html', {'u': user})


# ================= CATEGORY =================
def addcategory(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
    return redirect('/adminapp/adminhome/')


def deletecategory(request, id):
    Category.objects.filter(id=id).delete()
    return redirect('/adminapp/adminhome/')


# ================= TAG =================
def addtag(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Tag.objects.create(name=name)
    return redirect('/adminapp/adminhome/')


def deletetag(request, id):
    Tag.objects.filter(id=id).delete()
    return redirect('/adminapp/adminhome/')