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
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.save()
        return render(request, 'categories/categoryForm.html', {'category': category})
    return render(request, 'categories/categoryForm.html', {'form': CategoryForm(), 'main_title': 'Create Category'})


@login_required
def category_update(request, category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return render(request, 'categories/category_not_found.html')
    if request.method == 'POST':
        # get the data from modelform
        name = request.POST.get('name')
        description = request.POST.get('description')
        category.name = name
        category.description = description
        category.save()
        return render(request, 'categories/category_updated.html', {'category': category})
    return render(request, 'categories/category_update.html', {'category': category})


@login_required
def category_delete(request, category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return render(request, 'categories/all_categories.html', {'message': 'Category not found'})
    category.delete()
    context = {
        'categories': Category.get_all(),
        'message': 'Category deleted successfully'
    }
    return render(request, 'categories/all_categories.html', context)
