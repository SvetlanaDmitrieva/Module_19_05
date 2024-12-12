from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserRegister
from django.db import models
from .models import *
# Create your views here.
from django.views.generic import TemplateView


def main_page(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


def game_store_page(request):
    title = 'Игры'
    games = Game.objects.values()
    pay = 'Купить'
    context = {
        'title': title,
        'games': games,
        'pay': pay,
    }
    return render(request, 'game_store.html', context)


def cart_page(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)


def news_page(request):
    news = Post.objects.filter(is_published= True).order_by('-created_at')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})


def sign_up_by_html(request):
    users = Buyer.objects.values_list('name', flat=True)
    info = {}
    if request.method == 'POST':
        user_exists = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if is_user:
            info['error'] = 'Пользователь уже существует'
            print(info['error'])
            return HttpResponse(info['error'])
        passwords_matched = password == repeat_password
        if passwords_matched:
            if age >= 18:
                user_exists = True
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error'] = 'Пароли не совпадают'

        if user_exists:
            new_user = Buyer.objects.create(name=username, balance=10000, age=age)
            message = f'Приветствуем, {new_user.name}!'
        else:
            message = info['error']
        print(message)
        return HttpResponse(message)
    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = Buyer.objects.values_list('name', flat=True)
    info = {}
    message = ''
    if request.method == 'POST':
        user_exists = False
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            is_user = username in users
            if is_user:
                info['error'] = 'Пользователь уже существует'
                print(info['error'])
                return HttpResponse(info['error'])
            passwords_matched = password == repeat_password
            if passwords_matched:
                if age >= 18:
                    user_exists = True
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пароли не совпадают'

            if user_exists:
                new_user = Buyer.objects.create(name=username, balance=10000, age=age)
                message = f'Приветствуем, {new_user.name}!'
            else:
                message = info['error']
            print(message)
        return HttpResponse(message)
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)
