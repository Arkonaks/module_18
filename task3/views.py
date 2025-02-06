from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView

def platform(request):
    title = 'Главная страница'
    text1 = 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3
    }

    return render(request, 'platform.html', context)

def games(request):
    title = 'Магазин игр'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunc 2077'
    game3 = 'Pay Day 2'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')
