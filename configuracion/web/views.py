from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formulariopaciente import FormularioPaciente

from web.models import Medicos
#from web.models import Pacientes

# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def consultorioMedico(request):
    medicosConsultados = Medicos.objects.all()

    datosmedicos={
        "medicos":medicosConsultados
    }
    return render(request,'consultoriomedico.html',datosmedicos)

def consultoriopaciente(request):
    pacientesConsultados = Pacientes.objects.all()
    
    datospacientes={
        "pacientes":pacientesConsultados
    }
    return render(request,'consultoriopaciente.html',datospacientes)

def Medicosvista(request):
    #Creamos una variable para controlar la ejecucion del modal/alerta
    lanzandoAlerta = False

    #creamos una variable para controlar la ejecucion de la alerta de submit del medicos
    lanzandoalerta=False

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario,
        "bandera":lanzandoalerta
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #llevar mis datos hacia la base datos BD
            medicoNuevo = Medicos( 
                nombres=datos["nombre"],
                apellidos= datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta = datos["tarjetaProfesional"],
                especialidad =datos["especialidad"],
                jornada = datos["jornada"],
                contacto = datos["contacto"],
                sede = datos["sede"]
            )
            medicoNuevo.save()
            #print("Exito en la operacion")
            diccionario["bandera"]=True


    return render(request,'registromedicos.html',diccionario)

'''def Pacientesvista(request):


    formulario=FormularioPaciente()
    diccionario={
        "formulario":formulario
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioPaciente(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #llevar mis datos hacia la base datos BD
            pacienteNuevo = Pacientes(
                nombres=datos["nombre"],
                apellidos= datos["apellidos"],
                cedula=datos["cedula"],
                tipo=datos["TipoAfiliado"],
                regimen=datos["regimen"],
                contacto=datos["contacto"],
                grupo= datos["GrupoIngreso"]

            )
            pacienteNuevo.save()
            print("Exito en la operacion")


    return render(request,'registroPacientes.html',diccionario)'''
