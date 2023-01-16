from django.urls import path
from . import views

"""
File that contains routes which point to functions in /product/views
"""

app_name = "product"

"""
First arg is route extension
Second arg is function
Third arg is route name
"""
urlpatterns = [
    path('', views.index, name='index'),
]
