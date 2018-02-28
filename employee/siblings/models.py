from django.db import models
from mainapp.models import Employee
# Create your models here.
RELATION_CHOICES = (
	('child','Child'),
	('wife','Wife'),
	('husband','Husband'),

	)

class Sibilings(models.Model):
	employee 		= models.ForeignKey(Employee)
	relation        = models.CharField(max_length=50,
							default ='Child' ,
							choices=RELATION_CHOICES)
	full_name		= models.CharField(max_length=150)
	age 			= models.IntegerField()
	nationality 	= models.CharField(max_length=50)

	def __str__(self):
		return self.full_name
