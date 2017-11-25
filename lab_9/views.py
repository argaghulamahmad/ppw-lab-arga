# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# catatan: tidak bisa menampilkan messages jika bukan menggunakan method 'render'
from .api_enterkomputer import get_drones, get_opticals, get_soundcards

response = {}

# NOTE : untuk membantu dalam memahami tujuan dari suatu fungsi (def)
# Silahkan jelaskan menggunakan bahasa kalian masing-masing, di bagian atas
# sebelum fungsi tersebut.

# ======================================================================== #
# User Func
# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian

"""
    Fungsi yang akan dipanggil saat mengakses app lab-9
"""


def index(request):
    print("#==> masuk index")
    response['author'] = 'Arga Ghulam Ahmad'
    # Mengecek cookie, untuk mengetahui apakah sudah login?
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        html = 'lab_9/session/login.html'

        response['button_logout_session'] = False
        response['button_logout_cookie'] = False

        return render(request, html, response)


"""
    Fungsi untuk mengeset data untuk session
"""


def set_data_for_session(res, request):
    response['author'] = request.session['user_login']
    response['access_token'] = request.session['access_token']
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']
    response['drones'] = get_drones().json()
    response['opticals'] = get_opticals().json()
    response['soundcards'] = get_soundcards().json()

    # print("#drones = ", get_drones().json(), " - response = ", response['drones'])
    # print("#opticals = ", get_opticals().json(), " - response = ", response['opticals'])
    # print("#soundcards = ", get_soundcards().json(), " - response = ", response['soundcards'])

    ## handling agar tidak error saat pertama kali login (session kosong)
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date

    if 'drones' in request.session.keys():
        response['fav_drones'] = request.session['drones']
    else:
        response['fav_drones'] = []

    if 'opticals' in request.session.keys():
        response['fav_opticals'] = request.session['opticals']
    else:
        response['fav_opticals'] = []

    if 'soundcards' in request.session.keys():
        response['fav_soundcards'] = request.session['soundcards']
    else:
        response['fav_soundcards'] = []


"""
    Fungsi yang akan dipanggil saat halaman profil diakses
"""


def profile(request):
    print("#==> profile")
    ## sol : bagaimana cara mencegah error, jika url profile langsung diakses
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('lab-9:index'))
    ## end of sol

    set_data_for_session(response, request)

    response['button_logout_session'] = True
    response['button_logout_cookie'] = False
    response['author'] = "Arga Ghulam Ahmad"

    html = 'lab_9/session/profile.html'
    return render(request, html, response)


# ======================================================================== #

### Drones
def add_session_drones(request, id):
    ssn_key = request.session.keys()
    if not 'drones' in ssn_key:
        print("# init drones ")
        request.session['drones'] = [id]
    else:
        drones = request.session['drones']
        print("# existing drones => ", drones)
        if id not in drones:
            print('# add new item, then save to session')
            drones.append(id)
            request.session['drones'] = drones

    messages.success(request, "Berhasil tambah drone favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))


def del_session_drones(request, id):
    print("# DEL drones")
    drones = request.session['drones']
    print("before = ", drones)
    drones.remove(id)  # untuk remove id tertentu dari list
    request.session['drones'] = drones
    print("after = ", drones)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))


def clear_session_drones(request):
    print("# CLEAR session drones")
    print("before 1 = ", request.session['drones'])
    del request.session['drones']

    messages.error(request, "Berhasil reset favorite drones")
    return HttpResponseRedirect(reverse('lab-9:profile'))


### Opticals
def add_session_opticals(request, id):
    ssn_key = request.session.keys()
    if not 'opticals' in ssn_key:
        print("# init opticals ")
        request.session['opticals'] = [id]
    else:
        opticals = request.session['opticals']
        print("# existing opticals => ", opticals)
        if id not in opticals:
            print('# add new item, then save to session')
            opticals.append(id)
            request.session['opticals'] = opticals

    messages.success(request, "Berhasil tambah optical favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))


def del_session_opticals(request, id):
    print("# DEL opticals")
    opticals = request.session['opticals']
    print("before = ", opticals)
    opticals.remove(id)  # untuk remove id tertentu dari list
    request.session['opticals'] = opticals
    print("after = ", opticals)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))


def clear_session_opticals(request):
    print("# CLEAR session opticals")
    print("before 1 = ", request.session['opticals'])
    del request.session['opticals']

    messages.error(request, "Berhasil reset favorite opticals")
    return HttpResponseRedirect(reverse('lab-9:profile'))


### Soundcards
def add_session_soundcards(request, id):
    ssn_key = request.session.keys()
    if not 'soundcards' in ssn_key:
        print("# init soundcards ")
        request.session['soundcards'] = [id]
    else:
        soundcards = request.session['soundcards']
        print("# existing soundcards => ", soundcards)
        if id not in soundcards:
            print('# add new item, then save to session')
            soundcards.append(id)
            request.session['soundcards'] = soundcards

    messages.success(request, "Berhasil tambah soundcard favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))


def del_session_soundcards(request, id):
    print("# DEL soundcards")
    soundcards = request.session['soundcards']
    print("before = ", soundcards)
    soundcards.remove(id)  # untuk remove id tertentu dari list
    request.session['soundcards'] = soundcards
    print("after = ", soundcards)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))


def clear_session_soundcards(request):
    print("# CLEAR session soundcards")
    print("before 1 = ", request.session['soundcards'])
    del request.session['soundcards']

    messages.error(request, "Berhasil reset favorite soundcards")
    return HttpResponseRedirect(reverse('lab-9:profile'))


# ======================================================================== #
# COOKIES

"""
    Saat pertama kali membuka url yang menuju cookie_login page
    Bila sudah login akan ditampilkan halaman sudah login
    Bila belum login akan ditampilkan halaman cookie_login page
"""


def cookie_login(request):
    print("#==> masuk login")
    if is_login(request):
        return HttpResponseRedirect(reverse('lab-9:cookie_profile'))
    else:
        html = 'lab_9/cookie/login.html'

        response['button_logout_session'] = False
        response['button_logout_cookie'] = False
        response['author'] = "Arga Ghulam Ahmad"

        return render(request, html, response)


"""
    Fungsi yang memeriksa apakah username dan password pada request sudah benar?
    Bila benar, maka set cookie
    Bila salah, maka redirect ke cookie_login page
"""


def cookie_auth_login(request):
    print("# Auth login")
    if request.method == "POST":
        user_login = request.POST['username']
        user_password = request.POST['password']

        if my_cookie_auth(user_login, user_password):
            print("#SET cookies")
            res = HttpResponseRedirect(reverse('lab-9:cookie_login'))

            res.set_cookie('user_login', user_login)
            res.set_cookie('user_password', user_password)

            return res
        else:
            msg = "Username atau Password Salah"
            messages.error(request, msg)
            return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))


"""
    Halaman profile untuk cookie
"""


def cookie_profile(request):
    print("# cookie profile ")
    # method ini untuk mencegah error ketika akses URL secara langsung
    if not is_login(request):
        print("belum login")
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_cookie'] = True
        response['button_logout_session'] = False

        print("cookies => ", request.COOKIES)
        in_uname = request.COOKIES['user_login']
        in_pwd = request.COOKIES['user_password']

        # jika cookie diset secara manual (usaha hacking), distop dengan cara berikut
        # agar bisa masuk kembali, maka hapus secara manual cookies yang sudah diset
        if my_cookie_auth(in_uname, in_pwd):
            html = "lab_9/cookie/profile.html"
            res = render(request, html, response)
            return res
        else:
            print("#login dulu")
            msg = "Kamu tidak punya akses :P "
            messages.error(request, msg)
            html = "lab_9/cookie/login.html"
            return render(request, html, response)


"""
    Menghapus cookie agar bisa 'logout' dari program
"""


def cookie_clear(request):
    res = HttpResponseRedirect('/lab-9/cookie/login')
    res.delete_cookie('lang')
    res.delete_cookie('user_login')
    res.delete_cookie('user_password')

    msg = "Anda berhasil logout. Cookies direset"
    messages.info(request, msg)
    return res


"""
    Fungsi yang memeriksa username dan password pada halama cookie_login
"""


def my_cookie_auth(in_uname, in_pwd):
    my_uname = "user"  # SILAHKAN ganti dengan USERNAME yang kalian inginkan
    my_pwd = "pass"  # SILAHKAN ganti dengan PASSWORD yang kalian inginkan
    return in_uname == my_uname and in_pwd == my_pwd


"""
    Mengecek apakah user sudah login dengan memeriksa cookie yang ada pada browser client
"""


def is_login(request):
    return 'user_login' in request.COOKIES and 'user_password' in request.COOKIES


### General Function
# def add_session_item(request, key, id):
#     print("#ADD session item")
#     ssn_key = request.session.keys()
#     if not key in ssn_key:
#         request.session[key] = [id]
#     else:
#         items = request.session[key]
#         if id not in items:
#             items.append(id)
#             request.session[key] = items
#
#     msg = "Berhasil tambah " + key + " favorite"
#     messages.success(request, msg)
#     return HttpResponseRedirect(reverse('lab-9:profile'))
#
#
# def del_session_item(request, key, id):
#     print("# DEL session item")
#     items = request.session[key]
#     print("before = ", items)
#     items.remove(id)
#     request.session[key] = items
#     print("after = ", items)
#
#     msg = "Berhasil hapus item " + key + " dari favorite"
#     messages.error(request, msg)
#     return HttpResponseRedirect(reverse('lab-9:profile'))
#
#
# def clear_session_item(request, key):
#     del request.session[key]
#     msg = "Berhasil hapus session : favorite " + key
#     messages.error(request, msg)
#     return HttpResponseRedirect(reverse('lab-9:index'))
# ======================================================================== #
