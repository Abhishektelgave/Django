from django.urls import path
from . import views

urlpatterns = [
    path('', views.curr_dateTime, name='curr_dateTime'),
]