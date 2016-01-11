from django.shortcuts import render,get_object_or_404,redirect

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from noticias.models import *

from noticias.forms import *
# Create your views here.

from django.contrib import messages


def listado(request):
	noticias = Noticia.objects.all()
	paginator = Paginator(noticias,2)

	try: 
		pagina = int(request.GET.get("page",1))
	except ValueError: 
		pagina = 1

	try: 
		noticias = paginator.page(pagina)
	except (InvalidPage, EmptyPage): 
		noticias = paginator.page(paginator.num_pages)

	context = {
		'noticias'	: noticias
	}
	return render(request, "listado.html",context)

def ver(request,pk):
	idnoticia = Noticia.objects.get(pk=int(pk))
	print idnoticia
	context = {
		'noticia'	: idnoticia
	}
	return render(request, "ver.html",context)

def add(request):
	if request.method == 'POST' :
		noticia = Noticia()
		form = NoticiaForm(request.POST, instance = noticia)
		if form.is_valid():
			form.save()
			messages.success(request, 'Anadido OK')
			return redirect('listado')
		else:
			messages.error(request, 'Danger')
	else :
		form = NoticiaForm()

	context = { 'form': form,}
	return render(request,'add.html', context)

def editar(request,pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	if request.method == 'POST':
		form = NoticiaForm(request.POST, instance = noticia)
 
		if form.is_valid():
			form.save()
			messages.success(request, 'Editado OK')
			return redirect('listado')
		else:
			messages.error(request, 'Danger')
	else:
		form = NoticiaForm(instance = noticia)
        context = { 'form': form,}
	return render(request,'editar.html', context)

def borrar(request,pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	noticia.delete()
	messages.success(request, 'Borrado OK')

	return redirect('listado')