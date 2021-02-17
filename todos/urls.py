from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    # Each individual todo will eb avail at its primary key, which is a value django sets automatically in every db table. First entry is 1 and so on (api/1/).
    path("<int:pk>", DetailTodo.as_view()),
    # List of todos at the empty string "", or api/
    path("", ListTodo.as_view()),
]