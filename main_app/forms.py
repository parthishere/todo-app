from django import forms

from .models import *

class TodoModelForm(forms.ModelForm):
	class Meta:
		model = ToDoModel
		fields = ['text', 'description', 'end_date', 'tags', 'done']