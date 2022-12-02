"""configuracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
from web.views import Home,Medicosvista,consultorioMedico,consultoriopaciente,Pacientesvista

=======
from web.views import Home,Medicosvista
from web.views import Home
#Pacientesvista
>>>>>>> f3d4c5a08fe6430e1d3d8c70fa0ffe976cff8bae

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Home, name="home"),
    path('medicos/', Medicosvista, name="medicos"),
<<<<<<< HEAD
    path('pacientes/', Pacientesvista, name="pacientes"),
    path('consultoriomedico/', consultorioMedico, name="consultoriomedico"),
    path('consultoriopaciente/', consultoriopaciente, name="consultoriopaciente")
=======
    #path('pacientes/', Pacientesvista, name="pacientes")
>>>>>>> f3d4c5a08fe6430e1d3d8c70fa0ffe976cff8bae
]
