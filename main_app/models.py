from django.db import models
from django.shortcuts import redirect, reverse
from django.utils import timezone

from django.contrib.auth.models import User
import tags.models

# Create your models here.
class ToDoModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
	done = models.BooleanField(default=False)
	archive = models.BooleanField(default=False)
	tags = models.ManyToManyField('tags.Tag', blank=True)
	starred = models.BooleanField(default=False)

	class Meta():
		ordering = [ '-id' ]
 
	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse("main_app:detail", kwargs={"pk": self.pk})


	

