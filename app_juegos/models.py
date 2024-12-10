from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
