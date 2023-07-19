from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from .models import problem
# Create your views here.
@login_required(login_url = 'login')
def HomePage(request):
    probs = problem.objects.all()
    return render(request,'home.html',{'probs':probs})  
    