from django.shortcuts import render, get_object_or_404, redirect          # сли не найена страница, то выдаст ошибку 404
from news.forms import CommentForm
# Create your views here.
from news.models import News, Comments


def news_list(request):
    """
    вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def new_single(request, pk):           # pk is id of article
    """
    вызов полной сатьи и комментариев к ней
    """
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk)  # moderation=True)       # все записи, где номер статьи = pk (и комментарии модерированы)
    if request.method == 'POST':
        form = CommentForm(request.POST)        # пользователь уже ввел
        if form.is_valid():
            # зная, кто на сайте и кто отправил форму, надо добавить юзера к модели комментариев
            form = form.save(commit=False)  # Приостановили сохранение формы
            form.user = request.user  # к полю форм.юзер присваиваем имя того, кто совершил запрос
            form.new = new  # присвоим статью, на которой делали комментарий
            form.save()
            return redirect(new_single, pk)  # перенаправляем пользователя на изначальную страницу новости
    else:
        form = CommentForm()
    return render(request, "news/new_single.html",  # передаем в ХТМЛ то, что в кавычках
                  {"new": new,
                   'comments': comment,        # выше первый метод вывода комментариев
                   "form": form})          # потом перейти в УРЛ, который будет запускать эту функцию
