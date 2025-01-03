
from django.shortcuts import get_object_or_404, render, redirect
from .models import Juego, Comentario, Categoria, Pedido
from .forms import CategoriaForm, JuegoForm, ClienteForm, PedidoForm, ComentarioForm




def listar_juegos(request):
    juegos = Juego.objects.all()
    contexto = {'juegos': juegos}
    return render(request,'app_juegos/juego_list.html', contexto)

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_juegos:lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'app_juegos/categoria_create.html', {'form': form})

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_juegos:listar_juegos')
    else:
        form = JuegoForm()
    return render(request, 'app_juegos/juego_create.html', {'form': form})


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
    juegos = Juego.objects.all()
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_juegos:lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'app_juegos/pedido_create.html', {'form': form, 'juegos':juegos})

def buscar_juego(request):
    juegos = None 
    if 'nombre' in request.GET: 
        nombre = request.GET['nombre'] 
        juegos = Juego.objects.filter(nombre__icontains=nombre) 
    return render(request, 'app_juegos/buscar_juego.html', {'juegos': juegos})

def delete_juegos(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        juego.delete()
        return redirect('app_juegos:listar_juegos')
    contexto = {'juego' : juego}
    return render(request, 'app_juegos/juego_delete.html',contexto)

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


def add_comment(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.juego = juego
            comentario.creado_por = request.user if request.user.is_authenticated else 'Anónimo'
            comentario.save()
            return redirect('app_juegos:listar_juegos')
    return redirect('app_juegos:listar_juegos')

def lista_categorias(request):
    categorias = Categoria.objects.all() 
    return render(request, 'app_juegos/categoria_list.html', {'categorias': categorias})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'app_juegos/pedidos_list.html' , {'pedidos' : pedidos})

def inicio(request):
    return render(request, 'app_juegos/inicio.html')

def about(request): 
    return render(request, 'app_juegos/about.html')

