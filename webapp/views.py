from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import modelform_factory

# Create your views here.
from personas.models import Persona
from webapp.forms import PersonaFormPersonalizado


def bienvenido(request):
    return HttpResponse("Hello World from Django")


def despedirce(request):
    return HttpResponse("Say Good Bye Django")


def mostrarVista(request):
    mensaje = {
        'msg1': 'Hellow Wolrd',
        'msg2': 'Este es el mensaje 2'
    }
    # se pasa a la funcion render (request, archivo:vista, variables_diccionario)
    return render(request, 'saludo.html', mensaje)


def get_cantidad_personas(request):
    # ClaseModel.objects.funcion()
    # cada clase tiene objects, y permite manipular con funciones la bd
    no_personas = Persona.objects.count()
    return render(request, 'personas.html', {'no_personas': no_personas})


def get_personas(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'personas.html', {'no_personas': no_personas, 'personas': personas})


def detalle_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle-persona.html', {'persona': persona})


""" Usamos el creador por defecto de django para formularios """


# PersonaForm = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaFormPersonalizado(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('lista-personas')

        else:
            return render(request, 'nueva_persona.html', {'formaPersona': formaPersona})
    else:
        formaPersona = PersonaFormPersonalizado()
        return render(request, 'nueva_persona.html', {'formaPersona': formaPersona})


def actualizar_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    # Para la actualizacion si viene el id, django sabe que es un update al registro de tipo Persona
    if request.method == 'POST':
        formaPersona = PersonaFormPersonalizado(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('lista-personas')
    else:
        formaPersona = PersonaFormPersonalizado(instance=persona)

    return render(request, 'actualizar_persona.html', {'formaPersona': formaPersona})

def eliminar_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
        return redirect('lista-personas')