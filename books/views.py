from django.shortcuts import render ,redirect
import pandas as pd
import csv
from .forms import DataForm ,RatingForm
from django.views.generic import FormView
from django.contrib.auth.models import User
import time
from .models import Books , Ratings



class DataView(FormView):
    template_name = 'csvbookform.html'
    form_class = DataForm

    def form_valid(self, form):
        form.process_data()
        return super().form_valid(form)


def bookies(request):
    book_list = Books.objects.all()
    return render(request, 'book_list.html' , {
        'book_list' : book_list , 
    })

def books_detail(request , pk):
    books_detail = Books.objects.get(pk=pk)
    cate = books_detail.Category
    print(cate)

    book_list = Books.objects.filter(Category=cate).order_by('?')[:5]

    books_detail.Views = books_detail.Views + 1
    books_detail.save()

    rating_detail = Ratings.objects.filter(books =books_detail ,user=request.user)

    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            if Ratings.objects.filter(books =books_detail ,user=request.user).exists():
                form = RatingForm()
            else:
                book_form = form.save(commit=False)
                book_form.user = request.user
                book_form.books = books_detail
                book_form.save()
                
            return redirect('books:bookies')
    else:
        form = RatingForm()

    return render(request, 'book_detail.html' , {
        'books_detail' : books_detail , 
        'form' : form , 
        'rating_detail' : rating_detail ,
        'book_list' : book_list , 
    })
