

from django.urls import path, include
from .views import (
    list_function,
    add_todo,
    detail_todo,
    edit_todo,
    delete_list,
    archives_list,
    archive_todo,
    done_todo,
    done_todo_list,
    search_todo,
    starred_todo,
    starred_todo_list
)

app_name = 'main_app'

urlpatterns = [
    path('', list_function, name='home'),
    path('create/', add_todo, name='create'),
    path('done/', done_todo, name='done'),  
    path('search/', search_todo, name='search'),
    path('<int:pk>', detail_todo, name='detail'),
    path('<int:pk>/edit', edit_todo, name='edit'),
    path('<int:pk>/delete', delete_list, name='delete'),
    path('archive', archive_todo, name='archive'),
    path('archives', archives_list, name='archive-list'),
    path('completed', done_todo_list, name='completed-list'),
    
    path('starred', starred_todo_list, name='starred-list'),
    path('star', starred_todo, name='star'),
]
