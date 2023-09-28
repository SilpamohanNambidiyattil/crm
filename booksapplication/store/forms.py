from django import forms
from store.models import Books

class BooksCreateForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    publisher=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))


class BooksUpdateForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["name","author","publisher","price"]
        