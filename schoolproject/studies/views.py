from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.object_user(username=username, password=password)

            user.save();
            return redirect('login')
        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
def newpage(request):
    return render(request,'newpage.html')

def department(request,c_slug=None):
    c_page=None
    courses=None
    if c_slug!=None:
        c_page=get_object_or_404(Product,slug=c_slug)
        courses=Course.objects.all().filter(department=c_page,available=True)
    else:
        courses=Course.objects.all().filter(avaIlable=True)
    return render(request,'department.html')

def course(request,c_slug,course_slug):
    try:
        course=Course.objects.get(category__slug=c_slug,slug=course_slug)
    except Exception as e:
        raise e


    return render(request,'course.html',{'course':course})
