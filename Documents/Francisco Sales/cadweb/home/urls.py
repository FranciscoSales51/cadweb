from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="index,html"),
    path('', views.base, name="base.html"),
    path('', views.menu, name="menu.html"),
]