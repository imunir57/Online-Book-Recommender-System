from django.db import models


# Create your models here.
class Book_list(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	genre = models.CharField(max_length=500)
	
	def __str__(self):
		return self.name
	

class Recommended_list(models.Model):
	idx = models.ForeignKey(Book_list, on_delete=models.CASCADE)
	rec1 = models.IntegerField()
	rec2 = models.IntegerField()
	rec3 = models.IntegerField()
	rec4 = models.IntegerField()
	rec5 = models.IntegerField()
	
	def __str__(self):
		return self.idx.name
