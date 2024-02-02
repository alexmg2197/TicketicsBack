from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import logging
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AreasSerializer, ProblemasSerializer, PersonasSerializer, AllPersonaSerializer, DistritosSerializer, AgenciasSerializer, ModulosSerializer, ReportesSerializer, UserSerializer, AllReporteSerializer, ServiciosSerializer, OperacionesSerializer, AllOperacionesSerializer
from .models import Areas, Problemas, Personas, Distritos, Agencias, Modulos, Reportes, Servicios, Operaciones
from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Value, IntegerField

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Areas
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todas las Áreas
@api_view(['GET'])
def ListAllAreas(request):
    queryset = Areas.objects.all()
    query_seria = AreasSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Área por su ID
@api_view(['GET'])
def GetAreaById(request, pk=None):
    queryset = Areas.objects.filter(IdArea = pk).first()
    query_seria = AreasSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para crear un Área
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CrearArea(request):
    query_seria = AreasSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'creada'})

    return Response(query_seria.errors)

# Endpoint para modificar todos los campos de un Área
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ModComArea(request, pk=None):
    queryset = Areas.objects.filter(IdArea = pk).first()
    query_seria = AreasSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'actualizada'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de un Área
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def ModParArea(request, pk=None):
    queryset = Areas.objects.filter(IdArea = pk).first()
    query_seria = AreasSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'actualizada'})
    return Response({'message':'error en los parámetros'})
        
# Endpoint para eliminar un Área
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteArea(request, pk=None):
    queryset = Areas.objects.filter(IdArea = pk).first()
    queryset.delete()

    return Response({'message':'eliminada'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Problemas
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todos los Problemas
@api_view(['GET'])
def ListAllProblemas(request):
    queryset = Problemas.objects.all()
    query_seria = ProblemasSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Problema por su ID
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetProblemaById(request, pk=None):
    queryset = Problemas.objects.filter(IdProblema = pk).first()
    query_seria = ProblemasSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para crear un Problema
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CrearProblema(request):
    query_seria = ProblemasSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'Creado'})

    return Response(query_seria.errors)

# Endpoint para modificar todos los campos de un Problema
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ModComProblema(request, pk=None):
    queryset = Problemas.objects.filter(IdProblema = pk).first()
    query_seria = ProblemasSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'actualizado'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de un Problema
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def ModParProblema(request, pk=None):
    queryset = Problemas.objects.filter(IdProblema = pk).first()
    query_seria = ProblemasSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'actualizado'})
    return Response({'message':'error en los parámetros'})

# Endpoint para eliminar un Problema
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteProblema(request, pk=None):
    queryset = Problemas.objects.filter(IdProblema = pk).first()
    queryset.delete()

    return Response({'message':'eliminado'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Personas
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todas las Personas
@api_view(['GET'])
def ListAllPersonas(request):
    queryset = Personas.objects.all()
    query_seria = PersonasSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener una Persona por su ID
@api_view(['GET'])
def GetPersonaById(request, pk=None):
    queryset = Personas.objects.filter(IdPersona = pk).first()
    query_seria = PersonasSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para obtener una Persona completa por su ID
@api_view(['GET'])
def GetAllPersonaById(request, pk=None):
    queryset = Personas.objects.select_related('user').get(IdPersona = pk)
    query_seria = AllPersonaSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para obtener una Persona por Area
@api_view(['GET'])
def GetPersonaByArea(request, pk=None):
    queryset = Personas.objects.filter(AreaId = pk)
    # queryset = Reportes.objects.select_related('PersonaId').filter(Estatus = 'Iniciado')
    # queryset = Personas.objects.annotate(
    #     num_r_i=Count(
    #         Case(
    #             When(reportes__Estatus = 'Iniciado', then=Value(1)),
    #             output_field = IntegerField()
    #         )
    #     )
    # ).filter(num_r_i__lt=3, AreaId = pk)
    
    query_seria = PersonasSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para obtener una Persona por user
@api_view(['GET'])
def GetPersonaByUser(request, pk=None):
    queryset = Personas.objects.filter(user_id = pk)
    query_seria = AllPersonaSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para crear una Persona
@api_view(['POST'])
def CrearPersona(request):
    query_seria = PersonasSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response(query_seria['IdPersona'].value)

    return Response(query_seria.errors)

# Endpoint para modificar todos los campos de una Persona
@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def ModComPersona(request, pk=None):
    queryset = Personas.objects.filter(IdPersona = pk).first()
    query_seria = AllPersonaSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'Persona Actualizada'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de una Persona
@api_view(['PATCH'])
#@permission_classes([IsAuthenticated])
def ModParPersona(request, pk=None):
    queryset = Personas.objects.filter(IdPersona = pk).first()
    query_seria = PersonasSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'actualizada'})
    return Response({'message':'error en los parámetros'})

# Endpoint para eliminar una Persona
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeletePersona(request, pk=None):
    queryset = Personas.objects.filter(IdPersona = pk).first()
    queryset.delete()

    return Response({'message':'eliminada'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Distritos
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todos los Distritos
@api_view(['GET'])
def ListAllDistritos(request):
    queryset = Distritos.objects.all()
    query_seria = DistritosSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Distrito por su ID
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetDistritoById(request, pk=None):
    queryset = Distritos.objects.filter(IdDistrito = pk).first()
    query_seria = DistritosSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para crear un Distrito
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CrearDistrito(request):
    try:
        distrito = Distritos.objects.get(Distrito=request.data['Distrito'])

        if(distrito.MultipleObjectsReturned):
            return Response({'message':'existe','data':distrito.IdDistrito})
        
    except Distritos.DoesNotExist:
        query_distrito = DistritosSerializer(data = {
            'Distrito': request.data['Distrito']
        })

        if query_distrito.is_valid():
            query_distrito.save()

            id_distrito = query_distrito['IdDistrito']

            return Response({'message':'creado', 'data':id_distrito.value})
        
        return Response(query_distrito.errors)

# Endpoint para modificar todos los campos de un Distrito
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ModComDistrito(request, pk=None):
    queryset = Distritos.objects.filter(IdDistrito = pk).first()
    query_seria = DistritosSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'actualizado'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de un Distrito
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def ModParDistrito(request, pk=None):
    queryset = Distritos.objects.filter(IdDistrito = pk).first()
    query_seria = DistritosSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'actualizado'})
    return Response({'message':'error en los parámetros'})

# Endpoint para eliminar un Distrito
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteDistrito(request, pk=None):
    queryset = Distritos.objects.filter(IdDistrito = pk).first()
    queryset.delete()

    return Response({'message':'eliminado'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Agencias
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todas las Agencias
@api_view(['GET'])
def ListAllAgencias(request):
    queryset = Agencias.objects.all()
    query_seria = AgenciasSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener una Agencia por su ID
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetAgenciaById(request, pk=None):
    queryset = Agencias.objects.filter(IdAgencia = pk).first()
    query_seria = AgenciasSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para obtener una Agencia por ID de Distrito
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetAgenciaByDistrito(request, pk=None):
    queryset = Agencias.objects.filter(DistritoId = pk)
    query_seria = AgenciasSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para crear una Agencia
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CrearAgencia(request):
    query_seria = AgenciasSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'creada'})

    return Response(query_seria.errors)

# Endpoint para modificar todos los campos de una Agencia
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ModComAgencia(request, pk=None):
    queryset = Agencias.objects.filter(IdAgencia = pk).first()
    query_seria = AgenciasSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'actualizada'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de una Agencia
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def ModParAgencia(request, pk=None):
    queryset = Agencias.objects.filter(IdAgencia = pk).first()
    query_seria = AgenciasSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'actualizada'})
    return Response({'message':'error en los parámetros'})

# Endpoint para eliminar una Agencia
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteAgencia(request, pk=None):
    queryset = Agencias.objects.filter(IdAgencia = pk).first()
    queryset.delete()

    return Response({'message':'eliminada'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Modulos
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todos los Modulos
@api_view(['GET'])
def ListAllModulos(request):
    queryset = Modulos.objects.all()
    query_seria = ModulosSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Modulo por su ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetModuloById(request, pk=None):
    queryset = Modulos.objects.filter(IdModulo = pk).first()
    query_seria = ModulosSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para obtener un Modulo por su ID
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetModuloByAgencia(request, pk=None):
    queryset = Modulos.objects.filter(AgenciaId = pk)
    query_seria = ModulosSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para crear un Modulo
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CrearModulo(request):
    query_seria = ModulosSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'creado'})

    return Response(query_seria.errors)

# Endpoint para modificar todos los campos de un Modulo
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ModComModulo(request, pk=None):
    queryset = Modulos.objects.filter(IdModulo = pk).first()
    query_seria = ModulosSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'actualizado'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de un Modulo
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def ModParModulo(request, pk=None):
    queryset = Modulos.objects.filter(IdModulo = pk).first()
    query_seria = ModulosSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'actualizado'})
    return Response({'message':'error en los parámetros'})

# Endpoint para eliminar un Modulos
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteModulo(request, pk=None):
    queryset = Modulos.objects.filter(IdModulo = pk).first()
    queryset.delete()

    return Response({'message':'eliminado'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Reportes
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para obtener todos los Reportes
@api_view(['GET'])
def ListAllReportes(request):
    queryset = Reportes.objects.filter(Activo = 1).order_by('-ContF')
    query_seria = ReportesSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener todos los Reportes completos
@api_view(['GET'])
def ListAllReportesC(request):
    queryset_P = Reportes.objects.select_related('PersonaId','ModuloId').filter(Activo = 1, Estatus = 'Iniciado').order_by('FechaT')
    query_seria = AllReporteSerializer(queryset_P, many=True)

    return Response(query_seria.data)

# Endpoint para obtener todos los Reportes completos por distrito del usuario
@api_view(['GET'])
def ListAllReportesCD(request, dis=None):
    queryset_P = Reportes.objects.select_related('PersonaId','ModuloId').filter(Activo = 1, Estatus = 'Iniciado', PersonaId__Distrito=dis).order_by('FechaT')
    query_seria = AllReporteSerializer(queryset_P, many=True)

    return Response(query_seria.data)

# Endpoint para obtener todos los Reportes completos finalizados
@api_view(['GET'])
def ListAllReportesCF(request):
    queryset_P = Reportes.objects.select_related('PersonaId','ModuloId').filter(Activo = 1).order_by('FechaT')
    query_seria = AllReporteSerializer(queryset_P, many=True)

    return Response(query_seria.data)

# Endpoint para obtener todos los Reportes completos finalizados por distrito
@api_view(['GET'])
def ListAllReportesCFD(request, dis=None):
    queryset_P = Reportes.objects.select_related('PersonaId','ModuloId').filter(Activo = 1, PersonaId__Distrito=dis).order_by('FechaT')
    query_seria = AllReporteSerializer(queryset_P, many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Reporte por su ID
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetReporteById(request, pk=None):
    queryset = Reportes.objects.select_related('PersonaId','ModuloId').filter(IdReporte = pk)
    query_seria = AllReporteSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Reporte por Persona
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetReporteByPersona(request, pk=None):
    queryset = Reportes.objects.filter(PersonaId = pk)
    query_seria = AllReporteSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para obtener la cantidad de reportes asigandos a un usuario
@api_view(['GET'])
def GetCountReportsByPersona(request, pk=None):
    queryset = Reportes.objects.filter(PersonaId = pk, Estatus = 'Iniciado').count()

    return Response({'total':queryset})

# Endpoint para obtener los Reportes por Persona y sean finalizados
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetReporteByPersonaF(request, pk=None, estatus=None):
    queryset = Reportes.objects.filter(PersonaId = pk, Estatus = estatus)
    query_seria = AllReporteSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Reporte por Estatus
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetReporteByEstatus(request, pk=None):
    queryset = Reportes.objects.filter(Estatus = pk, Activo = 1)
    query_seria = AllReporteSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Reporte por Estatus
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetReporteByArea(request, pk=None):
    queryset = Reportes.objects.filter(PersonaId__AreaId = pk, Activo = 1, Estatus = 'Iniciado')
    query_seria = AllReporteSerializer(queryset,many=True)

    return Response(query_seria.data)

# Endpoint para obtener un Reporte por Folio
@api_view(['GET'])
def GetReporteByFolio(request, fol=None):
    queryset = Reportes.objects.filter(Activo = 1, Estatus = 'Iniciado', Folio__contains=fol)
    query_seria = AllReporteSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para crear un Reporte
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CrearReporte(request):
    query_seria = ReportesSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'Reporte Creado', 'id':query_seria.data})

    return Response(query_seria.errors)

# Endpoint para modificar todos los campos de un Reporte
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def ModComReporte(request, pk=None):
    queryset = Reportes.objects.filter(IdReporte = pk).first()
    query_seria = ReportesSerializer(queryset, data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'actualizado'})
    
    return Response(query_seria.errors)

# Endpoint para modificar algunos campos de un Reporte
@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def ModParReporte(request, pk=None):
    queryset = Reportes.objects.filter(IdReporte = pk).first()
    query_seria = ReportesSerializer(queryset, data=request.data, partial=True)
    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'Reporte Actualizado'})
    return Response({'message':'error en los parámetros'})

# Endpoint para eliminar un Reporte
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteReporte(request, pk=None):
    queryset = Reportes.objects.filter(IdReporte = pk).first()
    query_seria = ReportesSerializer(queryset, data=request.data, partial=True)

    if query_seria.is_valid():
        query_seria.save()
        return Response({'message':'Reporte Eliminado'})
    return Response({'message':'error en los parámetros'})
    # queryset.delete()

    # return Response({'message':'Reporte Eliminado'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Servicios
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para enlistar todas las claves de todos los servicios de todos los usuarios
@api_view(['GET'])
def ListAllServices(request):
    queryset = Servicios.objects.all()
    query_seria = ServiciosSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para retornar un servicio en especifico de un usuario por Id
@api_view(['GET'])
def ListServiceByPersona(request, pk=None, nom=None):
    queryset = Servicios.objects.get(PersonaId=pk, Servicio=nom)
    query_seria = ServiciosSerializer(queryset)

    return Response(query_seria.data)

# Endpoint para guardar un nuevo servicio de un usuario
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CrearServicio(request):
    query_seria = ServiciosSerializer(data = request.data)
    if query_seria.is_valid():
        query_seria.save()

        return Response({'message': 'Servicio Creado'})

    return Response(query_seria.errors)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de User
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para enlistar todos los Usuarios
@api_view(['GET'])
def ListAllUser(request):
    queryset = User.objects.all()
    query_seria = UserSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para crear un Usuario
@api_view(['POST'])
def CrearUsuario(request):
    try:
        new = User.objects.create_user(username=request.data['username'], email=request.data['email'], password=request.data['password'])
        return Response(new.pk)
    except:
        return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Operaciones
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para listar todas las operacines realizadas
@api_view(['GET'])
def ListOperations(request):
    queryset = Operaciones.objects.all()
    query_seria = OperacionesSerializer(queryset, many=True)

    return Response(query_seria.data)

# Endpoint para listar todas las operacines realizadas per rep
@api_view(['GET'])
def AllListOperations(request):
    queryset_A = Operaciones.objects.select_related('PersonaId','ReporteId')
    query_seria = AllOperacionesSerializer(queryset_A, many=True)

    return Response(query_seria.data)

# Endpoint para registrar una nueva operación
@api_view(['POST'])
def CrearOperation(request):
    query_seria = OperacionesSerializer(data = request.data)

    if query_seria.is_valid():
        query_seria.save()

        return Response({'message':'Operación Registrada'})
    
    return Response(query_seria.errors)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints de Authorization
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para Crear el token para el inicio del usuario
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        try:
            usu = User.objects.get(username = user.username)

            correct = usu.check_password(user.password)

            if(usu.DoesNotExist):
                return Response({'message':'Not User'})
            if(correct):
                token= usu.get_token()
                return token
            else:
                return Response({'message':'WrongPassword'})
        except:
            return Response({'message':'NotUser'})
                
# Endpoint  para retornar el token para el inicio del usuario
class MyTokenObtainPairView(TokenObtainPairView):
    @classmethod
    def get_token():
        try:
            serializer_class = MyTokenObtainPairSerializer

            return serializer_class
        except:
            return Response({'message':'NotUser'})
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoints Globales
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint para crear un Area que reporta
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CrearAreaR(request):
    id_distrito = ''
    id_agencia = ''
    id_modulo = ''
    logging.basicConfig(level=logging.NOTSET)

    distrito = Distritos.objects.filter(Distrito=request.data['Distrito'])

    if(distrito.exists()):
        query = Distritos.objects.get(Distrito=request.data['Distrito'])
        agencia = Agencias.objects.filter(Agencia=request.data['Agencia'], DistritoId=query.IdDistrito)         
        id_distrito = query.IdDistrito
        
    else:
        query_distrito = DistritosSerializer(data = {
            'Distrito': request.data['Distrito']
        })

        if query_distrito.is_valid():
            query_distrito.save()
            agencia = Agencias.objects.filter(Agencia=request.data['Agencia'], DistritoId=query_distrito['IdDistrito'].value)             
            id_distrito = query_distrito['IdDistrito'].value
        else:
            return Response(query_distrito.errors)
    if(agencia.exists()):
        query = Agencias.objects.get(Agencia=request.data['Agencia'], DistritoId = id_distrito)
        id_agencia = query.IdAgencia
        modulo = Modulos.objects.filter(Modulo=request.data['Modulo'], AgenciaId=id_agencia)

    else:
        query_agencia = AgenciasSerializer(data = {
            'Agencia': request.data['Agencia'],
            'DistritoId': id_distrito
        })        
        if query_agencia.is_valid():
            query_agencia.save()
            id_agencia = query_agencia['IdAgencia'].value
            modulo = Modulos.objects.filter(Modulo=request.data['Modulo'], AgenciaId=id_agencia)
        else:
            return Response(query_agencia.errors)
        
    logging.info(modulo)
    if(modulo.exists()):
        query = Modulos.objects.get(Modulo=request.data['Modulo'], AgenciaId=id_agencia)
        id_modulo = query.IdModulo
    else:
        query_modulo = ModulosSerializer(data = {
            'Modulo': request.data['Modulo'],
            'AgenciaId': id_agencia
        })
        if query_modulo.is_valid():
            query_modulo.save()

            id_modulo = query_modulo['IdModulo'].value
        else:
            return Response(query_modulo.errors)

    # logging.info(id_distrito)
    # logging.info(id_agencia)
    # logging.info(id_modulo)

    return Response({'message':'Area de reporte creada'})
    # return Response(query_distrito.errors)