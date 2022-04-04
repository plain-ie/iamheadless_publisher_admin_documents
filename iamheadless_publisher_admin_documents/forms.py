from django import forms
from django.forms import formset_factory


class DocumentContentForm(forms.Form):
    language = forms.CharField(initial='', max_length=255, widget=forms.widgets.HiddenInput())
    title = forms.CharField(initial='', max_length=255)
    summary = forms.CharField(widget=forms.widgets.Textarea(attrs={'readability': 'true'}))
    file_name = forms.CharField(initial='', max_length=4096, widget=forms.widgets.HiddenInput())
    file = forms.FileField(required=False)


DocumentContentFormSet = formset_factory(DocumentContentForm, extra=0)


class DocumentForm(forms.Form):
    pass
