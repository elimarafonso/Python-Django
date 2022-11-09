
from django.shortcuts import render, redirect
'''consegue adicionar mensagens na página
'''
from django.contrib import messages

# Create your views here.
# importando formulário
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }
    return render(request, 'index.html',context)


def contato(request):
    # chamando a instanacia do formulário
    # quando receber um post o formulário tem dados OU se nao passar o form é zerado
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao envia mensagem!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    user = str(request.user)
    if user.upper() == 'AnonymousUser'.upper():
        return redirect('index')
    else:
        if str(request.method) == 'POST':
            # request.FILES porque o formulario vai receber um FILE/arquivo
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                prod = form.save()
                messages.success(request, f'Produto cadastrado <{prod}>')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao cadastrar produto!')

        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)

