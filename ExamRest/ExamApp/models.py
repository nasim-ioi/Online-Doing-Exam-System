from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    question = models.TextField()
    options = models.TextField()
    correct_option = models.CharField(max_length=50)

    def __str__(self):
        return self.question
