from django.db import models

# Create your models here.

class TUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    security_question = models.CharField(max_length=100)
    security_answer = models.CharField(max_length=100)
