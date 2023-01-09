from django.urls import path
from app2.views import *

app_name=('dg')

urlpatterns=[

    path('secondapp/',secondapp,name='secondapp'),
]