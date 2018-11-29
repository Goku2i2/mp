from django.conf.urls import include, url

from . import views
from perris.quickstart import views2
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views2.UserViewSet)
router.register(r'groups', views2.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	#URL DE INICIO
    url(r'^$', views.inicio, name="inicio"),
    #URL DE REDIRIGIR
    url('perris/inicio', views.redirigir, name="redirigir"),
    #URL DE LOGIN - Registrar
    url('perris/login', views.login , name="login"),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    #URL DE Perros Disponibles
    url('perris/disponibles', views.perros_disponibles , name="perros_disponibles"),
    url('administrador',views.administrador_inicio, name="adm.inicio" ),
    #URL para agregar un nuevo post del perro_rescatado 
    path('agregar', views.new_post_perro, name='new_post_perro'),
    #URL para eliminar post 
    #Eliminar POST
    path('eliminar/<int:pk>', views.delete_post_perro, name='delete_post_perro'),
    #URL de detalles del post
    url(r'^perro/(?P<pk>[0-9]+)/$', views.detail_post_perro,name='detail_post_perro'),
    #URL Para editar un Post del Perro Rescatado 
    
    path('perro/<int:pk>/editar/', views.edit_post_perro, name='edit_post_perro'),
    
    url(r'^api-auth/', include('rest_framework.urls'))

 

]

