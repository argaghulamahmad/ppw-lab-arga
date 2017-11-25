from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

landing_page_content = 'A computer science student at Fasilkom, Universitas Indonesia. Who is eager to learn software development and try to develop an useful application. I am driven to be a software engineer'

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    if 'user_login' in request.session:
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_session'] = True
        return render(request, 'index_lab2.html', response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)