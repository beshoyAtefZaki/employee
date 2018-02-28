from django.db import models
from django.urls import reverse
from django.db.models.signals import m2m_changed
from mainapp.models import Employee



class Deduction(models.Model):
	deductions 	= models.DecimalField(
					max_digits=15, decimal_places=2 ,
					blank=True ,default=0)
	timestamp 	= models.DateTimeField(
					auto_now_add=True ,blank=True)
	def __str__(self):
		return str(self.deductions)

class Earnings(models.Model):
	earnings 	= models.DecimalField(
					max_digits=15, decimal_places=2 ,
					blank=True ,default=0)
	timestamp 	= models.DateTimeField(
					auto_now_add=True ,blank=True)
	def __str__(self):
		return str(self.earnings)

class Salary(models.Model):
	employee 		= models.OneToOneField(Employee)
	main_salary 	= models.DecimalField(
						max_digits =15,
						decimal_places=2)
	total_earnings  = models.DecimalField(
						default=0,
						max_digits=15,
						decimal_places=2 ,
						blank=True)
	total_deductions = models.DecimalField(
						max_digits=15,
						decimal_places=2 ,
						blank=True ,default=0)
	deductions 		= models.ManyToManyField(
						Deduction
						,blank=True)
	earnings 		= models.ManyToManyField(
						Earnings
						,blank=True)


	def __str__(self):
		return str(self.id)

	def total_salary(self):
		total = float(self.main_salary) + float(self.total_earnings) -float(self.total_deductions)
		return (total)
	def get_absolute_url(self):
		pk = self.id
		return reverse('salary:detail',kwargs={'pk':pk})




def m2m_earnings_resever(sender,action,instance,*args,**kwargs):
	#print(action)
	if action =='post_add' or action=='post_remove' or action=='post_clear':
		earning = instance.earnings.all()
		total_earning = 0
		for x in earning:
			total_earning += x.earnings
		# print(total)
		if instance.total_earnings != total_earning :
			instance.total_earnings = total_earning
			instance.save()

m2m_changed.connect(m2m_earnings_resever,
	   sender=Salary.earnings.through)

def m2m_deduction_resever(sender,action,instance,*args,**kwargs):
	#print(action)
	if action =='post_add' or action=='post_remove' or action=='post_clear':
		deduction = instance.deductions.all()
		total_deduction = 0
		for x in deduction:
			total_deduction += x.deductions
		# print(total)
		if instance.total_deductions != total_deduction :
			instance.total_deductions = total_deduction
			instance.save()

m2m_changed.connect(m2m_deduction_resever,
	   sender=Salary.deductions.through)