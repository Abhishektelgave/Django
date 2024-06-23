from django.urls import path
from . import views

urlpatterns = [
    path('',views.datetime_with_offset,name='datetime_with_offset')
]