from django.shortcuts import render, HttpResponse 


from Noticias.models import Project

# Create your views here.
def noticias(Request):
     
    project = Project.objects.all()
    return render (Request, "Noticias/Noticias.html",{'project':project})

    