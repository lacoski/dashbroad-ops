from django import forms

class DeleteForm(forms.Form):
    key = forms.CharField()

class StateServerForm(forms.Form):
    key = forms.CharField()

class CreateServerForm(forms.Form):
    name = forms.CharField()
    flavor_id = forms.CharField()
    image_id = forms.CharField()
    network_id = forms.CharField()

class StateFlavorForm(forms.Form):
    key = forms.CharField()

class CreateFlavorForm(forms.Form):
    name = forms.CharField()
    vcpus = forms.CharField()
    ram = forms.CharField()
    disk = forms.CharField()

class CreateImageForm(forms.Form):
    name = forms.CharField()
    disk_format = forms.CharField()

class StateImageForm(forms.Form):
    key = forms.CharField()   

