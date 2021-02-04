from django.urls import path
from . import views

app_name = 'taches'

urlpatterns = [
    path('',views.get_acceuil, name='get_acceuil'),
    path('add_tache/',views.add_tache, name='add_tache'),
    path('<str:slug>/',views.tache_type, name='tache_type'),
    path('detail/<int:id>/',views.detail, name='detail'),
]
