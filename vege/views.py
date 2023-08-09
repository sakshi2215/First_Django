from django.shortcuts import render ,redirect
from .models import*

# Create your views here.
def recepies(request):
    if request.method == "POST":
        data= request.POST
        recepie_image= request.FILES.get('recepie_image')
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')
        print(recepie_name)
        print(recepie_description)
        print(recepie_image)
# To save the data 
        Recepies.objects.create(
            recipie_image=recepie_image,
            recipie_name=recepie_name,
            recipie_description=recepie_description,
        )
        return redirect('/recepies/')

    queryset= Recepies.objects.all()
    context = {'recepies':queryset}
    return render(request,"recepies.html",context=context)

def delete_recepie(request, id):
    queryset = Recepies.objects.get(id= id)
    queryset.delete()
    return redirect('/recepies/')
