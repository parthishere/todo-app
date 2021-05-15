import django_filters

from .models import ToDoModel

class ToDoFilter(django_filters.FilterSet):
    class Meta:
        model = ToDoModel
        fields = ['text', 'description']