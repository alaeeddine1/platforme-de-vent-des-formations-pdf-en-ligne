from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('client',views.client,name='client'),
    path('compte',views.Compte,name='compte'),
    path('login',views.login,name='login'),
    path('panier',views.panier,name='panier'),
    path('reservation',views.reservations,name='reservation'),
    path('telecharger', views.telecharger, name='telecharger'),
    path('telecharger_pdf/<int:formation_id>/', views.telecharger_pdf, name='telecharger_pdf'),
    path('paiment',views.paiment,name='paiment'),

]