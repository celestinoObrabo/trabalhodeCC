from django.shortcuts import render,redirect
from usuarios.forms import UserModelForm
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,'orientacao/home.html')

@login_required
def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'usuarios/cadastro.html',context)

def do_login(request):
    if request.method == 'POST':
        user = authenticate(email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('/cadastro')
    return render(request,'usuarios/login.html')

def do_logout(request):
    logout(request)
    return redirect('')
