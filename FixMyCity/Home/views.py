
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"home.html")

def alert(request):
    return render(request,"alert.html", {'title': "Alert"})


