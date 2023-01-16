from django.urls import path
from . import views


app_name = "product"
#URL
urlpatterns = [
    path('', views.index(), name='index')
]