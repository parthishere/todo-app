from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    
    class Meta():
        ordering = ['-id']
        
    def __str__(self):
        return self.tag