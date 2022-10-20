
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactuss/',views.contactuss,name='contactus'),
    path('contactsave/',views.contactsave,name='contact_save'),
]