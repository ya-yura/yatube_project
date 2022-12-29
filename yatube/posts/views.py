from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_show(request):
    return HttpResponse('Список постов')


def group_detail(request, pk):
    return HttpResponse(f'Чота номер {pk}')
