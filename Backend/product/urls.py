from django.urls import path
from . import views
from .views import ProductView

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
    path('', ProductView.index, name='index'),
    path('get_all/', ProductView.as_view({'get': 'get_all'})),
    path('get_product/<str:uuid>/', ProductView.as_view({'get': 'get_product'}), name='myname')
]
