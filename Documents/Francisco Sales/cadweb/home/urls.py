from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categorias/', views.categorias, name="categorias"),
    # path('', views.menu, name="menu.html"),
]