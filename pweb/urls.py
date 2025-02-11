from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # URL para a página inicial (home app)
    path('', include('home.urls')),  # Isso inclui as URLs da aplicação 'home'
    
    # URL para acessar o painel administrativo do Django
    path('admin/', admin.site.urls),
    
    # URL para login, usando a view LoginView do Django com um template customizado
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # URL para logout, usando a view LogoutView do Django e redirecionando para a página de login após o logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

