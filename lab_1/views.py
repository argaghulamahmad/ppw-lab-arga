from django.shortcuts import render
<<<<<<< HEAD
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
=======
from datetime import datetime, date
# Enter your name here
mhs_name = '' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date() #TODO Implement this, format (Year, Month, Date)
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
>>>>>>> b80a2738b5018e63cdf9fdc4a7f28364875518a0
