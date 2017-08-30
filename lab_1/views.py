from django.shortcuts import render
import datetime

mhs_name = 'Arga Ghulam Ahmad'
birth_year = 1998

def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_year)}
    return render(request, 'index.html', response)

def calculate_age(birth_year):
    datetime_now = datetime.datetime.now()
    current_year = datetime_now.year
    my_age = abs(birth_year - current_year)
    return my_age
