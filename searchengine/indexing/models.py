# Create your models here.

from django.db import models

class TTexts(models.Model):
    idtext = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    publication_date = models.DateField
    source = models.CharField(max_length=150)
    upload_date = models.DateTimeField(auto_now_add=True)
    centents = models.TextField

    class Meta:
        db_table = 'TTexts'