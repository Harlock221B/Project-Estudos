from django.contrib import messages
from django.shortcuts import render
from .forms import Produto


def produto_index(request):
    return render(request, 'produtos/index.html')


def produtos_form(request):
    produto = Produto(request.POST or None)
    if str(request.method) == 'POST':
        if produto.is_valid():
            nome = produto.cleaned_data['nome']
            preco = produto.cleaned_data['preco']
            quantidade = produto.cleaned_data['quantidade']
            obs = produto.cleaned_data['obs']
            status = produto.cleaned_data['status']
            print(f'{nome}')
            messages.success(request,'Salvo com successo')
            produto = Produto()
        else:
            messages.success(request,'Erro ao cadastar')

    contexto = {'form': produto,'abc':10}

    return render(request, 'produtos/produto_form.html', contexto)


def produtos_salvar(request):
    return render(request, 'produtos/produto_editar.html')


def produtos_deletar(request):
    return render(request, 'produtos/index.html')
