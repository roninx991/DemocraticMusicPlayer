from django.db import models

# Create your models here.

class Song(models.Model):
	Name 	= models.CharField(max_length=200)
	Singer	= models.CharField(max_length=120,null=True,blank=True)
	Genre 	= models.CharField(max_length=120,null=True,blank=True)
	
	def __str__(self):
		return self.Name
