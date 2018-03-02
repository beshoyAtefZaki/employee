from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime as dt
# import datetime.datetime as dt
from mainapp.models import Employee
from .models import Salary,Deduction,Earnings
from . forms import DeductionForm ,EarningsForm


def add_salary(request):
	if request.method=='POST':
		pk 		= request.POST.get('pk')
		qs 		= Employee.objects.filter(id=pk)
		salary 	= request.POST.get('salary')
		if qs and salary:
			employee = qs.first()
			if employee.position =='employee' and (float(salary) < 5000 or float(salary) > 10000) :
				messages.add_message(request,messages.INFO,'employee salary shoud be inrange 5000 to 10000')
				return render(request,
						'salary/add_main_salary.html',{'employee':employee})
			if employee.position =='manager' and (float(salary) < 10000 or float(salary) > 19000) :
				messages.add_message(request,messages.INFO,'manager salary shoud be inrange 10000 to 19000')
				return render(request,
						'salary/add_main_salary.html',{'employee':employee})
			if employee.position =='ceo' and (float(salary) < 19000 or float(salary) > 25000) :
				messages.add_message(request,messages.INFO,'CEO salary shoud be inrange 19000 to 25000')
				return render(request,
						'salary/add_main_salary.html',{'employee':employee})				
		
			Salary.objects.create(
				employee=employee,
				main_salary = salary
				)
			return redirect('home')
	return render(request,
		'salary/add_main_salary.html')

def add_earning(request):
	if request.method=="POST":
		pk = request.POST.get('e_pk')
		qs = Salary.objects.filter(id=pk)
		if qs :
			salary 		= qs.first()
			earnings 	= request.POST.get('earnings')
			earnings 	= Earnings.objects.create(earnings=earnings)
			earnings.save()
			salary.earnings.add(earnings)
			if request.is_ajax():
				total_earnings = salary.total_earnings
				earning = earnings.earnings
				date = str(earnings.timestamp)
				total_salary = salary.total_salary()
				# print(str(date))
				t_date = (date).split(" ")
				# print(t_date)
				y_date = t_date[0].split("-")
				#print(y_date)
				h_time = t_date[1].split(":")
				# print(h_time)
				d_time = dt(int(y_date[0]) ,int(y_date[1]) ,
									int(y_date[2]) , int(h_time[0]) ,int(h_time[1]))
				date_f = dt.strftime(d_time ,"%b %d %Y %I %M %p")
				respond = {"total_earnings":total_earnings ,
							"total_salary" : total_salary,
							"earnings" : earning ,
							"date" : date_f ,} 
				return JsonResponse(respond)
			return redirect(salary.get_absolute_url())
	pass

def add_deduction(request):
	if request.method=="POST":
		pk = request.POST.get('d_pk')
		qs = Salary.objects.filter(id=pk)
		if qs :
			salary 		= qs.first()
			deduction 	= request.POST.get('deductions')
			deductions 	= Deduction.objects.create(deductions=deduction)
			deductions.save()
			salary.deductions.add(deductions)
			if request.is_ajax():
				total_dudcation = salary.total_deductions
				deducation = deductions.deductions
				date = deductions.timestamp
				total_salary = salary.total_salary()

				respond = {"total_dudcation":total_dudcation ,
							"total_salary" : total_salary,
							"deducation" : deducation ,
							"date" : date ,} 
				return JsonResponse(respond)
			return redirect(salary.get_absolute_url())
	pass

class SalaryDeatailView(DetailView):
	queryset 		= Salary.objects.all()
	template_name 	= "salary/detail.html"
	def get_context_data(self,*args,**kwargs):
		context = super( SalaryDeatailView ,
			 self).get_context_data(*args,**kwargs)
		salary 		= context.get('object')
		employee 	= salary.employee
		defult_deduction = None
		if employee.position =='employee':
			defult_deduction = float(salary.main_salary) * float(0.075)
		if employee.position =='manager':
			defult_deduction = float(salary.main_salary) * float(0.12)
		if employee.position =='ceo':
			defult_deduction = float(salary.main_salary) * float(0.15)
		deductions 	= salary.deductions.all()
		earnings 	= salary.earnings.all()
		d_form 		= DeductionForm()
		e_form 		= EarningsForm()
		d_form.fields["deductions"].initial=defult_deduction
		context['deductions']   =	deductions
		context['earnings'] 	=	earnings
		context['d_form'] 		=	d_form	
		context['e_form'] 		=	e_form		
		return context