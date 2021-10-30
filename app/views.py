from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.now()
    msg = f'The time is {now}'
    return HttpResponse(f"{msg}<br><a href={reverse('home')}>На главную</a>")


def workdir_view(request):
    workdir = os.listdir(path='.')
    msg = f'working directory contains: {workdir}'
    return HttpResponse(f"{msg}<br><a href={reverse('home')}>На главную</a>")
    raise NotImplemented
