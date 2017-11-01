from django.shortcuts import render

def index(request):
    html = 'lab_6/lab_6.html'
    return render(request, html)