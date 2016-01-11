from django.shortcuts import render,render_to_response,redirect

#Pagina 404
from django.shortcuts import get_object_or_404
#from django.http import Http404

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

#login
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from django.contrib import messages

#Para formularios:
from motogp.forms import *
from django.template import RequestContext

#Modelos
from motogp.models import *

#Fechas
from datetime import datetime, date, time, timedelta
import calendar

import random

PAGES_PAGINATION = 15

###########################################
#               AUXILIAR
###########################################
def isGameBlock():
	if int(Configuration.objects.get(name='GAME_BLOCK').value) == 0:
		return False
	else:
		return True

def sendMessageGameBlock(request):
	if isGameBlock():
		messages.warning(request, 'El juego esta bloqueado, no podras hacer ninguna operacion')

def isUpdate():
	last_date_update = Configuration.objects.get(name='LAST_DATE_UPDATE').value
	last_date_update = datetime.strptime(last_date_update, '%Y-%m-%d %H:%M:%S')

	today = datetime.today()
	today = datetime(today.year, today.month, today.day)

	if today > last_date_update:
		return False
	else:
		return True

def updateGame():
	if not isUpdate():
		#Bloquear juego
		next_block_race = Race.objects.filter(date_race__gte=date.today()).order_by("date_block")[:1][0].date_block
		next_block_race = datetime(next_block_race.year, next_block_race.month, next_block_race.day)

		today = datetime.today()
		today = datetime(today.year, today.month, today.day)

		if today == next_block_race:
			gameBlock = Configuration.objects.get(name='GAME_BLOCK')
			gameBlock.value = 1
			gameBlock.save()

		#Actualizar jugadores en mercado
		leagues = League.objects.all()
		for league in leagues:
			riders = list(Rider.objects.all())
			market = []
			while len(market) < len(riders)/2:
				rider_random = random.choice(riders)
				riders.remove(rider_random)
				market.append(rider_random)
			league.rider_on_sale = market
			league.save()

		#actualizar la fecha de actualizacion
		last_date_update = Configuration.objects.get(name='LAST_DATE_UPDATE')
		last_date_update.value = today
		last_date_update.save()
	

###########################################
#               INDEX
###########################################

def index(request):
	if request.user.is_authenticated():
		return redirect('home')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				updateGame()
				if user.is_superuser:
					return redirect('dashboard')
				else:
					if user.userprofile.debut == True:
						messages.info(request, 'Puedes crear un equipo y unirte a una liga')	
						return redirect('debut')
					else:
						return redirect('home')
			else:
				messages.error(request, 'La cuenta esta desactivada o ha sido eliminada')	
				return redirect('index')

		messages.error(request, 'Nombre de usuario o contrasena no valido')	

	return render(request, "index.html")

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
	return redirect('index')

###########################################
#               GAME
###########################################

@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, request=request)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'El email ha sido cambiado con exito!.')
            return render(request, 'game/setting/changeEmail.html', {'form': form})
    else:
        form = ChangeEmailForm(
            request=request,
            initial={'email': request.user.email})
    return render(request, 'game/setting/changeEmail.html', {'form': form})

@login_required
def change_pass(request):
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
            messages.success(request, 'La contrasena ha sido cambiado con exito!.')
            messages.success(request, 'Es necesario introducir los datos para entrar.')
            return render(request, 'game/setting/changePass.html', {'form': form})
    else:
        form = ChangePassForm()
    return render(request, 'game/setting/changePass.html', {'form': form})

@login_required
def delete_account(request):
	if request.method == 'POST':
		request.user.is_active=False
		logout(request)
		messages.success(request, 'Has borrado tu cuenta con exito.')
		return redirect('index')
	return render(request, "game/setting/deleteAccount.html")

@login_required
def debut(request):
	if request.user.userprofile.debut == False:
		return redirect('home')

	form = DebutForm()
	if request.method == 'POST':
		form = DebutForm(request.POST)
		if form.is_valid():
			name_team=form.cleaned_data.get('name_team')
			name_league=form.cleaned_data.get('name_league')
			create = form.cleaned_data.get('create')
			
			league = League()
			exist_league = League.objects.filter(name=name_league)

			if create == '1': #Crea una liga nueva
				if not exist_league:
					league = League(name=name_league)
					league.save()
				else:
					messages.error(request, 'El nombre de la liga introducido ya existe.')
					return render(request, 'game/debut/debut.html', {'form': form})
			elif create == '0': #Se une a una liga ya existente
				if not exist_league:
					messages.error(request, 'El nombre de la liga introducido no existe.')
					return render(request, 'game/debut/debut.html', {'form': form})
				else:
					league = League.objects.get(name=name_league)
					
			coin = int(Configuration.objects.get(name='PRICE_INIT_TEAM').value)
			uteam = Uteam(name=name_team, coin=coin)
			uteam.save()

			request.user.userprofile.uteam = uteam

			request.user.userprofile.league = league

			request.user.userprofile.debut = False

			request.user.userprofile.save()

			messages.success(request, 'Equipo creado. Ya puedes comenzar a jugar')
			return redirect('myteam')

	return render(request, 'game/debut/debut.html', {'form': form})

@login_required
def home(request):
	sendMessageGameBlock(request)

	next_race = Race.objects.filter(date_race__gte=date.today()).order_by("date_race")[:1]
	races = Race.objects.all()
	countries = Country.objects.all()
	context = {
		'next_race': str(next_race[0].date_block),
		'races' : races,
		'countries' : countries,
	}

	return render(request, 'game/home/home.html',context)

@login_required
def market(request):
	sendMessageGameBlock(request)

	league=request.user.userprofile.league
	riders = Rider.objects.filter(league=league)
	
	if request.method == 'POST':
		if isGameBlock():
			messages.error(request, 'No puede hacer esta accion mientras haya una carrera.')
			return False
		else:	
			nro_riders = int(Configuration.objects.get(name='MAX_RIDERS_BY_UTEAM').value)
			uteam=request.user.userprofile.uteam
			
			if 'id' in request.POST and uteam.rider.count()<nro_riders:	
				rider = Rider.objects.get(pk=request.POST['id'])
				if uteam.coin >= rider.price:
					uteam.rider.add(rider)
					uteam.coin -= rider.price
					uteam.save()
					league.rider_on_sale.remove(rider)
					rider.save()
					messages.success(request, 'Enhorabuena, has comprado el piloto')
				else:
					messages.error(request, 'No tienes suficiente dinero.')
					return False
			else:
				return False

	return render(request, "game/market/market.html",{'riders': riders})

@login_required
def myriders(request):
	sendMessageGameBlock(request)

	riders = Rider.objects.filter(uteam=request.user.userprofile.uteam)
	
	if request.method == 'POST':
		if isGameBlock():
			messages.error(request, 'No puede hacer esta accion mientras haya una carrera.')
			return False
		else:	
			uteam=request.user.userprofile.uteam
			league=request.user.userprofile.league
			if 'id' in request.POST:
				rider = Rider.objects.get(pk=request.POST['id'])
				uteam.rider.remove(rider)
				uteam.coin += rider.price_on_sale
				uteam.save()
				league.rider_on_sale.add(rider)
				rider.save()

	
	return render(request, "game/myriders/myriders.html",{'riders': riders})

@login_required
def myteam(request):
	sendMessageGameBlock(request)

	uteam=request.user.userprofile.uteam
	#Pagar la inscripcion
	if 'inscribe' in request.GET:
		if isGameBlock():
			messages.error(request, 'No puede hacer esta accion mientras haya una carrera.')
		else:
			if uteam.enrolment != True:
				price = int((Configuration.objects.get(name='PRICE_ENROLMENT')).value)
				if int(uteam.coin) >= price:
					uteam.coin -= price
					uteam.enrolment = True
					uteam.save()
					messages.success(request, 'Pagar Inscripcion.')
				else:
					messages.error(request, 'No tienes suficiente dinero.')
			else:
				messages.error(request, 'Ya has pagado la inscripcion')
	#Pagar el mantenimiento
	if 'maintenance' in request.GET:
		if isGameBlock():
			messages.error(request, 'No puede hacer esta accion mientras haya una carrera.')
		else:
			if uteam.maintenance != True:
				price = int((Configuration.objects.get(name='PRICE_MAINTENANCE')).value)
				if int(uteam.coin) >= price:
					uteam.coin -= price
					uteam.maintenance = True
					uteam.save()
					messages.success(request, 'Pagar Inscripcion.')
				else:
					messages.error(request, 'No tienes suficiente dinero.')
			else:
				messages.error(request, 'Ya has pagado el mantenimiento.')
	#Pedir el prestamo
	if 'loan' in request.GET:
		if isGameBlock():
			messages.error(request, 'No puede hacer esta accion mientras haya una carrera.')
		else:
			if uteam.loan != True:
				loan = int((Configuration.objects.get(name='LOAN')).value)
				uteam.owe += loan
				uteam.coin += loan
				uteam.loan = True
				uteam.save()
				messages.success(request, 'Has pedido un prestamo de %s.' % loan)
			else:
				messages.error(request, 'Ya tienes un prestamo pedido.')
	#Pagar la deuda
	if request.method == 'POST' and uteam.loan != False:
		if isGameBlock():
			messages.error(request, 'No puede hacer esta accion mientras haya una carrera.')
		else:
			form = PayLoanForm(request.POST)
			if form.is_valid():
				qty_loan=int(form.cleaned_data['qty_loan'])
				if int(uteam.coin) >= qty_loan:
					if uteam.owe >= qty_loan:
						uteam.owe -= qty_loan
						uteam.coin -= qty_loan
						if uteam.owe == 0:
							uteam.loan = False
							messages.success(request, 'Has pagado toda la deuda')
						else:
							messages.success(request, 'Has pagado un prestamo de %s' % qty_loan)
						uteam.save() 
					else:
						messages.error(request, 'Err.')
				else:
					messages.error(request, 'No tienes suficiente dinero.')
				
			else:
				messages.error(request, 'No tienes ningun pago pendiente.')

	riders = Rider.objects.filter(uteam=uteam)
	form = PayLoanForm()

	context = {
		'riders': riders,
		'form': form,
		'maintenance' : Configuration.objects.get(name='PRICE_MAINTENANCE'),
		'enrolment' : Configuration.objects.get(name='PRICE_ENROLMENT'),
		'tooltip_enrolment' : 'Debes inscribirte en el proximo gran premio para que puedan correr tus pilotos',
		'tooltip_maintenance' : 'Debes pagar el mantenimiento del equipo antes del gran premio (combustible, neumaticos...)',
		'tooltip_loan' : 'Puedes pedir un prestamo que puedes devolver mas adelante',
		'tooltip_owe' : 'Puedes pagar la deuda que tienes'
		}
	return render(request, "game/myteam/myteam.html",context)

@login_required
def ranking(request):
	sendMessageGameBlock(request)

	league=request.user.userprofile.league
	users = UserProfile.objects.filter(league=league)
	paginator = Paginator(users,PAGES_PAGINATION)

	try: 
		pagina = int(request.GET.get("page",1))
	except ValueError: 
		pagina = 1

	try: 
		users = paginator.page(pagina)
	except (InvalidPage, EmptyPage): 
		users = paginator.page(paginator.num_pages)

	context = {
		'users'			: users,
	}
	return render(request, "game/ranking/ranking.html",context)

###########################################
#               MANAGER
###########################################


@login_required
def dashboard(request):
	sendMessageGameBlock(request)

	if not request.user.is_superuser:
		return redirect('home')

	return render(request, "manager/dashboard/dashboard.html")

@login_required
def afterrace(request):
	sendMessageGameBlock(request)

	if not request.user.is_superuser:
		return redirect('home')

	categories = Category.objects.all()
	lista = []
	for i in range(0,categories.count()):
		lista.append([])
		teams = Team.objects.all().filter(category=categories[i])
		riders = Rider.objects.all().filter(team=teams)
		lista[i] = riders


	if request.method == 'POST':
		riders = Rider.objects.all()
		points = (Configuration.objects.get(name='POINT').value).split("-")
		position_no_point = len(points)+1
		calc_value = int(Configuration.objects.get(name='CALCULATE_VALUE_RIDER').value)
		coin_by_point = int(Configuration.objects.get(name='COIN_BY_POINT').value)

		for rider in riders:
			pos = int(request.POST['rider_'+str(rider.pk)])
			rider.updateAfterRace(pos,int(points[pos-1]),calc_value,position_no_point)
			uteams = Uteam.objects.filter(rider=rider)
			for uteam in uteams:
				uteam.updateAfterRace(int(points[pos-1]),coin_by_point)
			
		gameBlock = Configuration.objects.get(name='GAME_BLOCK')
		gameBlock.value = 0
		gameBlock.save()
		messages.success(request, 'Se han actualizado los pilotos')
			

	context = {
		'lista': lista,
		'categories':categories,
	}

	return render(request, "manager/afterrace/afterrace.html",context)

@login_required
def operation(request):
	sendMessageGameBlock(request)

	if not request.user.is_superuser:
		return redirect('home')

	#establecemos el precio, el sueldo y el precio de venta a cada jugador por defecto
	if 'reset_price_rider' in request.GET:
		margin_sell = float(Configuration.objects.get(name='MARGIN_SELL').value)
		margin_salary = float(Configuration.objects.get(name='MARGIN_SALARY').value)
		riders = Rider.objects.all()
		for rider in riders:
			rider.resetValues(margin_sell,margin_salary)


	return render(request, "manager/operation/operation.html")

###########################################
#               TEST
###########################################

"""def category(request,pk):

	#try:
	#	idCategory = Category.objects.get(id_category=int(id_category))
	#except Category.DoesNotExist:
	#	raise Http404

	#category = get_object_or_404(Category, pk=int(pk))
	
	return render(request, 
		"category/category.html",
		dict(
			category = category, 
			usuario = request.user,
		))"""