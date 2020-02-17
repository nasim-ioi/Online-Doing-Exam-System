from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.TextField()
    options = models.TextField()
    correct_option = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    

class Examiner(models.Model):
    name = models.CharField(max_length=50)
    examiner_questions = models.TextField()#list -> str from questions' id
    ans = models.TextField(null = True)

    def __str__(self):
        return self.name
    