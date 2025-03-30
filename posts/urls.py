from django.urls import path
from .views import python, django, home, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('python/', python, name='python'),
    path('django/', django, name='django'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
