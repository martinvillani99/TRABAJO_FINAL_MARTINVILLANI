
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CategoriaForm, JuegoForm, ClienteForm, PedidoForm
from .models import Juego

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'app_juegos/lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_create.html', {'form': form})

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_juegos:lista_juegos')
    else:
        form = JuegoForm()
    return render(request, 'juego_create.html', {'form': form})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedido_create.html', {'form': form})

def buscar_juego(request):
    if request.method == 'GET' and 'nombre' in request.GET:
        juegos = Juego.objects.filter(nombre__icontains=request.GET['nombre'])
    else:
        juegos = Juego.objects.all()
    return render(request, 'buscar_juego.html', {'juegos': juegos})

def listar_juego(request):
    juegos = Juego.objects.all()
    contexto = {'juegos': juegos}
    return render(request,'app_juegos/juego_list.html', contexto)

def delete_juegos(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        juego.delete()
        return redirect('app_juegos:listar_juegos')
    contexto = {'juego' : juego}
    return render(request, 'app_libros/juego_delete.html',contexto)

def update_juegos(request, id):
    juego = get_object_or_404(Juego, id=id)

    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('app_juegos:listar_juegos')
    else:
        form = JuegoForm(instance=juego)
        contexto = {'form':form}
    return render(request,'app_juegos/juego_update.html', contexto)
