from rest_framework import serializers
from .models import Areas, Problemas, Personas, Distritos, Agencias, Modulos, Reportes, Servicios, Operaciones
from django.contrib.auth.models import User

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Areas
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Problemas
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class ProblemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problemas
        fields = '__all__'

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo User
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar campos de login de User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Personas
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'

# Serializador para retornar todos los campos con su area
class PersonasASerializer(serializers.ModelSerializer):
    area = AreasSerializer(read_only=True,source='AreaId')
    class Meta:
        model = Personas
        fields = ('IdPersona','Nombre','ApellidoP','ApellidoM','Rol','Distrito','user','area')

# Serializador para retornar todos los campos de user y persona
class AllPersonaSerializer(serializers.ModelSerializer):
    cred = UserSerializer(read_only=True, source='user')
    class Meta:
        model = Personas
        fields = ('IdPersona','AreaId','Nombre','ApellidoP','ApellidoM','Rol','Distrito','user', 'cred')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Distritos
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class DistritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distritos
        fields = '__all__'

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Agencias
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class AgenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencias
        fields = '__all__'

# Serializador para retornar todos los campos con distrito
class AgenciasASerializer(serializers.ModelSerializer):
    dis = DistritosSerializer(read_only=True, source='DistritoId')
    class Meta:
        model = Agencias
        fields = ('IdAgencia', 'Agencia', 'dis')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Modulos
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'

# Serializador para retornar todos los campos con agencia
class ModulosASerializer(serializers.ModelSerializer):
    age = AgenciasASerializer(read_only=True, source='AgenciaId')
    class Meta:
        model = Modulos
        fields = ('IdModulo','Modulo','age')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Reportes
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos
class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reportes
        fields = '__all__'

# Serializador para retornar todos los campos de persona y modulo
class AllReporteSerializer(serializers.ModelSerializer):
    per = PersonasASerializer(read_only=True, source='PersonaId')
    mod = ModulosASerializer(read_only=True, source='ModuloId')
    # age = AgenciasSerializer(read_only=True,source='ModuloId__AgenciaId')
    class Meta:
        model = Reportes
        fields = ('IdReporte', 'Descripcion', 'Observaciones', 'Acciones', 'Contacto', 'Folio','ContF','FechaI', 'HoraI', 'FechaF', 'HoraF', 'Prioridad','PersonaS','PersonaF','Estatus', 'per','mod','FechaT')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Servicios
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serializador para retornar todos los campos 
class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Serializadores del modelo Servicios
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serilizador del modelo de Operaciones
class OperacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operaciones
        fields = '__all__'

# Serilizador del modelo de Operaciones con nombre de persona y ticket
class AllOperacionesSerializer(serializers.ModelSerializer):
    pers = PersonasSerializer(read_only=True, source='PersonaId')
    rep = ReportesSerializer(read_only=True, source='ReporteId')
    class Meta:
        model = Operaciones
        fields = ('IdOperacion', 'Tipo', 'Motivo', 'pers', 'rep', 'Fecha', 'Horafo')