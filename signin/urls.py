from django.urls import path
from django.http import Http404, HttpResponseBadRequest
from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
]