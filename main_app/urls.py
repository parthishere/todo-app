

from django.urls import path, include
from .views import list_function, add_todo, detail_todo

app_name = 'main_app'

urlpatterns = [
    path('', list_function, name='home'),
    path('create/', add_todo, name='create'),
    path('<int:pk>', detail_todo, name='detail')
]
