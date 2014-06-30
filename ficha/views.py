# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

from ficha.models import formingreso
from ficha.models import Registro, RegistroForm
from ficha.models import Facultad, FacultadForm
from ficha.models import Semestre, SemestreForm
from ficha.models import Cuenta, CuentaForm
from ficha.models import Estudiante, EstudianteForm
from ficha.models import Rubro

def ingreso(request):
    if request.method == 'POST':
        formu = formingreso(request.POST)
        usuariologin = request.POST['usuarioform']
        passlogin = request.POST['passform']
        acceso = authenticate(username=usuariologin, password=passlogin)
        if acceso is not None:
            if acceso.is_active:
                login(request,acceso)
                return HttpResponseRedirect('/menu/')
            else:
                return render_to_response('noactivo.html')
        else:
            return render_to_response('nousuario.html')
    else:
        formu = formingreso()
    return render_to_response('ingreso.html',{'formu':formu},context_instance=RequestContext(request))

@login_required(login_url='/ingreso')
def salida(request):
    logout(request)
    return render_to_response('salir.html')

def menu(request):
    diccio={}
    return render_to_response('menu.html',{'datos':diccio})

def estudiante(request):
    if request.method == 'POST':
        formr= EstudianteForm(request.POST)
        if formr.is_valid():
            formr.save()
            return HttpResponseRedirect('/nuevo/')
    else:
        formr = EstudianteForm()
    return render_to_response('estudiante.html',{'formr':formr},context_instance=RequestContext(request))

def registro(request):
    if request.method == 'POST':
        a = Registro(recoger=True,debe=False)
        formr= RegistroForm(request.POST,instance=a)
        if formr.is_valid():
            #print dir(formr)
            print formr.data
            formr.save()
            return HttpResponseRedirect('/menu/')
    else:
        formr = RegistroForm()
    return render_to_response('registro.html',{'formr':formr},context_instance=RequestContext(request))

def cuentas(request):
    if request.method=='POST':
        formulario = CuentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/cuentas')
    else:
        formulario = CuentaForm()
    return render_to_response('cuentas.html',{'formulario':formulario}, context_instance=RequestContext(request))

def actividades(request):
    diccio={}
    return render_to_response('actividades.html',{'datos':diccio})


def facultades(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo = len(Estudiante.objects.filter(facultad=facu))
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('facultades.html',{'conteos':conteos})

def salud(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('salud.html',{'conteos':conteos})


def estimulo(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('estimulo.html',{'conteos':conteos})

def maternidad(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('maternidad.html',{'conteos':conteos})

def defuncion(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('defuncion.html',{'conteos':conteos})

def oftalmologia(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('oftalmologia.html',{'conteos':conteos})

def rendimiento(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('rendimiento.html',{'conteos':conteos})

def recoger(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('recoger.html',{'conteos':conteos})


def deudor(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('deudores.html',{'conteos':conteos})

def cancelo(request):
    contenido = Facultad.objects.all().order_by("nombre")
    conteos = []
    for facu in contenido:
        conteo=len(Estudiante.objects.filter(facultad=facu))
        cadena=facu.nombre
        conteos.append({'numero':conteo,'facultad':facu})
    return render_to_response('cancelo.html',{'conteos':conteos})

def repanual(request):
    diccio={}
    return render_to_response('repanual.html',{'datos':diccio})

#reportes
def reportes_facultad(request,id_facultad):
    contenido = Facultad.objects.all().order_by("nombre")
    facultad = Facultad.objects.get(pk=id_facultad)
    #print facultad
    estudiantes = Estudiante.objects.filter(facultad=facultad)
    #print estudiantes
    titulo = facultad.nombre
    activo = "0"
    url_ant='facultades'
    return render_to_response('reportes.html',{'estudiantes':estudiantes,'titulo_facultad':titulo,'facultad':facultad,'activo':activo,'url_ant':url_ant})

def reportes_facultad_estudiante(request,facultad,id_estudiante):
    facultad = Facultad.objects.get(pk=facultad)
    titulo = facultad.nombre
    estudiante = Estudiante.objects.get(pk=id_estudiante)
    registros = Registro.objects.filter(estudiante=estudiante)
    activo = "0"
    url_ant='facultades'
    return render_to_response('reportes.html',{'estudiante':estudiante,'titulo_facultad':titulo,'facultad':facultad,'registros':registros,'activo':activo,'url_ant':url_ant})

def reporte_motivo_facultad(request,motivo,id_facultad):
    motivos_url = {'1':'salud','2':'estimulo','3':'maternidad','4':'defuncion','5':'oftalmologia','6':'rendimiento'}
    motivo = Rubro.objects.get(pk=motivo)
    contenido = Facultad.objects.all().order_by("nombre")
    facultad = Facultad.objects.get(pk=id_facultad)
    titulo_facultad = facultad.nombre
    #print facultad
    estudiantes = Estudiante.objects.filter(facultad=facultad)
    #print estudiantes
    titulo = motivo.nombre
    activo = str(motivo.pk)
    url_mot = motivos_url[activo]
    return render_to_response('reportes.html',{'estudiantes':estudiantes,'titulo':titulo,'facultad':facultad,'titulo_facultad':titulo_facultad,'motivo':motivo,'activo':activo,'url_mot':url_mot})

def reporte_motivo_estudiante(request,motivo,facultad,estudiante):
    motivos_url = {'1':'salud','2':'estimulo','3':'maternidad','4':'defuncion','5':'oftalmologia','6':'rendimiento'}
    motivo = Rubro.objects.get(pk=motivo)
    facultad = Facultad.objects.get(pk=facultad)
    titulo = motivo.nombre
    titulo_facultad = facultad.nombre
    estudiante = Estudiante.objects.get(pk=estudiante)
    registros = Registro.objects.filter(estudiante=estudiante)
    registros = registros.filter(motivo=motivo)
    activo = str(motivo.pk)
    url_mot = motivos_url[activo]
    return render_to_response('reportes.html',{'estudiante':estudiante,'titulo':titulo,'titulo_facultad':titulo_facultad,'facultad':facultad,'registros':registros,'activo':activo,'motivo':motivo,'url_mot':url_mot})

def reporte_estado_facultad(request,estado,id_facultad):
    estados_url = {'recoger':'7','deudores':'8','cancelo':'9'}
    #motivo = Rubro.objects.get(pk=motivo)
    #estado = {'nombre':estado}
    contenido = Facultad.objects.all().order_by("nombre")
    facultad = Facultad.objects.get(pk=id_facultad)
    titulo_facultad = facultad.nombre
    #print facultad
    estudiantes = Estudiante.objects.filter(facultad=facultad)
    #print estudiantes
    titulo = estado
    activo = estados_url[estado]
    url_est = estado
    return render_to_response('reportes.html',{'estudiantes':estudiantes,'titulo':titulo,'facultad':facultad,'titulo_facultad':titulo_facultad,'estado':estado,'activo':activo,'url_est':url_est})

def reporte_estado_estudiante(request,estado,facultad,estudiante):
    estados_url = {'recoger':'7','deudores':'8','cancelo':'9'}
    contenido = Facultad.objects.all().order_by("nombre")
    facultad = Facultad.objects.get(pk=facultad)
    titulo_facultad = facultad.nombre
    estudiante = Estudiante.objects.get(pk=estudiante)
    registros = Registro.objects.filter(estudiante=estudiante)
    if estado=='recoger':
        registros = registros.filter(recoger=True)
    elif estado=='deudores':
        registros = registros.filter(debe=True)
    elif estado=='cancelo':
        registros = registros.filter(debe=False)
    titulo = estado.capitalize()
    activo = estados_url[estado]
    url_est = estado
    return render_to_response('reportes.html',{'estudiante':estudiante,'titulo':titulo,'titulo_facultad':titulo_facultad,'facultad':facultad,'registros':registros,'activo':activo,'estado':estado,'url_est':url_est})
