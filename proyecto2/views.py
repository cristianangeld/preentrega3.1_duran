from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola bienvenido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola bienvenido usuario, fecha: {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html


def saludar_con_html(request):
    contexto = {
        "usuario": "Lucas"
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/base.html',
        context=contexto,
    )
    return http_responde

def inicio(request):
    contexto = {
        "titulo": "Bienvenido a Control de Estudios",
        "descripcion": "Gestiona tus cursos y estudiantes de manera eficiente.",
        "enlace_cursos": "/cursos/",  
        "enlace_estudiantes": "/estudiantes/",  
    }
    return render(request, 'control_estudios/index.html', contexto)