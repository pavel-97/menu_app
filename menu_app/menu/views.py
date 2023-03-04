from django.shortcuts import render


def index(request):
    return render(request, 'menu/menu.html')


def category(request, category_name):
    return render(request, 'menu/menu.html', context={'category': category_name})
