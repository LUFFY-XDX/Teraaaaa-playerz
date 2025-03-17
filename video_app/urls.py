from django.urls import path
from .views import index, generate_link

urlpatterns = [
    path('', index, name='index'),
    path('generate/', generate_link, name='direct_link'),
]
