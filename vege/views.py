from django.shortcuts import render

# Create your views here.
def recepies(request):
    data= request.POST
    print(data)
    return render(request,"recepies.html")
