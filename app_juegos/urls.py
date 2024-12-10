from django.urls import path
from .views import crear_categoria, crear_juego, crear_cliente, crear_pedido, buscar_juego, delete_juegos, listar_juego, update_juegos

app_name = 'app_juegos'

urlpatterns = [
    path('buscar_juego/', buscar_juego, name='buscar_juego'),
    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_juego/', crear_juego, name='crear_juego'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('listar_juego/', listar_juego, name='listar_juego'),
    path('eliminar-libros/<int:id>', delete_juegos, name='delete_juegos'),
    path('actualizar-libros/<int:id>', update_juegos, name='update_juegos'),
    
]
