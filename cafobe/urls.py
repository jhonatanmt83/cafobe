from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','ficha.views.ingreso'),
    url(r'^menu/$','ficha.views.menu'),
    url(r'^nuevo/$','ficha.views.registro'),
    url(r'^nuevoestudiante/$','ficha.views.estudiante'),
    url(r'^cuentas/$','ficha.views.cuentas'),
    url(r'^actividades/$','ficha.views.actividades'),
    url(r'^facultades/$','ficha.views.facultades'),
    url(r'^salud/$','ficha.views.salud'),
    url(r'^estimulo/$','ficha.views.estimulo'),
    url(r'^maternidad/$','ficha.views.maternidad'),
    url(r'^defuncion/$','ficha.views.defuncion'),
    url(r'^oftalmologia/$','ficha.views.oftalmologia'),
    url(r'^rendimiento/$','ficha.views.rendimiento'),
    url(r'^recoger/$','ficha.views.recoger'),
    url(r'^deudores/$','ficha.views.deudor'),
    url(r'^cancelo/$','ficha.views.cancelo'),
    url(r'^repanual/$','ficha.views.repanual'),
    url(r'^salida/$','ficha.views.salida'),
    
    #urls reportes
    
    url(r'^reportes/(?P<id_facultad>\w+)$','ficha.views.reportes_facultad'),
    url(r'^reportes/(?P<facultad>\w+)/(?P<id_estudiante>\w+)$','ficha.views.reportes_facultad_estudiante'),
    url(r'^reportes/motivo/(?P<motivo>\w+)/(?P<id_facultad>\w+)$','ficha.views.reporte_motivo_facultad'),
    url(r'^reportes/motivo/(?P<motivo>\w+)/(?P<facultad>\w+)/(?P<estudiante>\w+)$','ficha.views.reporte_motivo_estudiante'),
    url(r'^reportes/estado/(?P<estado>\w+)/(?P<id_facultad>\w+)$','ficha.views.reporte_estado_facultad'),
    url(r'^reportes/estado/(?P<estado>\w+)/(?P<facultad>\w+)/(?P<estudiante>\w+)$','ficha.views.reporte_estado_estudiante'),
            
    # Examples:
    # url(r'^$', 'cafobe.views.home', name='home'),
    # url(r'^cafobe/', include('cafobe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
