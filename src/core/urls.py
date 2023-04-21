from rest_framework import routers
from .api import ColeTablaViewSet, EstudiantesTablaViewSet, ModulosViewSet, QuizTablaViewSet, SalonTablaViewSet


router = routers.DefaultRouter()

router.register('coletabla', ColeTablaViewSet, 'cole')
router.register('estudiantestabla', EstudiantesTablaViewSet, 'estudiantes')
router.register('modulos', ModulosViewSet, 'modulos')
router.register('quiztabla', QuizTablaViewSet, 'quiz')
router.register('salontabla', SalonTablaViewSet, 'salon')

urlpatterns = router.urls