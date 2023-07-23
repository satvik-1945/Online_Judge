from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# from django.shortcuts import render
from .models import problem  # Import your 'Problem' model from models.py

def HomePage(request):
    probs = problem.objects.all()
    return render(request, 'home.html', {'probs': probs})

def problem_description(request, problem_id):
    # Assuming you have a 'problem_id' parameter to fetch the specific problem
    prob = problem.objects.get(pk=problem_id)
    print(prob)
    return render(request, 'description.html', {'prob': prob})


def submit_code(request, problem_id):
    prob = problem.objects.get(pk=problem_id)
    return render(request, 'verdict.html', {'prob': prob})
