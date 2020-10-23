from django.shortcuts import render
from .models import SliderIndex,Insumos,MisionyVision

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_autent
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def index(request):
    sliders = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'imagenes':sliders})

def misionyvision(request):
    lista = MisionyVision.objects.all()
    return render(request,'web/mision_vision.html',{'lista':lista})

@login_required(login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("txtProducto")
        precio = request.POST.get("txtPrecio")
        descr  = request.POST.get("txtDescripcion")
        stock  = request.POST.get("txtStock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descr
            insumo.stock = stock
            insumo.save()
            msg = 'Modifico'
        except:
            msg = 'No Modifico'
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'msg':msg})

    
@login_required(login_url='/login/')
def buscar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/formulario_insumo_mod.html',{'insumo':insumo})
    except:
        msg='no existe insumo'
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
@permission_required('myCar.delete_insumos',login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino Insumo'
    except:
        msg='No Elimino'
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def lista_insumos(request):
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista})

@login_required(login_url='/login/')
@permission_required('myCar.add_insumos',login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("txtProducto")
        precio = request.POST.get("txtPrecio")
        descr  = request.POST.get("txtDescripcion")
        stock  = request.POST.get("txtStock")

        insumo= Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descr,
            stock=stock
        )

        insumo.save()
        return render(request,'web/formulario_insumos.html',{'msg':'grabo insumo'})
    return render(request,'web/formulario_insumos.html')

def galeria(request):
    return render(request,'web/galeria2.html')

@login_required(login_url='/login/')
@permission_required('auth.add_user',login_url='/login/')
def registro(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtNombreusuario")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")
        if pass1!=pass2:
            return render(request,'web/registro.html',{'msg':'claves incorrectas'})        
        try:
            usu = User.objects.get(username=usuario)
            return render(request,'web/registro.html',{'msg':'usuario existe'})
        except:            
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.username = usuario
            usu.set_password(pass1)

            usu.save()

            usu = authenticate(request,username=usuario, password=pass1)
            login_autent(request,usu)
            sliders = SliderIndex.objects.all()
            return render(request,'web/index2.html',{'imagenes':sliders})

    return render(request,'web/registro.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombreusuario")
        password = request.POST.get("txtPass1")
        usu = authenticate(request,username=usuario, password=password)
        if usu is not None and usu.is_active:
            login_autent(request,usu)
            sliders = SliderIndex.objects.all()
            return render(request,'web/index2.html',{'imagenes':sliders})           
        else:
            return render(request,'web/login.html',{'msg':'no existe usuario'})
    return render(request,'web/login.html')

def cerrar(request):
    logout(request)
    sliders = SliderIndex.objects.all()
    return render(request,'web/index2.html',{'imagenes':sliders})