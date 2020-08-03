# from django.db import models
#
# # Create your models here.
#
# class TText(models.Model):
#     iduser = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=45)
#     password = models.CharField(max_length=45)
#     security_question = models.CharField(max_length=100)
#     security_answer = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = 'TText'

# from django.db import models
#
# class TText(models.Model):
#     idtext = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=45)
#     author = models.CharField(max_length=45)
#     publication_date = models.DateField
#     source = models.CharField(max_length=150)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     centents = models.TextField
#
#     class Meta:
#         db_table = 'TText'