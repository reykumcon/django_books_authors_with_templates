from django.urls import path
from . import views

urlpatterns = [
    path('books', views.index_book),
    path('authors', views.index_author),
    path('books/add_book', views.add_book),
    path('authors/add_author', views.add_author),
    path('books/<int:id>', views.display_book),
    path('authors/<int:id>', views.display_author),
    path('books/<int:id>/assign_author', views.assign_author),
    path('authors/<int:id>/assign_book', views.assign_author),
]