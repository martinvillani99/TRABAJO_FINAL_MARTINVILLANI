from django.urls import path, include
from django.contrib import admin
from .views import crear_categoria, crear_juego, crear_cliente, crear_pedido, buscar_juego, delete_juegos, listar_juegos, update_juegos
from . import views
from app_juegos import views
app_name = 'app_juegos'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('buscar_juego/', views.buscar_juego, name='buscar_juego'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_juego/', views.crear_juego, name='crear_juego'),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('listar_juegos/', views.listar_juegos, name='listar_juegos'),
    path('eliminar-juegos/<int:id>/', views.delete_juegos, name='delete_juegos'),
    path('actualizar-juegos/<int:id>/', views.update_juegos, name='update_juegos'),
    path('add_comment/<int:juego_id>/', views.add_comment, name='add_comment'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('about/', views.about, name='about'),
]
