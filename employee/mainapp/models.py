from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from employee.utils import unique_slug_generator
import random
import os


POSITION_CHOICES = (
	('employee','Employee'),
	('manager','Manager'),
	('ceo','CEO'),
	)

GENDAR_COICES = (
	('male' ,'Male'),
	('female' ,'Female'),)

#maritial_status
MARIRTIAL_STATUS_CHOICES=(
	('single' ,'Single'),
	('married' ,'Married'),
	)

def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext= os.path.splitext(base_name)
    return(name,ext)
def upload_image_path(instance,filename):
	
	new_filenumber= random.randint(1,567894328)
	name,ext= get_filename_ext(filename)
	qs = Employee.objects.filter(first_name=instance)
	new_final_name_un = False
	for i in qs: 
		new_final_name_un=(i.first_name)
	if new_final_name_un :
		new_final_name = str(new_final_name_un)+str(new_filenumber)
	else:
		new_final_name =  instance.first_name+str(new_filenumber)
	return f"{new_final_name}{ext}" 

class Employee(models.Model):
	first_name		= models.CharField(max_length=50)
	last_name		= models.CharField(max_length=50)
	middle_name		= models.CharField(max_length=50)
	slug 	   		= models.SlugField(blank=True ,
						unique=True)
	image 			= models.ImageField(
						upload_to = upload_image_path ,
				        blank= True)
	national_id		= models.CharField(max_length=15 ,
						unique=True)
	position 		= models.CharField(max_length=120 ,
						default='Employee',
				  		choices=POSITION_CHOICES)
	jop 			= models.CharField(max_length=150,
						 blank= True )
	age 			= models.IntegerField()
	date_of_birth	= models.DateField()
	timestamp   	= models.DateTimeField(
						auto_now_add=True)
	place_of_birth  = models.CharField(max_length=120)
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
		
	def get_absolute_url(self):
		slug = self.slug
		return reverse('detail',kwargs={'slug':slug})



def employee_pre_save_resever(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(employee_pre_save_resever, sender=Employee)
