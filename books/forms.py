import io
from django import forms
from .models import Books , Ratings
import csv

class DataForm(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        for books in reader :
            Books.objects.create(Title = books['title'], ISBN=books['ISBN'], Author=books['author'], Yop=books['yop'], Publisher=books['publisher'])

class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ('rate',)