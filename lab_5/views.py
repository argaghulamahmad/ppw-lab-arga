from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Todo_Form
from .models import Todo

response = {}
def index(request):
    response['author'] = "Arga Ghulam Ahmad"
    todo = Todo.objects.all()
    response['todo'] = todo
    html = 'lab_5/lab_5.html'
    response['todo_form'] = Todo_Form
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