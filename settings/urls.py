from django.urls import path

from  settings.views import nok

urlpatterns = [
    path('',nok,name='nok')
]