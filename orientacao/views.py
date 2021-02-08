#Para rotas
from django.shortcuts import render, get_object_or_404, redirect, reverse
#Para login
from django.contrib.auth.decorators import login_required
# Para paginação
from django.core.paginator import Paginator
# importou a nossa tabela de cursos
from django.urls import reverse_lazy

from .models import Orientacao
from django.contrib import messages
from .forms import OrientForm, RegisterForm
from django.views.generic.edit import UpdateView, CreateView

@login_required
def index(request):
    # variável que vai concentrar todos os objetos da tabela Orientacao
    orientacoes = Orientacao.objects.all().filter(user = request.user)

    paginator = Paginator(orientacoes,6)
    page = request.GET.get('page')

    orientacoes_2 = paginator.get_page(page)


    context = {
        # Nome dado a um dicionário
    'orientacoes': orientacoes_2

    }
    return render(request, 'orientacao/home.html', context)

@login_required
def details(request,id):
    orientacoes = get_object_or_404(Orientacao,pk = id)
    context = {
        'orientacao': orientacoes
    }
    template_name = 'orientacao/details.html'
    return render(request, template_name, context)
@login_required
def newOrient(request):
    if request.method == 'POST':
        form = OrientForm(request.POST)

        if form.is_valid():
            orientacao = form.save(commit=False)

            orientacao.save()
            return redirect('/orientacao')
    else:
        form = OrientForm()
        return render(request, 'orientacao/addOrient.html', {'form': form})
    
@login_required
def editOrient(request,id):
    orientacao = get_object_or_404(Orientacao, pk=id)
    form = OrientForm(instance=orientacao)

    if (request.method == 'POST'):
        form = OrientForm(request.POST,instance=orientacao)
        if (form.is_valid()):
            orientacao.save()
            return redirect('/orientacao')
        else:
            return render(request, 'orientacao/editOrient.html', {'form': form, 'orientacao': orientacao})
    else:
        return render(request, 'orientacao/editOrient.html', {'form': form, 'orientacao': orientacao})
@login_required
def deleteOrient(request,id):
    orientacao = get_object_or_404(Orientacao, pk=id)
    orientacao.delete()

    messages.info(request, 'Orientação deletada com sucesso!')

    return redirect('/orientacao')


def register(request):
    template_name = 'registration/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request, 'ERRO AO CADASTRAR!')
    else:
        form = RegisterForm()

    context = {
        'form': RegisterForm()
    }
    return render(request, template_name, context)

class OrientacaoUpdateView(UpdateView):
    model = Orientacao
    form_class = OrientForm
    template_name = 'orientacao/editOrient.html'
    success_message = 'As alterações foram efectuadas com sucesso'


    def get_success_url(self):
        return reverse('index')

class OrientacaoCreateView(CreateView):
    model = Orientacao
    fields = ('name', 'description', 'categoria', 'curso', 'user')
    template_name = 'orientacao/addOrient.html'

    def get_context_data(self, **kwargs):
        data = super(OrientacaoCreateView, self).get_context_data(**kwargs)
        return data

    def get_success_url(self):
        return reverse_lazy('index')


