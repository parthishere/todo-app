from django import forms
from .widgets import TimePickerInput


from tags.models import Tag
from .models import *

class TodoModelForm(forms.ModelForm):
	end_date =forms.DateField(widget = forms.SelectDateWidget())
	end_time = forms.TimeField(widget=TimePickerInput)
	class Meta:
		model = ToDoModel
		fields = ['text', 'description', 'end_date', 'end_time', 'tags']

	def __init__(self, *args,**kwargs):
		user_set = kwargs.pop('user_set', None)
		super(TodoModelForm, self).__init__(*args,**kwargs)
		self.fields['tags'].queryset = Tag.objects.filter(user=user_set)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'