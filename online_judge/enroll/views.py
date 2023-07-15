from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = 'login')
def HomePage(request):
    return render(request,'home.html')  
def signupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1!= password2:
            return HttpResponse("Your password is not same")
        else:
            myUser = User.objects.create_user(uname,email,password1)
            myUser.save()
            return redirect('login')
            # print(uname, email, password1, password2)

    return render(request,'sign-up.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('pass')
        user = authenticate(request,username = username,password = password1)

        if user is not None:    
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!")


    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')