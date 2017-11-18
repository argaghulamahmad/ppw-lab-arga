from django.shortcuts import render

response = {}

def index(request):
    response = {'author': 'Arga Ghulam Ahmad'}
    html = 'lab_8/lab_8.html'
    return render(request, html, response)