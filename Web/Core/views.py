from django.http import request
from django.shortcuts import render, HttpResponse 
from.forms import  ContactForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.



def inicio(Request): 

    return render(Request, "Core/Inicio.html")


def quienessomos(Request): 

    return render(Request, "Core/Quienes Somos.html")



def servicios(Request): 

    return render(Request, "Core/Servicios.html")

def cursos(Request): 

    return render(Request, "Core/Cursos.html")

def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "Estudio Juridico: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email,content),
                "no-aparicioseverich@gmail.com",
                ["aparicioseverich@gmail.com"],
                reply_to=[email]
                

            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('Contacto')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('Contacto')+"?fail")
    
    return render(request, "Core/contacto.html",{'form':contact_form})
