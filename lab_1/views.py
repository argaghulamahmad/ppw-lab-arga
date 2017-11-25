from django.shortcuts import render
from datetime import datetime, date

mhs_name = 'Arga Ghulam Ahmad' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1998, 12, 9) #TODO Implement this, format (Year, Month, Date)

def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    if 'user_login' in request.session:
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_session'] = True
        return render(request, 'index_lab1.html', response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
