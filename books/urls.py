from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('' , views.bookies , name='bookies'),
    path('books_detail/<int:pk>/' , views.books_detail , name='books_detail'),
    path('dataview/' , views.DataView.as_view() , name='DataView'),
]
