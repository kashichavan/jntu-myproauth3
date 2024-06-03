from django.shortcuts import redirect,render
from .forms import User,UserRegister,Login
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        user=User.objects.filter(username=request.POST['username'])
        if user.exists():
            messages.info(request,'User Already exist')
            return redirect('/register/')
        form=UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        form=Login(request.POST)
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user:
                login(request,user)
                return redirect('/home/')
            else:
                messages.info(request,'Invalid username or password')
                return redirect('/login/')
    return render(request,'login.html')

@login_required(login_url='app1:login')
def home(request):
    return render(request,'home.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')
