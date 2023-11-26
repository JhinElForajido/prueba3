from django.shortcuts import render
from django.urls import path
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def Login(request):
    return render(request, "registrar/login.html")


@login_required
def Registro(request):
    """ Tarea:
     - Crear un dashboard para el admin
     - Crear un dashboard para el usuario
    """

    if request.user.is_superuser:
        return render(request, 'dashboard/dashboardAdmin.html')
    if request.user.is_staff:
        return render(request, 'dashboard/dashboardStaff.html')
    else:
        return render(request, 'dashboard/dashboardUser.html')