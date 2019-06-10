from django.db import models
from django.contrib.auth.models import User


class CategoryTicket(models.Model):
    """
    Категории тикетов
    """
    title = models.CharField('категория', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Ticket(models.Model):
    """
    класс тикетов
    """
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryTicket,
                                 verbose_name='категория',
                                 on_delete=models.CASCADE)
    title = models.CharField('Тема', max_length=100)
    text = models.TextField('Текст письма', max_length=1000)

    class Meta:
        verbose_name_plural = 'Тикеты'
        verbose_name = 'Тикет'


    def __str__(self):
        return "{} {}".format(self.title, self.user)
