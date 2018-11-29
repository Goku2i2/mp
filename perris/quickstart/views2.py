from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from perris.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

#MENSAJES
from django.contrib import messages
#Importamos los modelos de los perros
from perris.models import Perros_Rescatados
#Importamos el Formulario 
from perris.forms import Perro_RescatadoForm

#Para redirigir las vistas 
from django.contrib.auth.decorators import login_required, permission_required

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
def inicio(request):
	# Se van agregar los post a la platilla.html
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/inicio.html',  {'perros': perros})
       


def home(request):
	return render(request, 'inicio.html')



#Metodo que nos redirecciones a un sitio para cada tipo de usuario

def redirigir(request):

    user = request.user
    perros = Perros_Rescatados.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    if user.has_perm('perris.admin'):
        return render(request, 'perris/adm.inicio.html', {'perros': perros}) 
    else:
        return render(request, 'perris/perros_disponibles.html',{'perros': perros})   


def login(request):
    return render(request, 'registration/login.html', {})

def perros_disponibles(request):
	#Mostrar los perros disponibles 
	# Se van agregar los post a la platilla.html
    # Hacer que en la lista aparezcan solo los usuarios disponibles 
    perros = Perros_Rescatados.objects.filter( estado="Disponible")
    return render(request, 'perris/perros_disponibles.html', {'perros': perros})




def administrador_inicio(request):
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/adm.inicio.html', {'perros': perros})


#Vista del Agregar un nuevo post de perro rescatadoo
def new_post_perro(request):
    form = Perro_RescatadoForm()
    return render(request, 'perris/adm.perro_post_add.html', {'form': form})



#Guardar los datos del Formulario del Perro rescatado en la BD 
def new_post_perro(request):
   if request.method == "POST":
       form = Perro_RescatadoForm(request.POST or None , request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           messages.info(request, 'El nuevo perro ha sido agregado')
           return redirect('adm.inicio')
   else:
       form = Perro_RescatadoForm()
   return render(request, 'perris/adm.perro_post_add.html', {'form': form})

#Ver mas detalles del Post Perro
#Detalle del Post
def detail_post_perro(request, pk):
    perros = get_object_or_404(Perros_Rescatados, pk=pk)
    return render(request, 'perris/adm.perro_post_detail.html', {'perro': perros})

#Modificar el POST de Perros y guardarlo
def edit_post_perro(request, pk):
    post = get_object_or_404(Perros_Rescatados, pk=pk)
    if request.method == "POST":
        form = Perro_RescatadoForm(request.POST or None , request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('detail_post_perro', pk=post.pk)
            messages.info(request, 'Se actualizó la información')
            return redirect('adm.inicio')
    else:
        form = Perro_RescatadoForm(instance=post)
    return render(request, 'perris/adm.perro_post_edit.html', {'form': form})

#Eliminar el post del perro
def delete_post_perro (request , pk):
    perros=Perros_Rescatados.objects.get(pk=pk)
    if request.method =="POST":
        perros.delete()
        messages.info(request, 'Se eliminó la información')
        return redirect ('adm.inicio')
    return render(request, 'perris/adm.perro_post_delete.html', {'perro': perros})
