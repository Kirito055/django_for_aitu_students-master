from django.db import models

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=100)
    user_surname=models.CharField(max_length=100)
    # birthday_date=models.DateField(input_formats=['%d-%m-%Y'])
    phone_number=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    # img=models.FileField()




class Editor(models.Model):
    editor_name = models.CharField(max_length = 100)
    editor_surname = models.CharField(max_length = 100)

class Article(models.Model):
    article_text = models.TextField('article_text')
    article_date = models.DateTimeField('date published', auto_now_add=True)
    article_editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
