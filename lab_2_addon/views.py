from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

bio_dict = [{'subject' : 'Name', 'value' : mhs_name}, {'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')}, {'subject' : 'Sex', 'value' : 'Male'}]

def index(request):
    response = {'bio_dict': bio_dict}
    if 'user_login' in request.session:
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_session'] = True
        return render(request, 'description_lab2addon.html', response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)
