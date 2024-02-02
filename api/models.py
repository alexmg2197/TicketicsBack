from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

# Modelo de Areas
class Areas(models.Model):
    IdArea = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nombre = models.CharField(max_length=200)
    Clave = models.CharField(max_length=3, default='ccc')

# Modelo de Problemas
class Problemas(models.Model):
    IdProblema = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    AreaId = models.ForeignKey(Areas, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=250)

# Modelo de Personas
class Personas(models.Model):
    IdPersona = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, related_name='cred', on_delete=models.CASCADE)
    AreaId = models.ForeignKey(Areas, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=250)
    ApellidoP = models.CharField(max_length=250)
    ApellidoM = models.CharField(max_length=250)
    Rol = models.CharField(max_length=100)  
    Distrito = models.CharField(max_length=50, default = 'Pachuca')

# Modelo de Distritos
class Distritos(models.Model):
    IdDistrito = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Distrito = models.CharField(max_length=100)

# Modelo de Agencias
class Agencias(models.Model):
    IdAgencia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DistritoId = models.ForeignKey(Distritos, on_delete=models.CASCADE)
    Agencia = models.CharField(max_length=500)

# Modelo de Modulos
class Modulos(models.Model):
    IdModulo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    AgenciaId = models.ForeignKey(Agencias, on_delete=models.CASCADE)
    Modulo = models.CharField(max_length=500)

# Modelo de Reporte
class Reportes(models.Model):
    IdReporte = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PersonaId = models.ForeignKey(Personas, on_delete=models.CASCADE)
    ModuloId = models.ForeignKey(Modulos, on_delete=models.CASCADE)
    Folio = models.CharField(max_length=12)
    ContF = models.IntegerField(max_length=4,null=True,blank=True)
    Descripcion = models.CharField(max_length=1000, default='abcdefghijklmnopqrstuvwxyz')
    Observaciones = models.CharField(max_length=1000, default='observado')
    Acciones = models.CharField(max_length=1000, null=True, blank=True)
    FechaI = models.DateField(auto_now_add=True)
    HoraI = models.TimeField(auto_now_add=True)
    FechaF = models.DateField(null=True,blank=True)
    HoraF = models.TimeField(default=timezone.now, null=True, blank=True)
    FechaT = models.DateTimeField(auto_now_add=True)
    Prioridad = models.CharField(max_length=20)
    PersonaS = models.CharField(max_length=250)
    PersonaF = models.CharField(max_length=250, null=True, blank=True)
    Contacto = models.CharField(max_length=12, default='7711111111')
    Estatus = models.CharField(max_length=20)
    Activo = models.BooleanField(default=1)

# Modelo para almacenar tokens de servicios de usuarios
class Servicios(models.Model):
    IdServicio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PersonaId = models.ForeignKey(Personas, on_delete=models.CASCADE)
    Clave = models.CharField(max_length=500)
    Servicio = models.CharField(max_length=100)

# Modelo para almacenar los cambios realizados
class Operaciones(models.Model):
    IdOperacion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ReporteId = models.ForeignKey(Reportes, on_delete=models.CASCADE)
    PersonaId = models.ForeignKey(Personas, on_delete=models.CASCADE)
    Tipo = models.CharField(max_length=12)
    Motivo = models.CharField(max_length=500)
    Fecha = models.DateField(auto_now_add=True)
    Horafo = models.TimeField(auto_now_add=True)

    