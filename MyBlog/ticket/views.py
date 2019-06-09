from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Классы Джанго')


class MyTemplateView(TemplateView):     # позволяет возвращать данные сразу в шаблон

    template_name = 'ticket/add-ticket.html'
    """
    В общем случае, метод get_context_data объединяет(сливает вместе) данные контекста всех родительских классов с данными текущего класса. Чтобы сохранить такое поведение в пользовательских классах, в которых вы собираетесь изменять контекст, вы должны в начале вызвать метод get_context_data родительского класса. Если нет двух классов, которые пытаются определить одинаковый ключ, - вы получите желаемый результат. Однако, если есть некий класс, который пытается переопределить ключ, установленный родительскими классами(после вызова super), то любой потомок этого класса также должен явно установить такой ключ(после вызова super), если необходимо гарантировать полное переопределение данных родителей. Если у вас возникли проблемы, просмотрите mro(method resolution order) вашего представления.
    """

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        context['text'] = 'Hello world!'        # в контекст как в словарь ключ со значением (text используем для вызова в add-tickets.html)
        return context
