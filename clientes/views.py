from django.shortcuts import render, redirect
from django.contrib import messages # Importe isso
from .models import Cliente

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Cliente.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone
        )
        
        # Adiciona a mensagem de sucesso
        messages.success(request, f'Cliente {nome} cadastrado com sucesso!')
        return redirect('cadastrar_cliente')

    return render(request, 'clientes/cadastro.html')