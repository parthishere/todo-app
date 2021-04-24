from django.urls import path, include
from .views import (
    tag_list,
    add_tag,
    edit_tag, 
    delete_tag
)

app_name = 'tag'

urlpatterns = [
    path('', tag_list, name='list'),
    path('create/', add_tag, name='create'),
    path('<int:pk>/edit', edit_tag, name='edit'),
    path('<int:pk>/delete', delete_tag, name='delete'),

]
