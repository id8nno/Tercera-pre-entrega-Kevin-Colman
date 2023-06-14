from django.urls import path
from APP import views

urlpatterns =[
    path("", views.start),
    path("modo_de_juego",views.modo_de_juego),
    path("nickname",views.nickname),
    path("last_update",views.last_update),
]