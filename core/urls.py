from django.urls import path
from django.conf.urls.static import static

from .views import register_metherelogic, query_metherelogic

urlpatterns = [
    path('register_metherelogic', register_metherelogic, name='register_metherelogic'),
    path('query_metherelogic', query_metherelogic, name='query_metherelogic'),
    ]