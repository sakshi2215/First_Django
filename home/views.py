from django.shortcuts import render
from django.http import HttpResponse  #respose return
# Create your views here.
def home(request):
    return render(request,"home/index.html")


def sucess_page(request):
    return HttpResponse("Hey this is a sucess page")