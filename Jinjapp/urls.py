from django.urls import path
from Jinjapp import views

urlpatterns = [
    path('', views.index, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('images/', views.gallery, name='my_gallery'),

]
