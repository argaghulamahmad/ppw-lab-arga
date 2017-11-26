import datetime
import json

import environ
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Friend

response = {}

from lab_9.csui_helper import *


now = datetime.datetime.now()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

@csrf_exempt
def index(request):
    response = {}
    if 'user_login' in request.session:
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_session'] = True

        access_token = request.session['access_token']
        mahasiswa_list = get_mahasiswa_list(access_token)
        friend_list = Friend.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(mahasiswa_list, 10)
        mahasiswa_list = paginator.page(page)
        response['mahasiswa_list'] = mahasiswa_list
        response['friend_list'] = friend_list
        html = 'lab_7/lab_7.html'
        return render(request, html, response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)

def friend_description(request, index):
    username = env("SSO_USERNAME")
    password = env("SSO_PASSWORD")

    index_number = int(index)
    siakng_mahasiswalist_data = get_mahasiswa_list(get_access_token(username, password))
    npm_mahasiswa = siakng_mahasiswalist_data[index_number]['npm']
    nama_mahasiswa = siakng_mahasiswalist_data[index_number]['nama']
    alamat_mahasiswa = siakng_mahasiswalist_data[index_number]['alamat_mhs']
    response = {
        "npm": npm_mahasiswa, "nama": nama_mahasiswa, "alamat": alamat_mahasiswa, "author": "Arga Ghulam Ahmad"
    }
    html = 'lab_7/deskripsi_teman.html'
    return render(request, html, response)


def friend_list(request):
    friend_list = Friend.objects.all()
    response['friend_list'] = friend_list
    response['author'] = "Arga Ghulam Ahmad"
    html = 'lab_7/daftar_teman.html'
    return render(request, html, response)


def get_friend_list_objects_json(request):
    friends_json = serializers.serialize("json", Friend.objects.all())
    data = {
        'friends_json': friends_json,
        'status': 'success'
    }
    return JsonResponse(data)


@csrf_exempt
def add_friend(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        npm = request.POST.get('npm', None)
        friend_list = Friend.objects.all()
        is_taken = False
        for friend in friend_list:
            if friend.npm == npm:
                is_taken = True
        if not is_taken:
            friend = Friend(friend_name=name, npm=npm)
            friend.save()
            data = model_to_dict(friend)
            return HttpResponse(data)
        if is_taken:
            data = {}
            return HttpResponse(data)


@csrf_exempt
def delete_friend(request):
    if request.method == 'POST':
        friend_id = request.POST.get('friend_id', None)
        Friend.objects.filter(id=friend_id).delete()
        data = {
            'success': True,
            'friend_id': friend_id,
        }

        return JsonResponse(data)


@csrf_exempt
def validate_npm(request):
    npm = request.POST.get('npm', None)
    list_friends = Friend.objects.all()

    # lakukan pengecekan apakah Friend dgn npm tsb sudah ada
    taken = False
    for friend in list_friends:
        if friend.npm == npm:
            taken = True

    data = {
        'is_taken': taken
    }
    return JsonResponse(data)


def model_to_dict(obj):
    data = serializers.serialize('json', [obj, ])
    struct = json.loads(data)
    data = json.dumps(struct[0]["fields"])
    return data
