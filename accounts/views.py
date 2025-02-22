from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Tentando autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # ou redirecione para a página que você deseja
        else:
            messages.error(request, "Login Incorreto!")
            return render(request, 'login.html')
    
    return render(request, 'login.html')
