from django.conf.urls import url

from . import views

urlpatterns = [
    # Auth API
    url(r'^$', views.index, name='index'),
	url(r'^throw$', views.throw, name='throw'),
	url(r'^log_error$', views.log_error, name='log_error'),
]