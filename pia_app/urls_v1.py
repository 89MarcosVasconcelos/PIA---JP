from django.urls import path
from .views import  UsuarioPagoDetailAPIView, UsuarioPagoListCreateAPIView, RegisterView, AgendaUsuarioPagoListCreateAPIView, AgendaUsuarioPagoDetailAPIView , UsuarioPagoAllRegisterDetailAPIView

urlpatterns = [
    path('usuariopago/', UsuarioPagoListCreateAPIView.as_view(), name='usuario-pago-list'),
    path('usuariopago/<int:pk>/', UsuarioPagoDetailAPIView.as_view(), name='usuario-pago-detail'),
    path('usuariopagocheckregister/<int:pk>/', UsuarioPagoAllRegisterDetailAPIView.as_view(), name='usuario-pago-detail'),
    path('agendausuariopago/', AgendaUsuarioPagoListCreateAPIView.as_view(), name='agenda-usuario-pago-list'),
    path('agendausuariopago/<int:pk>/', AgendaUsuarioPagoDetailAPIView.as_view(), name='agenda-usuario-pago-detail'),
    

    # path('register/', RegisterView.as_view(), name='register'),
    path('register/', RegisterView, name='register'),
]
