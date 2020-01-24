from django.shortcuts import render, redirect
from .models import Sai, Age
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    hl = Age.objects.all()
    return render( request,"index.html", {'ask':hl})
@login_required
def profiles(request):
    pk = Sai.objects.all()
    ag = request.POST.get('age')
    st = request.POST.get('state')
    gen = request.POST.get('gender')
    cit = request.POST.get('city')
    if gen:
        pk=pk.filter(gender=gen)
    if ag:
        pk=pk.filter(agee=ag)
    if st:
        pk = pk.filter(state=st)
    if cit:
        pk = pk.filter(city=cit)
    return render(request,"profiles.html", {'lk':pk})

def viewpro(request,id):
    sk=Sai.objects.get(id=id)
    return render(request,'viewprofile.html',{'sp':sk})

def step1(request):
    xx = Age.objects.all()
    return render(request, "step1.html",{'sk': xx})

def save(request):
    uid = request.POST.get('sai')
    fname = request.POST.get('fn')
    sname = request.POST.get('sn')
    phone = request.POST.get('mobile')
    mail = request.POST.get('mail')
    gen = request.POST.get('gen')
    ag = request.POST.get('a')
    kk = Age.objects.get(id= ag)
    city = request.POST.get('city')
    photo = request.FILES.get('myfiles[]')
    sta = request.POST.get('state')
    abt = request.POST.get('abou')
    if uid == '':
        ss = Sai(fname = fname, lname= sname, mob= phone, gender= gen, mail= mail, agee= kk, city=city,
                 image= photo, state = sta, about = abt)
        ss.save()
        return render(request, "step1.html")
    else:
        ke = Sai.objects.filter(id=uid).update(fname = fname, lname= sname, mob= phone, gender= gen, mail= mail,
                                               agee= kk, city=city, image= photo, state = sta, about = abt)
        return render(request, "index.html", {'ss': ke})

def edit(request,id):
    ex = Sai.objects.get(id=id)
    xx = Age.objects.all()
    return render(request, "step1.html", {'ss':ex,'sk': xx})
def delete(request,id):
    mp = Sai.objects.get(id=id)
    mp.delete()
    return redirect (step1)
def register(request):
    if request.method == 'POST':
        finame=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('Email')
        password1=request.POST.get('pwd')
        password2=request.POST.get('cpwd')
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect(index)
            else:
                user=User.objects.create_user(username=email,first_name=finame,last_name=lastname,email=email,password=password1)
                Log_User=authenticate(username=email,password=password1)
                auth.login(request,user)
                messages.success(request,'Form submited successfully...')
                return redirect(index)
        else:
            messages.error(request, 'username or password are not matching')
            return redirect(index)
    else:
        return render(request,'index.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'logout successfully')
    return redirect(index)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        raw_password=request.POST.get('password')
        user=auth.authenticate(username=username,password=raw_password)
        if user is not None:
            auth_login(request,User)
            messages.success(request,'login sucessfully')
            return redirect(index)
        else:
            messages.error(request,'Invalid credentials...')
            return redirect(index)
    else:
        return redirect(index)












