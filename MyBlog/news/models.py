from django.db import models
from django.contrib.auth import get_user_model  # захват логина/пароля пользователя

User = get_user_model()


class Category(models.Model):
    """
    таблица категорий
    """
    title = models.CharField('Название', max_length=50)

    class Meta:                                 # будет в админ панели
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title  # Возвращает НАЗВАНИЕ статьи


class Tag(models.Model):
    """
    Теги статей
    """
    title = models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title  # Возвращает название статьи


class News (models.Model):
    """
    Таблица новостей
    """
    user = models.ForeignKey(User,          # у одного автора много постов
                             verbose_name='Автор',
                             on_delete=models.CASCADE)      # при удалении юзера все его новости удаляются
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    category = models.ForeignKey(Category,          # в одной категории много новостей
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,  # при удалении категории поле будет пустым,
                                 null=True)                  # статья удаляться не будет
    text_min = models.TextField(verbose_name="мин. текст", max_length=350)
    text = models.TextField("Текст статьи")
    tags = models.ManyToManyField(Tag, verbose_name="Теги", )  # у одной статьи несколько тегов
    created = models.DateTimeField("Дата создания", auto_now_add=True)  # Автоматическое присванивание даты
    description = models.CharField("Описание", max_length=100)
    keywords = models.CharField("Ключевые слова", max_length=50)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Стаьи'

    def __str__(self):
        return self.title  # Возвращает название статьи


class Comments(models.Model):
    """
    таблица комментариев к новостям
    """
    text = models.TextField('Комментарий')
    new = models.ForeignKey(News,           # для использования внешнего ключа, класс News уже должен быть объявлен
                            verbose_name='новость',
                            on_delete=models.CASCADE)  # при удалении поста удаляются все комметарии
    user = models.ForeignKey(User,          # у одного автора много комментариев
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return "{}".format(self.user)       # вывод пользователя
