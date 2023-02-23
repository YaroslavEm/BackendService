from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(label='Название статьи')
