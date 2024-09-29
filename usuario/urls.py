from django.urls import path
from .views import register_view, login_view, logout_view, menu_principal, ingresar_azucar, ingresar_vegano, ingresar_gluten, about


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  #cerrar sesion
    path('menu/', menu_principal, name='menu_principal'),  #menu principal
    path('buscar/', menu_principal, name='buscar_producto'),  #buscar
    path('ingresar_azucar/', ingresar_azucar, name='ingresar_azucar'),
    path('ingresar_vegano/', ingresar_vegano, name='ingresar_vegano'),
    path('ingresar_gluten/', ingresar_gluten, name='ingresar_gluten'),
    path('about/', about, name='about'), #presentacion & linkedin

]

