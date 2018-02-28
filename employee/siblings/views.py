from django.shortcuts import render ,redirect
from mainapp.models import Employee
from .forms import SibilingsForm
from.models import Sibilings



def siblings_view(request):
	form = SibilingsForm(request.POST or None)
	if form.is_valid():
		slug = request.POST.get('employee')
		qs   = Employee.objects.filter(slug=slug)
		if qs.count() == 1 :
			employee 	= qs.first()
			relation	= form.cleaned_data.get(
									'relation')
			full_name	= form.cleaned_data.get(
									'full_name')
			age			= form.cleaned_data.get(
									'age')
			nationality	= form.cleaned_data.get(
									'nationality')
			Sibilings.objects.create(
						employee 	= employee ,
						relation 	= relation,
						full_name	= full_name,
						age 		= age,
						nationality = nationality)
			return redirect (
					employee.get_absolute_url())
		
	content= {
	'form' : form 
	}
	return render(request ,
			'siblings/create.html' ,content)

def siblings_update_view(request):
	
	if request.method=='POST': 
		pk = request.POST.get('pk')
		qs= Sibilings.objects.filter(id=pk)
		sibiling = qs.first()
		qs= Sibilings.objects.filter(id=pk)
		sibiling = qs.first()
		if request.POST.get('relation') :
			sibiling.relation=request.POST.get('relation')
		if request.POST.get('full_name'):
			sibiling.full_name=request.POST.get('full_name')
		if request.POST.get('age'):
			sibiling.age =request.POST.get('age')
		if request.POST.get('nationality'):
			sibiling.nationality=request.POST.get('nationality')
		sibiling.save()

	
	return redirect(
		sibiling.employee.get_absolute_url())

def delete_siblings(request):
	if request.method =='POST':
		pk =request.POST.get('pk')
		qs = Sibilings.objects.filter(id=pk)
		sp =  qs.first()  
		employee =sp.employee	
		Sibilings.objects.filter(id=pk).delete()
		return redirect(
		employee.get_absolute_url())