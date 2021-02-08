from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm

def registerView(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request,'accounts/register.html',context)
        
