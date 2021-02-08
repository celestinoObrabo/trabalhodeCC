from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import TaskForm,CommentForm,UploadForm
from django.http import HttpResponse
from .models import Orientacao
from django.contrib import messages
import datetime
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

from .models import Task,Orientacao,Comment,Arquivos



def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    comment = Comment.objects.filter(task=task).order_by('-id')
    arquivos = Arquivos.objects.filter(task = task).order_by('-id')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        upload_form = UploadForm(request.POST or None, request.FILES)

        if upload_form.is_valid():
            arquivos = upload_form.save(commit = False)
            arquivos.task = task
            arquivos.save()
            return redirect('/task/view/' + str(task.id))

        if comment_form.is_valid():
            content = request.POST.get('content')
            user = request.POST.get('user')
            comment = Comment.objects.create(task = task, content = content, user=user)
            comment.save()
            return redirect('/task/view/'+ str(task.id))
    else:
        comment_form = CommentForm()
        upload_form = UploadForm()

    return render(request, 'tasks/task.html', {'task': task,'comments':comment, 'comment_form':comment_form,
                                                 'arquivos': arquivos, 'upload_form': upload_form})



def taskList(request,id):
    orientacao = get_object_or_404(Orientacao, pk = id)
    filter = request.GET.get('filter')
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search, orientacao=orientacao)
    elif filter:
        tasks = Task.objects.filter(done=filter, orientacao = orientacao)
    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(orientacao = orientacao)
        paginator = Paginator(tasks_list, 6)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.orientacao = orientacao

            task.save()
            return redirect('/task/'+ str(task.orientacao.id))
    else:
        form = TaskForm()
    return render(request, 'tasks/list.html',
                  {'tasks': tasks,'form': form})




def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid()):
            task.save()
            return redirect('/task/'+ str(task.orientacao.id))
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})



def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/task/'+ str(task.orientacao.id))

def deleteFile(request,id):
    arquivos = get_object_or_404(Arquivos,pk = id)
    arquivos.delete()

    messages.info(request, 'Arquivo deletado com sucesso!')

    return redirect('/task/view/'+ str(arquivos.task.id))

def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if (task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/task/'+ str(task.orientacao.id))

def deleteComment(request,id):
    comment = get_object_or_404(Comment, pk = id)
    comment.delete()

    return redirect('/task/view/' + str(comment.task.id))

def sendEmail(request):
    html_content = render_to_string("tasks/emails/send_email.html")
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        'teste',
        text_content,
        'from@example.com',
        ['to@example.com']
    )

    email.attach_alternative(html_content,'text/html')
    email.send()


    return HttpResponse('Mail successfully sent')
