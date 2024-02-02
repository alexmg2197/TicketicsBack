from django.urls import path, include
from rest_framework import routers
from api import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Areas
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListAreas', views.ListAllAreas),
    path('v1/AreaById/<uuid:pk>', views.GetAreaById),
    path('v1/CrearArea', views.CrearArea),
    path('v1/ActualizarArea/<uuid:pk>', views.ModComArea),
    path('v1/ModificarArea/<uuid:pk>', views.ModParArea),
    path('v1/EliminarArea/<uuid:pk>', views.DeleteArea),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Problemas
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListProblemas', views.ListAllProblemas),
    path('v1/ProblemaById/<uuid:pk>', views.GetProblemaById),
    path('v1/CrearProblema', views.CrearProblema),
    path('v1/ActualizarProblema/<uuid:pk>', views.ModComProblema),
    path('v1/ModificarProblema/<uuid:pk>', views.ModParProblema),
    path('v1/EliminarProblema/<uuid:pk>', views.DeleteProblema),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Personas
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListPersonas', views.ListAllPersonas),
    path('v1/PersonaById/<uuid:pk>', views.GetPersonaById),
    path('v1/PersonaCById/<uuid:pk>', views.GetAllPersonaById),
    path('v1/PersonaByArea/<uuid:pk>', views.GetPersonaByArea),
    path('v1/PersonaByUser/<int:pk>', views.GetPersonaByUser),
    path('v1/CrearPersona', views.CrearPersona),
    path('v1/ActualizarPersona/<uuid:pk>', views.ModComPersona),
    path('v1/ModificarPersona/<uuid:pk>', views.ModParPersona),
    path('v1/EliminarPersona/<uuid:pk>', views.DeletePersona),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Distritos
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListDistritos', views.ListAllDistritos),
    path('v1/DistritoById/<uuid:pk>', views.GetDistritoById),
    path('v1/CrearDistrito', views.CrearDistrito),
    path('v1/ActualizarDistrito/<uuid:pk>', views.ModComDistrito),
    path('v1/ModificarDistrito/<uuid:pk>', views.ModParDistrito),
    path('v1/EliminarDistrito/<uuid:pk>', views.DeleteDistrito),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Agencias
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListAgencias', views.ListAllAgencias),
    path('v1/AgenciaById/<uuid:pk>', views.GetAgenciaById),
    path('v1/AgenciaByDistrito/<uuid:pk>', views.GetAgenciaByDistrito),
    path('v1/CrearAgencia', views.CrearAgencia),
    path('v1/ActualizarAgencia/<uuid:pk>', views.ModComAgencia),
    path('v1/ModificarAgencia/<uuid:pk>', views.ModParAgencia),
    path('v1/EliminarAgencia/<uuid:pk>', views.DeleteAgencia),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Modulos
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListModulos', views.ListAllModulos),
    path('v1/ModuloById/<uuid:pk>', views.GetModuloById),
    path('v1/ModuloByAgencia/<uuid:pk>', views.GetModuloByAgencia),
    path('v1/CrearModulo', views.CrearModulo),
    path('v1/ActualizarModulo/<uuid:pk>', views.ModComModulo),
    path('v1/ModificarModulo/<uuid:pk>', views.ModParModulo),
    path('v1/EliminarModulo/<uuid:pk>', views.DeleteModulo),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Reportes
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListReportes', views.ListAllReportes),
    path('v1/ListAllReportesC', views.ListAllReportesC),
    path('v1/ListAllReportesCByDistrito/<str:dis>', views.ListAllReportesCD),
    path('v1/ListAllReportesCF', views.ListAllReportesCF),
    path('v1/ListAllReportesCFByDistrito/<str:dis>', views.ListAllReportesCFD),
    path('v1/ReporteById/<uuid:pk>', views.GetReporteById),
    path('v1/ReporteByPersona/<uuid:pk>', views.GetReporteByPersona),
    path('v1/TotalReportesByPersona/<uuid:pk>', views.GetCountReportsByPersona),
    path('v1/ReporteByPersonaYEstatus/<uuid:pk>/<str:estatus>', views.GetReporteByPersonaF),
    path('v1/ReporteByEstatus/<str:pk>', views.GetReporteByEstatus),
    path('v1/ReporteByFolio/<str:fol>', views.GetReporteByFolio),
    path('v1/ReporteByArea/<uuid:pk>', views.GetReporteByArea),
    path('v1/CrearReporte', views.CrearReporte),
    path('v1/ActualizarReporte/<uuid:pk>', views.ModComReporte),
    path('v1/ModificarReporte/<uuid:pk>', views.ModParReporte),
    path('v1/EliminarReporte/<uuid:pk>', views.DeleteReporte),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Servicios
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListServicios', views.ListAllServices),
    path('v1/ServicioById/<uuid:pk>/<str:nom>', views.ListServiceByPersona),
    path('v1/CrearServicio', views.CrearServicio),  
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Servicios
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListOperaciones', views.ListOperations),
    path('v1/AllListOperaciones', views.AllListOperations),
    path('v1/RegistrarOpe', views.CrearOperation),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de User
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/ListUsers', views.ListAllUser),
    path('v1/CrearUsuario', views.CrearUsuario),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls de Authorization
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('api/token', MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # urls Globales
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('v1/CrearAreaReporta', views.CrearAreaR)
]