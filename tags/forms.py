from django import forms

from .models import *

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['tag']
  
	def __init__(self, *args, **kwargs):
		super(TagForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'