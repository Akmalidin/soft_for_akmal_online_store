from django import forms

class ImportProductsForm(forms.Form):
    file = forms.FileField()