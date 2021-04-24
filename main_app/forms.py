from django import forms

from tags.models import Tag
from .models import *

class TodoModelForm(forms.ModelForm):
	class Meta:
		model = ToDoModel
		fields = ['text', 'description', 'end_date', 'tags', 'done']
  
	def __init__(self, *args,**kwargs):
		user_set = kwargs.pop('user_set', None)
		super(TodoModelForm, self).__init__(*args,**kwargs)
		self.fields['tags'].queryset = Tag.objects.filter(user=user_set)