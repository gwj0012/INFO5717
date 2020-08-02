from django.db import models
from django.shortcuts import HttpResponse

# Create your models here.

class TUser(models.Model):
    iduser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    security_question = models.CharField(max_length=100)
    security_answer = models.CharField(max_length=100)

    class Meta:
        db_table = 'TUser'

class HttpJavascriptResponse(HttpResponse):
    def __init__(self, content):
       HttpResponse.__init__(self, content, mimetype="text/javascript")