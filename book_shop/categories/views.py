from email import message
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm


def all_categories(request):
    categories = Category.get_all()
    return render(request, 'categories/allCategories.html', {'categories': categories})


def category_detail(request, category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return render(request, 'categories/category_not_found.html')
    return render(request, 'categories/category_detail.html', {'category': category})


# @login_required
# def category_create(request):
#     category = None
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             category = form.save()
#     return render(request, 'categories/categoryForm.html', {'form': CategoryForm(), 'main_title': 'Create Category', 'category': category})

# @login_required

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return render(request, 'categories/categoryForm.html', {'category': category, 'message': 'Category created successfully'})
    else:
        form = CategoryForm()  # Create a new form instance for GET requests
    return render(request, 'categories/categoryForm.html', {'form': form, 'main_title': 'Create Category'})


def category_update(request, category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return render(request, 'categories/categoryForm.html', {'message': 'Category not found'})

    # Pass instance of category to form
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return render(request, 'categories/categoryForm.html', {'category': category, 'message': 'Category updated successfully'})

    return render(request, 'categories/category_update.html', {'form': form, 'category': category})


@login_required
def category_delete(request, id):
    category = Category.get_by_id(id)
    if not category:
        return render(request, 'categories/all_categories.html', {'message': 'Category not found'})
    category.delete()
    context = {
        'categories': Category.get_all(),
        'message': 'Category deleted successfully'
    }
    return render(request, 'categories/allCategories.html', context)
