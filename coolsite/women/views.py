from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям:</h1><p>{catid}</p>")


def pageNotFound(requst, exception):
    return HttpResponseNotFound('<h1>404</h1><p>Друг, страница не найдена, шел бы отсюда.</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам:</h1><p>{year}</p>")