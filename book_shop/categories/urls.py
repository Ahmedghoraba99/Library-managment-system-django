from django.urls import path
from categories.views import category_create, category_delete, category_detail, all_categories, category_update

urlpatterns = [
    path('create/', category_create, name='category_create'),
    path('<int:pk>/edit/', category_update,
         name='category_update'),
    path('<int:pk>/delete/', category_delete, name='category_delete'),
    path('<int:pk>/', category_detail, name='category_detail'),
    path('', all_categories, name='all_categories'),
]
