from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, BlogForm
from .models import Blog, Like, Comment, Follow, Category, Tag

# --- RBAC Helpers ---
def is_author(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def is_admin(user):
    return user.is_authenticated and user.is_superuser

# --- Signup & Login ---
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    error = ""
    if request.method == 'POST':
        unm = request.POST.get('username')
        pas = request.POST.get('password')
        user = authenticate(request, username=unm, password=pas)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password"
    return render(request, 'login.html', {'error': error})


def userlogout(request):
    auth_logout(request)
    return redirect('login')



# --- Home ---
def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Filters
    author = request.GET.get('author')
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if author:
        blogs = blogs.filter(user__username__icontains=author)
    if category_id:
        blogs = blogs.filter(category_id=category_id)
    if tag_id:
        blogs = blogs.filter(tag_id=tag_id)
    if start_date and end_date:
        blogs = blogs.filter(created_at__date__range=[start_date, end_date])

    followed_users = []
    if request.user.is_authenticated:
        followed_users = Follow.objects.filter(follower=request.user)\
                                       .values_list('following_id', flat=True)

    return render(request, 'home.html', {
        'blogs': blogs,
        'followed_users': followed_users,
        'categories': categories,
        'tags': tags
    })

# --- Create Blog ---
@login_required
def createblog(request):
    msg = ''
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        tag_id = request.POST.get('tag')
        image = request.FILES.get('image')

        if not category_id or not tag_id:
            msg = "Please select category and tag"
        else:
            try:
                Blog.objects.create(
                    title=title,
                    content=content,
                    category_id=int(category_id),
                    tag_id=int(tag_id),
                    image=image,
                    user=request.user
                )
                return redirect('/')
            except Exception as e:
                msg = f"Error saving blog: {e}"

    return render(request, 'createblog.html', {
        'categories': categories,
        'tags': tags,
        'msg': msg
    })

# --- Edit Blog ---
@login_required
def editblog(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    # Permission: Owner or Admin
    if blog.user != request.user and not request.user.is_superuser:
        return redirect('/')

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.category_id = request.POST.get('category')
        blog.tag_id = request.POST.get('tag')

        if request.FILES.get('image'):
            blog.image = request.FILES['image']

        blog.save()
        return redirect('/myblogs/')

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'editblog.html', {
        'blog': blog,
        'categories': categories,
        'tags': tags
    })

# --- Delete Blog ---
@login_required
def deleteblog(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    # Permission: Owner or Admin
    if blog.user == request.user or request.user.is_superuser:
        blog.delete()
        return redirect('/myblogs/')
    
    return redirect('/')

# --- Read / Like / Comment / Follow ---
def readblog(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(blog=blog).order_by('-created_at')
    return render(request, 'readblog.html', {'blog': blog, 'comments': comments})


@login_required
def like(request, id):
    blog = get_object_or_404(Blog, id=id)
    like_obj = Like.objects.filter(user=request.user, blog=blog).first()
    if like_obj:
        like_obj.delete()
    else:
        Like.objects.create(user=request.user, blog=blog)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def comment(request, id):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                user=request.user,
                blog_id=id,
                text=text
            )
    return redirect(f'/read/{id}/')


@login_required
def deletecomment(request, id):
    comment_obj = get_object_or_404(Comment, id=id)
    # Permission: Owner of comment, Owner of blog, or Admin
    if comment_obj.user == request.user or comment_obj.blog.user == request.user or request.user.is_superuser:
        comment_obj.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def editcomment(request, id):
    comment_obj = get_object_or_404(Comment, id=id)
    if comment_obj.user != request.user and not request.user.is_superuser:
        return redirect('/')
        
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            comment_obj.text = text
            comment_obj.save()
        return redirect(f'/read/{comment_obj.blog.id}/')
    
    return render(request, 'editcomment.html', {'comment': comment_obj})



@login_required
def follow(request, id):
    target_user = get_object_or_404(User, id=id)
    if request.user == target_user:
        return redirect('/')
        
    follow_obj = Follow.objects.filter(follower=request.user, following=target_user).first()
    if follow_obj:
        follow_obj.delete()
    else:
        Follow.objects.create(follower=request.user, following=target_user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def myblogs(request):
    blogs = Blog.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'myblogs.html', {'blogs': blogs})