from django.urls import path
#from . import views
from .views import (
    TodoListApiView,
)


urlpatterns = [
#path('', views.todos, name = 'todos'),
path('api', TodoListApiView.as_view()),

]