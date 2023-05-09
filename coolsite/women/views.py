from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts':posts,'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям:</h1><p>{catid}</p>")


def pageNotFound(requst, exception):
    return HttpResponseNotFound('<h1>404</h1><p>Друг, страница не найдена, шел бы отсюда.</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам:</h1><p>{year}</p>")