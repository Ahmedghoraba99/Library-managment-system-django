from django.urls import path
from .views import books_list, book_detail, book_edit, book_delete, book_create

urlpatterns = [
    path('', books_list, name='books_list'),
    path('<int:book_id>/', book_detail, name='show'),
    path('<int:book_id>/edit/', book_edit, name='edit'),
    path('<int:book_id>/delete/', book_delete, name='delete'),
    path('add/', book_create, name='add'),  # type: ignore
]
