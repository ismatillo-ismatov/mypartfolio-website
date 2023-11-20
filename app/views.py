from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.conf import settings
from .models import Post,Tag,Comment
from .forms import *
# Create your views here.

def home(request):
    posts = Post.objects.all()
    tag = Tag.objects.all()
    context = {'posts':posts,'tag':tag}
    return render(request,"base/index.html",context)



def post(request,slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        Comment.objects.create(
            auther=request.user.profile,
            post=post,
            body=request.POST['comment']
        )
        messages.success(request,"You're comment was successfuly posted!")
        return redirect('app:post',slug=post.slug)

    context = {'post':post}
    return render(request,'base/post.html',context)

def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'base/posts.html',context)

def profile(request):
    return render(request,'base/profile_form.html')

@login_required(login_url="home")
def userAccount(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request,'base/account.html',context)

@login_required(login_url="home")
def updateProfile(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
        
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('app:account')

    context = {'form':form}
    return render(request,'base/profile_form.html',context)


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })
        
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.Email_HOST_USER,
            ['ismatilloismatov1995@gmail.com']
        )
        email.fail_silently=False
        email.send()
    
    return render(request,'base/email_sent.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                User.objects.get(username=username)
                messages.error(request,'This username is already token')
            except User.DoesNotExist:
                user = form.save(commit=False)
                user.save()
            messages.success(request,'Account successfuly created')
            user = authenticate(request,username=user.username,password=request.POST['password1'])
            if user is not None:
                login(request,user)

        

            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'home'
            return redirect(next_url)
        else:
            messages.error(request,'an error has occured with registration')

    context = {"form":form}
    return render(request,'base/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('app:home')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request,username=user.username,password=password)
        except:
            messages.error(request,'User with this email does not exists')
            return redirect('app:login')
        
        if user is not None:
            login(request,user)
            return redirect('app:home')
        else:
            messages.error(request,'email or password is incorrect')
        
    
    context = {}
    return render(request,'base/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('app:home')


def updateProfile(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()

        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid:
            form.save()
            return redirect('app:account')
        
    
    context = {"form":form}
    return render(request,'base/profile_form.html',context)