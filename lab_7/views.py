from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Friend
from .api_csui_helper.csui_helper import CSUIhelper
import os
import json

response = {}
csui_helper = CSUIhelper(os.environ.get("SSO_USERNAME"),
                         os.environ.get("SSO_PASSWORD"))


@csrf_exempt
def index(request):
    # Page halaman menampilkan list mahasiswa yang ada
    if request.method == 'POST':
        csui_helper.instance.set_current_page(int(request.POST.get('buttonUrl')))

    mahasiswa_list = csui_helper.instance.get_mahasiswa_list()
    siakng_mahasiswalist_data = csui_helper.instance.get_siakng_mahasiswalist_data()

    previous_url = siakng_mahasiswalist_data.json()['previous']
    next_url = siakng_mahasiswalist_data.json()['next']

    # page number -1 represent not display back or next button
    previous_page_number = -1
    next_page_number = -1

    if previous_url != None:
        previous_page_number = csui_helper.instance.current_page_number - 1

    if next_url != None:
        next_page_number = csui_helper.instance.current_page_number + 1

    friend_list = Friend.objects.all()
    response = {"mahasiswa_list": mahasiswa_list, "friend_list": friend_list, "author": "Arga Ghulam Ahmad",
                "next_url": next_page_number,
                "previous_url": previous_page_number}
    html = 'lab_7/lab_7.html'
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
