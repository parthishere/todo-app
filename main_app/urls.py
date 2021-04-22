

from django.urls import path, include
from .views import list_function, add_todo, detail_todo, edit_todo, archives_list, archive_todo

app_name = 'main_app'

urlpatterns = [
    path('', list_function, name='home'),
    path('create/', add_todo, name='create'),
    path('<int:pk>', detail_todo, name='detail'),
    path('<int:pk>/edit', edit_todo, name='edit'),
    path('<int:pk>/delete', edit_todo, name='delete'),
    path('<int:pk>/archive', archive_todo, name='archive'),
    path('archives', archives_list, name='archive-list'),
]
