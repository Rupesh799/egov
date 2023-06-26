from django.shortcuts import render, HttpResponse, redirect
from account.models import User, Problems, alert
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password


def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']

        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('Home')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('Home')

    return HttpResponse('Invalid Access')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['un']
        password = make_password(request.POST['pw'])
        
        user = User(first_name=fname, last_name=lname, email=email, 
                     username=username, password=password)
        user.save()
        messages.info(request,'You have successfully Registered')
        return redirect('Home')

    return HttpResponse('Invalid Access')


def logout(request):
    auth.logout(request)
    messages.warning(request, 'You are logged out!')
    return redirect('Home')


def update_profile(request):
    pass


def change_password(request):
    pass

def alert(request):
    problems = Problems.objects.all()
    if request.method == "POST":
        problem = request.POST['problem']
        address = request.POST['address']
        img = request.POST['image']
       
        
        alert = alert(problem = Problems.objects.get(id=problem), user= request.user,location = address , image = img )
        alert.save()
        messages.success(request,"Problems have been Submitted!!")
        return redirect('alert')
    return render(request, 'alert.html', {'problem':problems})


    