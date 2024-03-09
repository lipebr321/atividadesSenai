from django.db import models

# Create your models here.


class pessoas (models.Model):
    id = models.AutoField(primary_key=True)
    nome= models.TextField()
    email= models.TextField()
    telefone=models.IntegerField()
    mensagem=models.TextField()

    