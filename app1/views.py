from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import  FileForm
from .models import File
import os
from django.urls import reverse_lazy
from django.conf import settings
from django.http import HttpResponseNotFound
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')


def HomePage(request):
    return render (request,'home.html')


    
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

class MyPasswordResetView(PasswordResetView):
    email_template_name = 'my_app/password_reset_email.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    subject_template_name = 'my_app/password_reset_subject.txt'

def LogoutPage(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj})
            
    else:
        form = FileForm()
    files = File.objects.filter(user=request.user)
    return render(request, "index.html", {"files": files, "form": form})

def delete_file(request, file_id):
    try:
        file = File.objects.get(id=file_id)
    except File.DoesNotExist:
        return HttpResponseNotFound("File not found")
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.file))
    if os.path.isfile(file_path):
        os.remove(file_path)
        file.delete()
        return redirect('upload')
    else:
        return HttpResponseNotFound("File not found")
    
