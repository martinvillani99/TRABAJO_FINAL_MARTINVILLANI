from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    juego = models.ForeignKey('Juego', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    juego = models.ForeignKey(Juego, related_name='comentarios', on_delete=models.CASCADE)
    texto = models.TextField()
    creado_por = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
