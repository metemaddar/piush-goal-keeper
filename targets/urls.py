from django.urls import path
from .views import *

app_name = 'targets'

urlpatterns = [
    path('',index, name='index')
]