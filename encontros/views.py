from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .forms import EncontrosForms
from django.core.paginator import Paginator
from .models import Encontros,Orientacao

# Create your views here.

def home(request,id):
    orientacao = get_object_or_404(Orientacao, pk=id)
    encontros = Encontros.objects.all().filter(orientacao=orientacao)
    print(id)

    paginator = Paginator(encontros, 6)
    page = request.GET.get('page')
    encontros_2 = paginator.get_page(page)

    if request.method == 'POST':
        form = EncontrosForms(request.POST)

        if form.is_valid():
            encontros = form.save(commit=False)
            encontros.orientacao = orientacao
            encontros.save()
            return redirect('/encontros/'+ str(encontros.orientacao.id))
    else:
        form = EncontrosForms()

    context = {
        'encontros' : encontros_2,
            'form': form
        }
    return render(request,'encontros/home.html', context)

def deleteEncontro(request,id):
    encontros = get_object_or_404(Encontros,pk = id)
    encontros.delete()

    messages.info(request, 'Encontro deletado com sucesso!')

    return redirect('/encontros/'+ str(encontros.orientacao.id))
def editEncontro(request,id):
    encontros = get_object_or_404(Encontros, pk=id)
    form = EncontrosForms(instance=encontros)

    if (request.method == 'POST'):
        form = EncontrosForms(request.POST, instance=encontros)

        if (form.is_valid()):
            encontros.save()
            return redirect('/encontros/'+ str(encontros.orientacao.id))
        else:
            return render(request, 'encontros/editEncontro.html', {'form': form, 'encontro':encontros})
    else:
        return render(request, 'encontros/editEncontro.html', {'form': form, 'encontro':encontros})
