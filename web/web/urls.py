"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from motogp import views
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),

    #url(r'^category/(?P<pk>\d+)/$', views.category, name='category'),
    url(r'^login/$', views.login, name='login'),

    #=== Index ===
    url(r'^$', views.index, name='index'),

    #=== Sign Up ===
    url(r'^signup/$', views.signup, name='signup'),

    #=== Logout ===
    url(r'^logout/$', views.logout_view, name='logout'),

    #=== Manager ===
    url(r'^manager/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^manager/afterrace/$', views.afterrace, name='afterrace'),
    url(r'^manager/operation/$', views.operation, name='operation'),
    url(r'^manager/operation/\?reset_price_rider$', views.operation, name='reset_price_rider'),

    #=== Game View ===
    url(r'^debut/$', views.debut, name='debut'),
    url(r'^home/$', views.home, name='home'),
    url(r'^market/$', views.market, name='market'),
    url(r'^myriders/$', views.myriders, name='myriders'),
    url(r'^myteam/$', views.myteam, name='myteam'),
    url(r'^ranking/$', views.ranking, name='ranking'),
    url(r'^setting/email/$', views.change_email, name='change_email'),
    url(r'^setting/pass$', views.change_pass, name='change_pass'),
    url(r'^setting/delete$', views.delete_account, name='delete_account'),

    #=== Game My Team ====
    url(r'^myteam/\?inscribe$', views.myteam, name='inscribe'),
    url(r'^myteam/\?maintenance$', views.myteam, name='maintenance'),
    url(r'^myteam/\?loan$', views.myteam, name='loan'),
    url(r'^myteam/\?owe$', views.myteam, name='owe'),

    #=== Game Rider ====
    url(r'^myriders/\?id=(?P<pk>\d+)$', views.myriders, name='sell_rider'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',(r'^motogp/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))