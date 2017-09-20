from django.shortcuts import render
from lab_2.views import landing_page_content

response = {'author': "Arga Ghulam Ahmad"}
about_me = ["Computer Science Student", "Programmer", "Gamer", "Developer", "Rider", "OmegaCSUI"]
def index(request):
    response['content'] = landing_page_content
    html = 'lab_4/lab_4.html'
    response['about_me'] = about_me
    return render(request, html, response)
