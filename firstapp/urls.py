from django.urls import path
from . import views

urlpatterns = [
    path('', views.sotrudnik_list, name='sotrudnik_list'), ]
# Create your views here.
