from django.urls import path
from todo import views


urlpatterns = [
    path('', views.TodoDetailView.as_view(), name='todo_detail_view'),
]
