from django.shortcuts import render

# Create your views here.
def recepies(request):
    return render(request,"recepies.html")
