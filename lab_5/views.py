from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Todo_Form
from .models import Todo

response = {}
def index(request):
    todo = Todo.objects.all()
    response['todo'] = todo
    response['todo_form'] = Todo_Form
    if 'user_login' in request.session:
        html = 'lab_5/lab_5.html'
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_session'] = True
        return render(request, html, response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)

def add_todo(request):
    form = Todo_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['title'] = request.POST['title']
        response['description'] = request.POST['description']
        todo = Todo(title=response['title'],description=response['description'])
        todo.save()
        return HttpResponseRedirect('/lab-5/')
    else:
        return HttpResponseRedirect('/lab-5/')

def delete_todo(request, uid):
    p = Todo.objects.get(id=uid)
    p.delete()
    return HttpResponseRedirect('/lab-5/')