from django import forms
from noticias.models import *
from django.forms import ModelForm

class NoticiaForm (forms.ModelForm):
	class Meta:
		model = Noticia
		fields = '__all__'