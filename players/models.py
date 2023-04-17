from django.db import models

# Create your models here.
class Player(models.Model):
#    id = models.AutoField(primary_key="True")
   name = models.CharField(max_length=225,null= False,primary_key="True")
   address = models.CharField(max_length=225,null= False)