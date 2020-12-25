from django import forms

from .models import Sotrudnik


class PostSotrudnik(forms.ModelForm):
    class Meta:
        model = Sotrudnik
        fields = ('name_n', 'name_i')


class SearchSotrudnik(forms.Form):
    query = forms.CharField()
