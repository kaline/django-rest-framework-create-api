from django.urls import path
#from . import views
from .views import (
    TodoListApiView,
    TodoDetailApiView
)


urlpatterns = [
#path('', views.todos, name = 'todos'),
path('api', TodoListApiView.as_view()),
path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]