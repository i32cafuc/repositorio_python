from django.conf.urls import patterns, include, url
from django.contrib import admin

from noticias import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'periodico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^ver/(?P<pk>\d+)/$',views.ver, name="ver"),
    url(r'^listado/$',views.listado,name="listado"),
    url(r'^add/$',views.add,name="add"),
    url(r'^editar/(?P<pk>\d+)/$',views.editar, name="editar"),
    url(r'^borrar/(?P<pk>\d+)/$',views.borrar, name="borrar"),


    url(r'^accounts/', include('accounts.urls')),

)
