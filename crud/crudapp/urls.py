from django.urls import path
from . import views

app_name = 'crudapp'

urlpatterns = [
    path('lst/', views.book_list, name='book_list'),
    path('cbooks/', views.create_book, name='create_book'),
    path('form/', views.BookForm, name='BookForm'),
 ]