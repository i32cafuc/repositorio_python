from django.conf.urls import url

from . import views
from .models import *

urlpatterns = [
    url(r'^registro/$', views.signup, name='accounts.registro'),
    url(r'^login/$', views.login_view, name='accounts.login'),
    url(r'^logout/$', views.logout_view, name='accounts.login'),
    url(r'^test/$', views.test_login, name='accounts.login'),

    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='user-detail'),
]