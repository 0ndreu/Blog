from django.shortcuts import render, get_object_or_404           # сли не найена страница, то выдаст ошибку 404

# Create your views here.
from news.models import News


def news_list(request):
    """
    вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def new_single(request, pk):           # pk is id of article
    """
    вызов полной сатьи
    """
    new = get_object_or_404(News, id=pk)
    return render(request, "news/new_single.html", {"new": new})           # потом перейти в УРЛ, который будет запускать эту функцию

