from django.shortcuts import render,redirect
#login
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from django.views.generic import TemplateView, ListView, DetailView


from django.contrib import messages


from .models import *
from .forms import *
# Create your views here.


def login_view(request):
	if request.user.is_authenticated():
		return redirect('/listado')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if user.is_superuser:
					return redirect('dashboard')
				else:
					return redirect('/')
			else:
				messages.error(request, 'La cuenta esta desactivada o ha sido eliminada')	
				return redirect('index')

		messages.error(request, 'Nombre de usuario o contrasena no valido')	

	return render(request, "login.html",{'form':LoginForm()})


def signup(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = SignupForm(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            photo = cleaned_data.get('photo')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Anadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo (el campo, permite datos null)
            user_profile.photo = photo
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.
            messages.success(request, 'Te has registrado con exito.')
            return redirect('debut')
    else:
        # Si el mthod es GET, instanciamos un objeto SignupForm vacio
        form = SignupForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'signup.html', context)


def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado con exito.')
	return redirect('/')

@login_required
def test_login(request):
	return render(request, 'test_login.html')

#from django.views.generic import TemplateView, ListView, DetailView
#CreateView, UpdateView, Delete View

class UserDetailView(DetailView): #Listar objetos
	model = UserProfile
	template_name="user_list.html"

class clase2(TemplateView): #consultas mas simples
	template_name="clase2_list.html"

class clase3(DetailView): #traer un objeto de la bbdd
	template_name="clase3_list.html"

