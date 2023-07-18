from rest_framework import routers
from .api import (ColegioTablaViewSet, 
                  SalonTablaViewSet,
                  RolViewSet,
                  UsuariosViewSet,
                  ValuThinkificViewSet,
                  EstatusThinkificViewSet,
                  EstatusValuViewSet,
                  ModulosViewSet,
                  ContenidosColegioViewSet,
                  ModuloContenidoViewSet,
                  QuizTablaViewSet,
                  FeedbackViewSet,
                  MonitoreoViewSet,
                  JerarquiumViewSet
                  )


router = routers.DefaultRouter()

router.register('colegiotabla', ColegioTablaViewSet, 'colegio_tabla')
router.register('salontabla', SalonTablaViewSet, 'salon_tabla')
router.register('rol', RolViewSet, 'rol')
router.register('usuarios', UsuariosViewSet, 'usuarios')
router.register('valuthinkific', ValuThinkificViewSet, 'valu_thinkific')
router.register('estatusthinkific', EstatusThinkificViewSet, 'estatus_thinkific')
router.register('estatusvalu', EstatusValuViewSet, 'estatus_valu')
router.register('modulos', ModulosViewSet, 'modulos')
router.register('contenidoscolegio', ContenidosColegioViewSet, 'contenidos_colegio')
router.register('modulocontenido', ModuloContenidoViewSet, 'modulo_contenido')
router.register('quiztabla', QuizTablaViewSet, 'quiz_tabla')
router.register('feedback', FeedbackViewSet, 'feedback')
router.register('monitoreo', MonitoreoViewSet, 'monitoreo')
router.register('jerarquium', JerarquiumViewSet, 'jerarquium')

urlpatterns = router.urls
