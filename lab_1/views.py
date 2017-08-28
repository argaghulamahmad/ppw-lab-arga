from django.shortcuts import render
import datetime

# Enter your name here
mhs_name = 'Arga Ghulam Ahmad'
birth_year = 1998


# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_year)}
    return render(request, 'index.html', response)


# TODO Implement this to complete last checklist
def calculate_age(birth_year):
    datetime_now = datetime.datetime.now()
    current_year = datetime_now.year
    my_age = birth_year - current_year
    return my_age
