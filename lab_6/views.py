from django.shortcuts import render

response = {}
def index(request):
    if 'user_login' in request.session:
        html = 'lab_6/lab_6.html'
        response['user_name'] = request.session['user_login']
        response['user_npm'] = request.session['kode_identitas']
        response['author'] = "Arga Ghulam Ahmad"
        response['button_logout_session'] = True
        return render(request, html, response)
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)
    