from rest_framework import routers
from .api import (ColeTablaViewSet, 
                  EstudiantesTablaViewSet, 
                  ModulosViewSet, 
                  QuizTablaViewSet, 
                  SalonTablaViewSet, 
                  MonitorTablaViewSet, 
                  SalonKpiModuloViewSet,
                  EstatusViewSet,
                  MonitoreoViewSet,
                  FeedbackViewSet,
                  EstudiantesConPromedioYModulosViewSet,
                  EstudiantesRankingPorModulosViewSet
                  )


router = routers.DefaultRouter()

router.register('coletabla', ColeTablaViewSet, 'cole_tabla')
router.register('modulos', ModulosViewSet, 'modulos_tabla')
router.register('quiztabla', QuizTablaViewSet, 'quiz_tabla')
router.register('salontabla', SalonTablaViewSet, 'salon_tabla')
router.register('monitortabla', MonitorTablaViewSet, 'monitor_tabla')
router.register('estudiantestabla', EstudiantesTablaViewSet, 'estudiantes_tabla')
router.register('salonkpimodulo', SalonKpiModuloViewSet, 'salon_kpi_modulo')
router.register('estatus', EstatusViewSet, 'estatus')
router.register('monitoreo', MonitoreoViewSet, 'monitoreo')
router.register('feedback', FeedbackViewSet, 'feedback')
router.register('estudiantesconpromedio', EstudiantesConPromedioYModulosViewSet, 'estudiantesconpromedio')
router.register('estudiantesrankingmodulos', EstudiantesRankingPorModulosViewSet, 'estudiantesrankingmodulos')

urlpatterns = router.urls
