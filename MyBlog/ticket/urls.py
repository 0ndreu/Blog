from . import views
from django.urls import path

urlpatterns =[
    # path('', views.MyView.as_view()),       # Так подключается класс УРЛ
    path('add-ticket', views.AddTicket.as_view()),
    path('list-ticket', views.ListTicket.as_view(), name='list-ticket'),
    path('update-ticket/<int:pk>', views.UpdateTicket.as_view(), name='update-ticket'),

]