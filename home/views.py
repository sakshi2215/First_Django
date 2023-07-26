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
    for people in peoples:
        if people['age']:
            print("Yes")
    return render(request,"home/index.html", context={'page':'Django 2023 Tutorial','peoples':peoples})


def sucess_page(request):
    return HttpResponse("Hey this is a sucess page")

def about_page(request):
    context={ 'page' :'About'}
    return render(request,"home/about.html",context)

def contact_page(request):
    context={ 'page' :'Contact'}
    return render(request,"home/contact.html",context)