from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
import tags.models

# Create your models here.
class ToDoModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=120)
	start_date = models.DateTimeField(default=timezone.now)
	end_date = models.DateTimeField(default=timezone.now)
	done = models.BooleanField(default=False)
	archive = models.BooleanField(default=False)
	tags = models.ManyToManyField('tags.Tag', blank=True, null=True)

	class Meta():
		ordering = [ '-id' ]
 
	def __str__(self):
		return self.text

