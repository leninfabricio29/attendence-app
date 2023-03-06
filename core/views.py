from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from .forms import Myform
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import  Attendence


@login_required
def ConsolePage(request):
    userLogged=request.user.id
    list_attendence=Attendence.objects.all()
    print(list_attendence)
    contexto = {
        'attendences': list_attendence
    }
    return render(request, 'attendence/index.html',contexto)


def WelcomePage(request):
    return render (request, 'attendence/welcome.html')

def HomePage(request):
    form = Myform(request.POST)
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=name, password=password)
        if form.is_valid():
            form = Myform()
            if user is not None:
                login(request, user)
                return redirect('console-page')
            else:
                messages.error(request, 'Error, credenciales inválidas')
        else:
            messages.error(request, 'Captcha Fallido, vuelve a repetir')

    return render(request, 'attendence/login.html', {'form':form})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        numeroCaracteres = len(password)

        if numeroCaracteres >= 8:
            list_Users = User.objects.all()
            for ale in list_Users:
                if ale.username == name:
                    messages.error(request,'Error, ya existe este username')
                    #Se borro llaves.
                    return render(request,'attendence/register.html')
                else:
                    print("Registro exitoso de "+name)
                    new_user = User.objects.create_user(name, email, password)
                    new_user.first_name = fname
                    new_user.last_name = lname
                    new_user.save()
                    return redirect('welcome-page')
        else:
            messages.error(request,"Tu contraseña debe tener mínimo 8 caracteres")
    return render(request, 'attendence/register.html', {})
   

        
def logoutuser(request):
    logout(request)
    return redirect('home-page')



def error_404_view(request,exception):
    return render(request,'attendence/404_error.html')
