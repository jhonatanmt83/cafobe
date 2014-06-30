from django.contrib import admin
from ficha.models import Rubro
from ficha.models import Estudiante
from ficha.models import Registro
from ficha.models import Facultad
from ficha.models import Semestre
from ficha.models import Cuenta

admin.site.register(Rubro)
admin.site.register(Estudiante)
admin.site.register(Registro)
admin.site.register(Facultad)
admin.site.register(Semestre)
admin.site.register(Cuenta)

