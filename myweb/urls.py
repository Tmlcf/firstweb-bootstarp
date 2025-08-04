from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('loopdata/', views.skills, name='loopdata'),
    path('for/', views.for_view, name='for'),
]