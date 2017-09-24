from django import forms

class Message_Form(forms.Form):
    lab_4_error_messages = {
        'required': 'Tolong isi input ini ya teman :)',
        'invalid': 'Isi input dengan email ya teman :)',
    }
    attrs = {
        'class': 'form-control'
    }

    name = forms.CharField(label='Nama', required=False, max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs))
    message = forms.CharField(widget=forms.Textarea(attrs=attrs), required=True, error_messages=lab_4_error_messages)