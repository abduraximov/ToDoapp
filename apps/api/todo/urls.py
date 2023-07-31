from django.urls import path

from apps.api.todo.views import (list_todo, detail_todo,
                                 not_completed, is_completed,
                                 set_completed, set_not_completed
                                 )

urlpatterns = [
    path('todo/', list_todo, name="todo"),
    path('todo/not-completed/', not_completed, name="not-completed"),
    path('todo/set-completed/<int:pk>/', set_completed, name="set-completed"),
    path('todo/set-not-completed/<int:pk>/', set_not_completed, name="set-not-completed"),
    path('todo/is-completed/', is_completed, name="is-completed"),
    path('todo/<slug:slug>/', detail_todo, name="detail"),

]
