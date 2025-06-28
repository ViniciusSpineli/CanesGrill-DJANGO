from django.urls import path
from .views import index, churrasco
urlpatterns = [
    path('', index),
    #path('churrasco',churrasco),   
    path('<int:id>', churrasco, name='churrasco')
]
