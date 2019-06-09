from . import views
from django.urls import path

urlpatterns =[
    path('', views.MyView.as_view()),       # Так подключается класс УРЛ
    path('add_ticket', views.MyTemplateView.as_view()),
]