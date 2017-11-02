from django.shortcuts import render

response = {}
def index(request):
    response['author'] = "Arga Ghulam Ahmad"
    html = 'lab_6/lab_6.html'
    return render(request, html, response)