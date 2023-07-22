from django.shortcuts import render
from django.http import HttpResponse  #respose return
# Create your views here.
def home(request):

    peoples=[
        {'name':'Abhihjeet', 'age':26},
        {'name':'Abhi', 'age':16},
        {'name':'jeet', 'age':20},
        {'name':'Sakshi', 'age':19},
    ]
    return render(request,"home/index.html", context={'peoples':peoples})


def sucess_page(request):
    return HttpResponse("Hey this is a sucess page")