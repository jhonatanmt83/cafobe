#encoding:utf-8
from django.db import models
import datetime
from django import forms
from django.forms import ModelForm,Select,TextInput

# Create your models here.
class formingreso(forms.Form):
    usuarioform = forms.CharField(label='Usuario')
    passform = forms.CharField(label='Contraseña',widget=forms.PasswordInput(render_value=False))

class Rubro(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='rubro')

    def __unicode__(self):
        return self.nombre

class RubroForm(ModelForm):
    class Meta:
        model = Rubro

class Facultad(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Facultad')

    def __unicode__(self):
        return self.nombre

class FacultadForm(ModelForm):
    class Meta:
        model = Facultad

class Semestre(models.Model):
    nombre = models.CharField(max_length=4, verbose_name='Semestre')

    def __unicode__(self):
        return self.nombre

class SemestreForm(ModelForm):
    class Meta:
        model = Semestre

class Estudiante(models.Model):
    codigo = models.CharField(max_length=11, verbose_name = 'Codigo de Matricula', primary_key=True)
    apellidos = models.CharField(max_length=50, verbose_name = 'Apellidos')
    nombres = models. CharField(max_length=50, verbose_name = 'Nombres')
    facultad = models.ForeignKey(Facultad, null=True)
    semestre = models.ForeignKey(Semestre, null=True)

    def __unicode__(self):
        return self.nombres

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante

class Registro(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    expediente = models.CharField(max_length=10, verbose_name = 'Expediente', primary_key=True)
    emergencia = models.BooleanField(verbose_name='Emergencia')
    estudiante = models.ForeignKey(Estudiante)
    motivo = models.ForeignKey(Rubro, null=True)
    suma = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Monto S/.')
    acuerdo = models.TextField(verbose_name='Acuerdo')
    recoger = models.BooleanField(verbose_name='Falta Recoger')
    debe = models.BooleanField(verbose_name='Deudor')

    def __unicode__(self):
        return self.expediente

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        exclude = ('recoger','debe')

class Cuenta(models.Model):
    alumno = models.ForeignKey(Registro,verbose_name='Nro. de Expediente')
    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Monto S/.')
    fecha = models.DateTimeField(auto_now_add=True)
    resta = models.CharField(max_length=8, verbose_name='Resta deuda')
    texto = models.TextField(verbose_name='Documentos')

    def __unicode__(self):
        return self.texto

class CuentaForm(ModelForm):
    class Meta:
        model = Cuenta
	


