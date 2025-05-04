"""
URL configuration for pia_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pia_app.views import (
    UsuarioPagoListCreateAPIView,
    AgendaUsuarioPagoListCreateAPIView,
    UsuarioPagoDetailAPIView,
    AgendaUsuarioPagoDetailAPIView,
    CustomTokenView,
    RegisterView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # APIs organizadas por versão
    path('api/v1/', include('pia_app.urls_v1')),
    path('api/v2/', include('pia_app.urls_v2')),

    # Rotas de autenticação OAuth2
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('o/token/', CustomTokenView.as_view(), name='token'),

    # Rotas para usuários pagos
    path('api/v1/usuario_pago/', UsuarioPagoListCreateAPIView.as_view(), name='usuario_pago_list_create'),
    path('api/v1/usuario_pago/<int:pk>/', UsuarioPagoDetailAPIView.as_view(), name='usuario_pago_detail'),

    # Rotas para agenda de usuários pagos
    path('api/v1/agenda_usuario_pago/', AgendaUsuarioPagoListCreateAPIView.as_view(), name='agenda_usuario_pago_list_create'),
    path('api/v1/agenda_usuario_pago/<int:pk>/', AgendaUsuarioPagoDetailAPIView.as_view(), name='agenda_usuario_pago_detail'),

    # Registro de usuários
    path('api/v1/register/', RegisterView, name='register'),
]

