from django.db import models
from django.db.models.signals import pre_save

POSITION_CHOICES = (
	('X','Employee'),
	('Y','Manager'),
	('Z','CEO'),
	)

GENDAR_COICES = (
	('male' ,'Male'),
	('female' ,'Female'),)

#maritial_status
MARIRTIAL_STATUS_CHOICES=(
	('single' ,'Single'),
	('married' ,'Married'),
	)

class Employee(models.Model):
	first_name		= models.CharField(max_length=50)
	last_name		= models.CharField(max_length=50)
	middle_name		= models.CharField(max_length=50)
	slug 	   		= models.SlugField(blank=True ,
									unique=True)
	nationa_id		= models.CharField(max_length=15 ,
									unique=True)
	position 		= models.CharField(max_length=120 ,
									default='Employee',
							  		choices=POSITION_CHOICES)
	age 			= models.IntegerField()
	date_of_birth	= models.DateField()
	timestamp   	= models.DateTimeField(auto_now_add=True)
	placr_of_birth  = models.CharField(max_length=120)
	country 		= models.CharField(max_length=50)
	nationality 	= models.CharField(max_length=50)
	maritial_status = models.CharField(max_length=50 ,
									default ='Male' ,
									choices=MARIRTIAL_STATUS_CHOICES)
	gendar 			=  models.CharField(max_length=50 ,
									default ='Male' ,
									choices=GENDAR_COICES)

	def __str__(self):
		return self.first_name
	def full_name(self):
		self.FullName = self.first_name + ' ' + self.middle_name+ ' '+self.last_name
		return self.FullName




def employee_pre_save_resever(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(employee_pre_save_resever, sender=Employee)
