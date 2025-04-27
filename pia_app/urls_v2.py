# quadras/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioPagoViewSet, AgendaUsuarioPagoViewSet

router = DefaultRouter()
router.register(r'usuariopago', UsuarioPagoViewSet)
router.register(r'agendausuariopago', AgendaUsuarioPagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
