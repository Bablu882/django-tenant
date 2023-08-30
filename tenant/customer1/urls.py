from django.urls import path
from .views import *


urlpatterns=[
    path('organisation',my_team,name='organisation')
]