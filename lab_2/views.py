from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

landing_page_content = 'A computer science student at Fasilkom, Universitas Indonesia. Who is eager to learn software development and try to develop an useful application. I am driven to be a software engineer'

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)
