from django.shortcuts import render, redirect
from .models import Diary
from datetime import datetime
import pytz
import json

diary_dict = {}
response ={}
def index(request):
    diary_dict = Diary.objects.all().values()
    if 'user_login' in request.session:
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['diary_dict'] = convert_queryset_into_json(diary_dict)
        response['button_logout_session'] = True
        return render(request, 'to_do_list.html', response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)

def add_activity(request):
    try:
        if request.method == 'POST':
            date = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M')
            Diary.objects.create(date=date.replace(tzinfo=pytz.UTC), activity=request.POST['activity'])
            return redirect('/lab-3/')
    except ValueError:
        pass
    finally:
        return redirect('/lab-3/')

def convert_queryset_into_json(queryset):
    ret_val = []
    for data in queryset:
        ret_val.append(data)
    return ret_val
