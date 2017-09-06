from django.shortcuts import render
    from lab_1.views import mhs_name, birth_date
    [{'subject' : 'Name', 'value' : 'Arga Ghulam Ahmad'},{{'subject' : 'Birth Date', 'value' : '9 December 1998'},{{'subject' : 'Sex', 'value' : 'Male'}

    bio_dict = [{'subject' : 'Name', 'value' : mhs_name},\
    {'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')},\
    {'subject' : 'Sex', 'value' : ''}]

    def index(request):
        response = {}
        return render(request, 'description_lab2addon.html', response)
